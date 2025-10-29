#!/usr/bin/env python3
"""
商业场景挑战演示

本文件展示了大模型在实际商业场景中的应用挑战和解决方案，
包括：客户服务、内容生成、数据分析、决策支持等业务场景。

技术要点：
- 真实商业场景的问题建模
- 多轮对话与上下文管理
- 专业领域知识的应用
- 商业规则与约束的处理
"""

from typing import List, Dict, Any, Optional
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.schema import HumanMessage, AIMessage
from pydantic import BaseModel, Field
from datetime import datetime, timedelta
import json
import random


class CustomerProfile(BaseModel):
    """客户档案模型"""
    customer_id: str = Field(description="客户ID")
    name: str = Field(description="客户姓名")
    tier: str = Field(description="客户等级", default="regular")
    purchase_history: List[Dict] = Field(description="购买历史", default_factory=list)
    preferences: List[str] = Field(description="偏好标签", default_factory=list)
    contact_history: List[Dict] = Field(description="联系历史", default_factory=list)


class BusinessInsight(BaseModel):
    """商业洞察模型"""
    insight_type: str = Field(description="洞察类型")
    title: str = Field(description="洞察标题")
    description: str = Field(description="详细描述")
    confidence: float = Field(description="置信度", ge=0.0, le=1.0)
    recommendations: List[str] = Field(description="建议行动", default_factory=list)
    impact_level: str = Field(description="影响级别", default="medium")


