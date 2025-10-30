#AI⼤模型版-Python核⼼数据类型讲解
s1 = '单引号字符串'
s2 = "双引号字符串"
s3 = '''三引号支持
        多行字符串'''
s4 = r"原始字符串\n不转义"  # 输出：原始字符串\n不转义，r 代表原始字符串，转义符失效

print(s1,s2,s3,s4,sep="\n")

# print("C:\\")


# s = "Python"
# print(s[0])     # P（正向索引，从0开始）
# print(s[-1])    # n（反向索引，从-1开始）
# print(s[2:5])   # tho（切片：[起始, 结束)）
# print(s[::2])   # Pto（步长为2）



# s = "Hello, Python apple"
# print(s.upper())       # HELLO, PYTHON
# print(s.lower())       # hello, python
# print(s.title())       # Hello, Python（每个单词首字母大写）
# print(s.swapcase())    # hELLO, pYTHON（大小写互换）



# s = "Hello World"
# # 查找子串位置
# print(s.find("World"))     # 6（返回首次出现的索引，找不到返回-1）
# print(s.index("lo"))       # 3（类似find，但找不到会报错）

# # 统计出现次数
# print(s.count("l"))        # 3

# # 替换内容
# print(s.replace("World", "Python"))  # Hello Python


# 分割为列表
# s = "apple,banana,orange"
# print(s.split(","))        # ['apple', 'banana', 'orange']

# # 按行分割（适用于多行文本）
# text = "Line1\nLine2\nLine3"
# print(text.splitlines())   # ['Line1', 'Line2', 'Line3']

# # 连接列表为字符串
# lst = ["2030", "10", "01"]
# print("-".join(lst))       # 2030-10-01




s = "   Python   "
print(s.strip())       # "Python"（去除两侧空白）
print(s.lstrip())      # "Python   "（去左空白）
print(s.rstrip())      # "   Python"（去右空白）

# 填充对齐
print(s.center(20, "*"))   # ****Python****（居中填充）
print(s.zfill(10))         # 0000Python（左侧补零）

print("{} + {} = {}".format(3, 5, 8))         # 3 + 5 = 8（按顺序）
print("{name}喜欢{language}".format(name="小明", language="Python"))  # 关键字参数


price = 19.99
print(f"价格：{price:.2f}元")   # 价格：19.99元（保留两位小数）

