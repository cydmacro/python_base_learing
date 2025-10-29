

user_input = int(input("用户输入"))
#type()是判断类型
print(type(user_input))
print(f"用户的输入是：{user_input}") #str() int() float() 



# 多输入处理（通过split分割）
values = input("输入两个数字（空格分隔）：").split()
# map(func,lst) 讲传入的函数变量func作用在lst上每个元素中
a, b = map(int, values)
print(f"两数之和：{a + b}")


import math
print(math.sqrt(16))

from math import sqrt,pi
import my_module
print(sqrt(16))
print(pi)
my_module.greet()
