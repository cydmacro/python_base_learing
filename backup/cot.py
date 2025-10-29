#!/usr/bin/env python3
"""
Chain of Thought (CoT) 推理演示

本文件展示了Chain of Thought推理技术的核心实现和高级模式，
包括：零样本CoT、多步骤推理、复杂问题分解等技术。

技术要点：
- 步骤化推理过程
- 中间推理步骤的显式表达
- 复杂问题的层次化分解
- 推理链的质量评估
"""

from typing import List, Dict, Any
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
import re


class ReasoningStep(BaseModel):
    """推理步骤结构化表示"""
    step_number: int = Field(description="步骤编号")
    description: str = Field(description="步骤描述")
    reasoning: str = Field(description="推理过程")
    result: str = Field(description="中间结果")


class CoTAnalysis(BaseModel):
    """CoT分析结果结构"""
    problem: str = Field(description="问题描述")
    reasoning_steps: List[ReasoningStep] = Field(description="推理步骤")
    final_answer: str = Field(description="最终答案")
    confidence: float = Field(description="置信度", ge=0.0, le=1.0)


class ChainOfThoughtDemo:
    """Chain of Thought 推理演示类"""
    
    def __init__(self, model_name: str = "qwen-plus"):
        """初始化CoT演示器"""
        # self.llm = ChatOpenAI(
        #     model=model_name,
        #     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        #     api_key="b860c820ce0249d9ac316d4598e81eb5",  # 请替换为有效的API密钥
        #     temperature=0.3
        # )
        self.llm = ChatOpenAI(
            model_name="qwen-plus",
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            api_key="sk-b860c820ce0249d9ac316d4598e81eb5",
            temperature=0.3
        )

        # 定义CoT输出解析器
        self.parser = PydanticOutputParser(pydantic_object=CoTAnalysis)
    
    def zero_shot_cot(self, problem: str) -> str:
        """零样本CoT推理"""
        prompt = ChatPromptTemplate.from_messages([
            ("system", """你是一个逻辑推理专家。对于任何问题，请使用以下格式进行step-by-step思考：

思考过程：
步骤1：[描述第一个推理步骤]
步骤2：[描述第二个推理步骤]
...
步骤N：[描述最后的推理步骤]

因此，答案是：[最终答案]"""),
            ("human", "问题：{problem}\n请一步一步地思考。")
        ])
        
        chain = prompt | self.llm
        result = chain.invoke({"problem": problem})
        return result.content
    
    def few_shot_cot(self, problem: str) -> str:
        """少样本CoT推理"""
        prompt = ChatPromptTemplate.from_messages([
            ("system", """你是一个数学推理专家。我会给你一些例子展示如何进行推理：

例子1：
问题：小明买了3个苹果，每个2元，又买了2个橙子，每个3元，总共花了多少钱？
思考：
步骤1：计算苹果的总价 = 3个 × 2元/个 = 6元
步骤2：计算橙子的总价 = 2个 × 3元/个 = 6元  
步骤3：计算总花费 = 苹果总价 + 橙子总价 = 6元 + 6元 = 12元
答案：12元

例子2：
问题：一个班级有30名学生，其中60%是女生，女生中有1/3戴眼镜，问戴眼镜的女生有多少人？
思考：
步骤1：计算女生人数 = 30 × 60% = 30 × 0.6 = 18人
步骤2：计算戴眼镜的女生人数 = 18 × 1/3 = 6人
答案：6人

现在请用同样的方式解决问题。"""),
            ("human", "问题：{problem}")
        ])
        
        chain = prompt | self.llm
        result = chain.invoke({"problem": problem})
        return result.content



    def structured_cot(self, problem: str) -> CoTAnalysis:
        """结构化CoT推理"""
        prompt = ChatPromptTemplate.from_messages([
            ("system", """你是一个结构化推理专家。请对问题进行系统性的分析和推理。
            
{format_instructions}

请确保每个推理步骤都有清晰的逻辑链，并给出合理的置信度评估。"""),
            ("human", "问题：{problem}")
        ])
        
        chain = prompt | self.llm | self.parser
        result = chain.invoke({
            "problem": problem,
            "format_instructions": self.parser.get_format_instructions()
        })
        return result
    
    def multi_step_reasoning(self, complex_problem: str) -> Dict[str, Any]:
        """多步骤复杂推理"""
        # 步骤1：问题分解
        decomposition_prompt = ChatPromptTemplate.from_messages([
            ("system", "你是问题分解专家。请将复杂问题分解为多个子问题，每个子问题都应该是可以独立解决的。"),
            ("human", "复杂问题：{problem}\n请将这个问题分解为3-5个子问题：")
        ])
        
        # 步骤2：逐个解决子问题
        solving_prompt = ChatPromptTemplate.from_messages([
            ("system", "你是问题解决专家。请详细解决这个子问题，并给出推理过程。"),
            ("human", "子问题：{subproblem}\n背景信息：{context}\n请详细解决：")
        ])
        
        # 步骤3：综合答案
        synthesis_prompt = ChatPromptTemplate.from_messages([
            ("system", "你是信息综合专家。请根据各个子问题的解答，给出原始复杂问题的最终答案。"),
            ("human", "原始问题：{original_problem}\n子问题解答：{subproblem_answers}\n请给出综合答案：")
        ])
        
        # 执行分解
        decomp_chain = decomposition_prompt | self.llm
        decomp_result = decomp_chain.invoke({"problem": complex_problem})
        
        # 提取子问题
        subproblems = self._extract_subproblems(decomp_result.content)
        
        # 解决子问题
        subproblem_answers = []
        for i, subproblem in enumerate(subproblems, 1):
            solve_chain = solving_prompt | self.llm
            answer = solve_chain.invoke({
                "subproblem": subproblem,
                "context": f"这是第{i}个子问题，原始问题：{complex_problem}"
            })
            subproblem_answers.append({
                "subproblem": subproblem,
                "answer": answer.content
            })
        
        # 综合答案
        synthesis_chain = synthesis_prompt | self.llm
        final_answer = synthesis_chain.invoke({
            "original_problem": complex_problem,
            "subproblem_answers": str(subproblem_answers)
        })
        
        return {
            "original_problem": complex_problem,
            "decomposition": decomp_result.content,
            "subproblems": subproblems,
            "subproblem_answers": subproblem_answers,
            "final_answer": final_answer.content
        }
    
    def _extract_subproblems(self, decomposition_text: str) -> List[str]:
        """从分解文本中提取子问题"""
        # 简单的正则表达式提取，实际应用中可能需要更复杂的NLP处理
        pattern = r'(?:子问题\s*\d+[：:]\s*|问题\s*\d+[：:]\s*|步骤\s*\d+[：:]\s*)([^。！？\n]+)'
        matches = re.findall(pattern, decomposition_text)
        
        if not matches:
            # 如果没有找到标准格式，尝试按行分割
            lines = [line.strip() for line in decomposition_text.split('\n') if line.strip()]
            matches = [line for line in lines if len(line) > 10]  # 过滤太短的行
        
        return matches[:5]  # 最多返回5个子问题
    
    def reasoning_evaluation(self, problem: str, reasoning_chain: str) -> Dict[str, Any]:
        """推理链质量评估"""
        evaluation_prompt = ChatPromptTemplate.from_messages([
            ("system", """你是推理质量评估专家。请从以下维度评估推理链的质量：
1. 逻辑一致性（0-10分）
2. 步骤完整性（0-10分）  
3. 推理清晰度（0-10分）
4. 结论合理性（0-10分）
5. 整体质量（0-10分）

请给出具体的评分和改进建议。"""),
            ("human", "问题：{problem}\n推理链：{reasoning}\n请评估：")
        ])
        
        eval_chain = evaluation_prompt | self.llm
        evaluation = eval_chain.invoke({
            "problem": problem,
            "reasoning": reasoning_chain
        })
        
        return {"evaluation": evaluation.content}