class BusinessChallengesDemo:
    """商业场景挑战演示类"""
    
    def __init__(self, model_name: str = "qwen-plus"):
        """初始化商业场景演示器"""
        # self.llm = ChatOpenAI(
        #     model=model_name,
        #     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        #     api_key="your_api_key_here",  # 请替换为有效的API密钥
        #     temperature=0.7
        # )
        self.llm = ChatOpenAI(
            model_name="qwen-plus",
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            api_key="sk-b860c820ce0249d9ac316d4598e81eb5",
            temperature=0.3
        )
        
        # 初始化新的消息历史管理
        self.message_history = ChatMessageHistory()
        self.max_messages = 10  # 保持最近10条消息
    
    def customer_service_bot(self, customer_query: str, customer_profile: CustomerProfile) -> str:
        """智能客服场景演示"""
        # 构建上下文感知的客服提示
        service_prompt = ChatPromptTemplate.from_messages([
            ("system", """你是一位专业的客服代表。请根据客户档案提供个性化的服务。

客户档案信息：
- 客户姓名：{customer_name}
- 客户等级：{customer_tier}
- 购买历史：{purchase_history}
- 偏好标签：{preferences}
- 联系历史：{contact_history}

服务原则：
1. 称呼客户姓名，体现个性化服务
2. 根据客户等级调整服务态度（VIP客户更加关注）
3. 参考购买历史提供相关建议
4. 考虑客户偏好进行推荐
5. 保持专业、友善、解决问题的态度

请回复客户的询问："""),
            ("human", "{query}")
        ])
        
        chain = service_prompt | self.llm
        response = chain.invoke({
            "customer_name": customer_profile.name,
            "customer_tier": customer_profile.tier,
            "purchase_history": json.dumps(customer_profile.purchase_history, ensure_ascii=False),
            "preferences": ", ".join(customer_profile.preferences),
            "contact_history": json.dumps(customer_profile.contact_history[-3:], ensure_ascii=False),  # 最近3次联系
            "query": customer_query
        })
        
        return response.content
    
    def content_generation_pipeline(self, content_type: str, target_audience: str, 
                                  key_points: List[str], brand_tone: str = "professional") -> Dict[str, Any]:
        """内容生成流水线演示"""
        
        # 1. 内容策略规划
        strategy_prompt = ChatPromptTemplate.from_messages([
            ("system", """你是内容策略专家。请为以下内容生成需求制定策略：
- 分析目标受众特点
- 确定内容结构和要点
- 制定传播策略"""),
            ("human", """内容类型：{content_type}
目标受众：{target_audience}
关键要点：{key_points}
品牌调性：{brand_tone}

请制定内容策略：""")
        ])
        
        # 2. 内容创作
        creation_prompt = ChatPromptTemplate.from_messages([
            ("system", """你是专业的内容创作者。根据策略要求创作高质量内容：
- 遵循品牌调性
- 符合目标受众特点
- 包含所有关键要点
- 确保内容吸引力和实用性"""),
            ("human", """基于以下策略创作内容：

策略：{strategy}

请创作内容：""")
        ])
        
        # 3. 内容优化
        optimization_prompt = ChatPromptTemplate.from_messages([
            ("system", """你是内容优化专家。请对内容进行多维度优化：
1. SEO关键词优化
2. 可读性提升
3. 互动性增强
4. 转化率优化"""),
            ("human", """原始内容：{original_content}

请优化内容：""")
        ])
        
        # 执行内容生成流程
        try:
            # 步骤1：策略规划
            strategy_chain = strategy_prompt | self.llm
            strategy_result = strategy_chain.invoke({
                "content_type": content_type,
                "target_audience": target_audience,
                "key_points": ", ".join(key_points),
                "brand_tone": brand_tone
            })
            
            # 步骤2：内容创作
            creation_chain = creation_prompt | self.llm
            content_result = creation_chain.invoke({
                "strategy": strategy_result.content
            })
            
            # 步骤3：内容优化
            optimization_chain = optimization_prompt | self.llm
            optimized_result = optimization_chain.invoke({
                "original_content": content_result.content
            })
            
            return {
                "strategy": strategy_result.content,
                "original_content": content_result.content,
                "optimized_content": optimized_result.content,
                "generation_success": True
            }
            
        except Exception as e:
            return {
                "error": str(e),
                "generation_success": False
            }
    
    def business_data_analyst(self, data_description: str, business_questions: List[str]) -> List[BusinessInsight]:
        """商业数据分析师演示"""
        insights = []
        
        for question in business_questions:
            analysis_prompt = ChatPromptTemplate.from_messages([
                ("system", """你是资深的商业数据分析师。请基于数据描述分析业务问题：

分析要求：
1. 深入理解业务背景和数据特征
2. 运用统计学和业务逻辑进行分析
3. 提供可执行的商业建议
4. 评估分析结果的可信度
5. 识别潜在的风险和机会

请提供结构化的分析结果。"""),
                ("human", """数据描述：{data_description}

业务问题：{business_question}

请进行深入分析并提供洞察：""")
            ])
            
            try:
                analysis_chain = analysis_prompt | self.llm
                result = analysis_chain.invoke({
                    "data_description": data_description,
                    "business_question": question
                })
                
                # 解析分析结果（这里简化处理，实际应用中可能需要更复杂的解析逻辑）
                insight = BusinessInsight(
                    insight_type="data_analysis",
                    title=f"关于 '{question}' 的分析洞察",
                    description=result.content,
                    confidence=random.uniform(0.7, 0.95),  # 示例置信度
                    recommendations=self._extract_recommendations(result.content),
                    impact_level=random.choice(["low", "medium", "high"])
                )
                insights.append(insight)
                
            except Exception as e:
                print(f"分析问题 '{question}' 时出错：{e}")
                continue
        
        return insights
    
    def strategic_decision_support(self, decision_context: str, options: List[str], 
                                 constraints: List[str]) -> Dict[str, Any]:
        """战略决策支持演示"""
        
        decision_prompt = ChatPromptTemplate.from_messages([
            ("system", """你是企业战略顾问。请为复杂的商业决策提供专业分析：

分析框架：
1. 现状分析（SWOT）
2. 选项评估（优劣势对比）
3. 风险评估（风险矩阵）
4. 实施建议（路线图）
5. 关键成功因素识别

请提供系统性的决策分析报告。"""),
            ("human", """决策背景：{context}

可选方案：
{options}

约束条件：
{constraints}

请提供决策分析：""")
        ])
        
        try:
            decision_chain = decision_prompt | self.llm
            analysis_result = decision_chain.invoke({
                "context": decision_context,
                "options": "\n".join([f"选项{i+1}：{opt}" for i, opt in enumerate(options)]),
                "constraints": "\n".join([f"约束{i+1}：{const}" for i, const in enumerate(constraints)])
            })
            
            # 风险评估
            risk_prompt = ChatPromptTemplate.from_messages([
                ("system", "你是风险管理专家。请识别决策中的潜在风险并提供缓解策略。"),
                ("human", "决策分析：{analysis}\n请识别风险和缓解措施：")
            ])
            
            risk_chain = risk_prompt | self.llm
            risk_result = risk_chain.invoke({"analysis": analysis_result.content})
            
            return {
                "decision_analysis": analysis_result.content,
                "risk_assessment": risk_result.content,
                "recommended_approach": self._extract_recommendation(analysis_result.content),
                "confidence_level": random.uniform(0.75, 0.9)
            }
            
        except Exception as e:
            return {"error": str(e), "analysis_success": False}
    
    def multi_turn_conversation(self, conversation_type: str = "sales") -> None:
        """多轮对话场景演示"""
        print(f"\n🗣️ 开始{conversation_type}对话演示（输入 'quit' 退出）")
        print("-" * 50)
        
        # 定义对话角色
        role_prompts = {
            "sales": "你是专业的销售代表，目标是了解客户需求并推荐合适的产品。",
            "support": "你是技术支持专家，专注于解决客户的技术问题。",
            "consultant": "你是业务顾问，帮助客户分析业务挑战并提供解决方案。"
        }
        
        conversation_prompt = ChatPromptTemplate.from_messages([
            ("system", role_prompts.get(conversation_type, role_prompts["sales"])),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])
        
        conversation_chain = conversation_prompt | self.llm
        
        while True:
            user_input = input("\n用户: ")
            if user_input.lower() == 'quit':
                break
                
            try:
                # 生成回复
                response = conversation_chain.invoke({
                    "input": user_input,
                    "chat_history": self.message_history.messages
                })
                
                print(f"AI助手: {response.content}")
                
                # 保存到消息历史
                self.message_history.add_user_message(user_input)
                self.message_history.add_ai_message(response.content)
                
                # 保持消息历史在限制范围内
                if len(self.message_history.messages) > self.max_messages:
                    self.message_history.messages = self.message_history.messages[-self.max_messages:]
                
            except Exception as e:
                print(f"对话出错：{e}")
    
    def _extract_recommendations(self, analysis_text: str) -> List[str]:
        """从分析文本中提取建议（简化实现）"""
        # 实际应用中可能需要更复杂的NLP处理
        recommendations = []
        lines = analysis_text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['建议', '推荐', '应该', '可以考虑']):
                recommendations.append(line.strip())
        return recommendations[:5]  # 最多返回5个建议
    
    def _extract_recommendation(self, analysis_text: str) -> str:
        """从分析文本中提取主要建议"""
        lines = analysis_text.split('\n')
        for line in lines:
            if '推荐' in line or '建议' in line:
                return line.strip()
        return "需要进一步分析"


