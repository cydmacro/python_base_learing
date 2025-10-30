
#默认是空格分隔
print("hello"," Python", "学习python",2030)
print("hello", "Python", "学习python",2030, sep="-")

print("hello", "Python", "学习python",2030, sep="%",end="")
print("hello", "Python", "学习python",2030, sep="*")

name = "老陈"
age = 18
#  # 按顺序填充
# print("Name : {}, Age : {}".format(name,age))
#  # 按关键字填充
# print("Name : {n}, Age : {a}".format(n="学习python",a=7))



print(f"姓名：{name}, 年龄{age}")

print(f"计算结果:{1+2*3}")

score = 95
print(f"成绩:{'优秀' if score>=90 else '良好'}")



# 错误示例1：忘记f前缀
name = "韩梅梅"
print(f"姓名：{name}")  # 不会报错，但输出原样文本


print(f"结果：{len('abc')}")  # 正确写法
#print(f"结果：{len 'abc'}")    # 语法错误（缺少括号）