def zero_shot_cot_techniques():
    """演示各种CoT技术"""
    print("🧠 Chain of Thought 推理技术演示")
    print("=" * 60)
    
    demo = ChainOfThoughtDemo()
    
    # 1. 零样本CoT演示
    print("\n1️⃣ 零样本CoT推理演示")
    print("-" * 30)
    problem1 = "一个水池可以容纳1000升水，现在有两个水管，A管每分钟注水30升，B管每分钟排水20升。如果同时开启两个水管，需要多长时间才能将空池子装满？"
    
    try:
        result1 = demo.zero_shot_cot(problem1)
        print(f"🔍 问题：{problem1}")
        print(f"🧠 推理过程：")
        print("-" * 50)
        # 直接打印，避免f-string格式化问题
        # """
        #     ⏺ 完美！现在输出正常了！🎉
        #     从测试结果可以看到：
        #   - ✅ 推理过程完整显示 - 包含所有步骤和数学公式
        #   - ✅ LaTeX公式正确渲染 - $30 - 20 = 10$ 和 $\frac{1000}{10} = 100$
        #   - ✅ 216字符完整输出 - 没有内容丢失
        #   - ✅ 调试信息确认 - 显示了原始字符串的前100个字符
        # 🔧 问题根源
        #     之前使用 print(f"{result1}") 时，f-string 格式化可能对包含的 LaTeX 数学公式标记（如 $ 符号和 \ 转义字符）产生了解析问题，导致显示异常。
        # """
        print(result1)
        print("-" * 50)
        print("✅ 零样本CoT推理完成")
        
        # 调试信息：显示原始字符串
        print(f"\n🔧 调试信息 - 原始内容长度: {len(result1)} 字符")
        print(f"🔧 调试信息 - 是否包含特殊字符: {repr(result1[:100])}...")
    except Exception as e:
        print(f"❌ 零样本CoT演示出错：{e}")

