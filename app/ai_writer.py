from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import AsyncGenerator


# 封装AI问答的类
class AIWriter:
    def __init__(self):
        # 初始化语言模型
        self.llm = self.llm_model()

    # 定义一个返回自定义语言模型的方法
    def llm_model(self):
        #创建模型
        model = ChatOpenAI(
            model_name = "qwen-plus",
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            api_key="sk-b860c820ce0249d9ac316d4598e81eb5",
            temperature=0.7,
            streaming=True
        )
        return model
    
    #编写大模型运行的方法
    async def run_stream(self,query:str)->AsyncGenerator[str,None]:
        try:
            prompt_template = "用100个字介绍下的知识点或者介绍:{concept}"
            prompt = ChatPromptTemplate.from_template(prompt_template)
            
            chain = prompt | self.llm | StrOutputParser()
            
            async for chunk in chain.astream({"concept": query}):
                if isinstance(chunk,str):
                    yield chunk
                elif isinstance(chunk,dict) and "content" in chunk:
                    yield chunk['content']
                else:
                    yield str(chunk)
            
        except Exception as e:
            response = f"大模型运行失败：{str(e)}"
            
    async def chat(self, query: str):
        """处理用户消息并返回流式响应"""
        try:
            async for chunk in self.run_stream(query):
                yield chunk
        except Exception as e:
            yield f"发生错误: {str(e)}" 