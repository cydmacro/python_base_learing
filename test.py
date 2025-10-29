# # # 执行简单测试
# from langchain_core.prompts import ChatPromptTemplate

# # print(ChatPromptTemplate.from_template("Hello 欢迎来到学习python-AI大模型开发课程 {title}!").format(title=",干就完了"))

# # # 应输出: Human: Hello 欢迎来到学习python-AI大模型开发课程 ,干就完了!

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model_name = "qwen-plus",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-b860c820ce0249d9ac316d4598e81eb5",
    temperature=0.7
    )

response = llm.invoke("你是谁?")

print(response)