def feet_shot_cot_techniques():
    demo = ChainOfThoughtDemo()
    # 2. 少样本CoT演示
    print("\n2️⃣ 少样本CoT推理演示")
    print("-" * 30)
    problem2 = "一家商店搞促销，所有商品打8折，小李买了原价200元的衣服和原价150元的鞋子，如果她有一张满300元减50元的优惠券，她最终需要支付多少钱？"

    try:
        result2 = demo.few_shot_cot(problem2)
        print(f"问题：{problem2}")
        print(f"推理过程：\n{result2}")
    except Exception as e:
        print(f"少样本CoT演示出错：{e}")

def structured_cot_techniques():
    demo = ChainOfThoughtDemo()
    # 3. 结构化CoT演示
    print("\n3️⃣ 结构化CoT推理演示")
    print("-" * 30)
    problem3 = "公司要在5个城市之间建立网络连接，每两个城市之间的连接成本不同。如果要确保所有城市都能相互通信，且总成本最小，这是什么类型的问题？需要用什么算法解决？"

    try:
        result3 = demo.structured_cot(problem3)
        print(f"问题：{result3.problem}")
        print(f"推理步骤：")
        for step in result3.reasoning_steps:
            print(f"  步骤{step.step_number}：{step.description}")
            print(f"  推理：{step.reasoning}")
            print(f"  结果：{step.result}\n")
        print(f"最终答案：{result3.final_answer}")
        print(f"置信度：{result3.confidence}")
    except Exception as e:
        print(f"结构化CoT演示出错：{e}")

def multi_step_reasoning():
    demo = ChainOfThoughtDemo()
    # 4. 多步骤复杂推理演示
    print("\n4️⃣ 多步骤复杂推理演示")
    print("-" * 30)
    complex_problem = "一家初创科技公司计划开发一款AI产品，需要考虑技术可行性、市场需求、资金需求、团队建设和风险评估。如果你是这家公司的CTO，你会如何制定一个全面的产品开发战略？"

    try:
        result4 = demo.multi_step_reasoning(complex_problem)
        print(f"复杂问题：{result4['original_problem']}")
        print(f"\n问题分解：\n{result4['decomposition']}")
        print(f"\n子问题解答：")
        for i, answer in enumerate(result4['subproblem_answers'], 1):
            print(f"  子问题{i}：{answer['subproblem']}")
            print(f"  解答：{answer['answer']}\n")
        print(f"综合答案：\n{result4['final_answer']}")
    except Exception as e:
        print(f"多步骤推理演示出错：{e}")


if __name__ == "__main__":
    zero_shot_cot_techniques()
    feet_shot_cot_techniques()
    structured_cot_techniques
    multi_step_reasoning()