def demonstrate_business_scenarios():
    """演示各种商业场景"""
    print("🏢 商业场景挑战演示")
    print("=" * 60)
    
    demo = BusinessChallengesDemo()
    
    # 1. 智能客服演示
    print("\n1️⃣ 智能客服场景演示")
    print("-" * 30)
    
    # 创建示例客户档案
    customer = CustomerProfile(
        customer_id="CUST001",
        name="张先生",
        tier="VIP",
        purchase_history=[
            {"product": "笔记本电脑", "amount": 8999, "date": "2024-01-15"},
            {"product": "鼠标", "amount": 299, "date": "2024-02-20"}
        ],
        preferences=["科技产品", "高性能", "品牌保障"],
        contact_history=[
            {"type": "咨询", "content": "产品保修问题", "date": "2024-03-01"},
            {"type": "投诉", "content": "配送延迟", "date": "2024-03-10"}
        ]
    )
    
    query = "我的笔记本电脑开机变慢了，这是怎么回事？能帮我看看吗？"
    
    try:
        service_response = demo.customer_service_bot(query, customer)
        print(f"客户咨询：{query}")
        print(f"客服回复：\n{service_response}")
    except Exception as e:
        print(f"客服演示出错：{e}")
    
    # 2. 内容生成流水线演示
    print("\n2️⃣ 内容生成流水线演示")
    print("-" * 30)
    
    try:
        content_result = demo.content_generation_pipeline(
            content_type="产品介绍文章",
            target_audience="科技爱好者",
            key_points=["AI技术", "用户体验", "性价比", "创新功能"],
            brand_tone="专业且易懂"
        )
        
        if content_result.get("generation_success"):
            print("📋 内容策略：")
            print(content_result["strategy"][:200] + "...")
            print("\n📝 原始内容：")
            print(content_result["original_content"][:200] + "...")
            print("\n✨ 优化内容：")
            print(content_result["optimized_content"][:200] + "...")
        else:
            print(f"内容生成失败：{content_result.get('error', '未知错误')}")
    except Exception as e:
        print(f"内容生成演示出错：{e}")
    
    # 3. 商业数据分析演示
    print("\n3️⃣ 商业数据分析演示")
    print("-" * 30)
    
    data_desc = """
    电商平台2024年Q1数据：
    - 总订单数：150万
    - 总销售额：5.2亿元
    - 新用户注册：32万
    - 用户复购率：45%
    - 移动端订单占比：78%
    - 平均订单价值：347元
    """
    
    business_questions = [
        "如何提升用户复购率？",
        "移动端占比高说明什么？应该如何优化？",
        "新用户转化策略有哪些机会？"
    ]
    
    try:
        insights = demo.business_data_analyst(data_desc, business_questions)
        for i, insight in enumerate(insights, 1):
            print(f"\n洞察{i}：{insight.title}")
            print(f"描述：{insight.description[:200]}...")
            print(f"置信度：{insight.confidence:.2f}")
            print(f"建议：{'; '.join(insight.recommendations[:2])}")
    except Exception as e:
        print(f"数据分析演示出错：{e}")
    
    # 4. 战略决策支持演示
    print("\n4️⃣ 战略决策支持演示")
    print("-" * 30)
    
    decision_context = "公司计划进入新的市场领域，需要在三个不同的方向中做出选择"
    options = [
        "投资AI教育平台，预计需要2000万启动资金",
        "开发企业级SaaS工具，预计需要1500万启动资金", 
        "进军海外电商市场，预计需要3000万启动资金"
    ]
    constraints = [
        "可用资金总额为2500万",
        "必须在18个月内看到初步成果",
        "团队规模不能超过50人"
    ]
    
    try:
        decision_result = demo.strategic_decision_support(decision_context, options, constraints)
        if decision_result.get("analysis_success", True):
            print(f"决策分析：\n{decision_result['decision_analysis'][:300]}...")
            print(f"\n风险评估：\n{decision_result['risk_assessment'][:200]}...")
            print(f"\n推荐方案：{decision_result['recommended_approach']}")
            print(f"置信水平：{decision_result.get('confidence_level', 0.8):.2f}")
        else:
            print(f"决策分析失败：{decision_result.get('error', '未知错误')}")
    except Exception as e:
        print(f"决策支持演示出错：{e}")
    
    # 5. 多轮对话演示（交互式）
    print("\n5️⃣ 多轮对话演示")
    print("-" * 30)
    print("可选对话类型：sales（销售）、support（技术支持）、consultant（顾问咨询）")

async def run_business_challenges_demo():
    """运行业务挑战演示 - 包装函数用于统一接口"""
    demonstrate_business_scenarios()
    
    # 注意：这个演示需要用户交互，在自动化演示中可能不适合
    # demo.multi_turn_conversation("sales")


if __name__ == "__main__":
    demonstrate_business_scenarios()