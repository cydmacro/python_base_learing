# # 示例1：加法函数
# add = lambda a, b: a + b
# print(add(3, 5))  # 8

# # 示例2：平方函数
# square = lambda x: x**2
# print(square(4))  # 16

# #作为函数参数传递
# def operate(func, a, b):
#     return func(a, b)

# result = operate(lambda x, y: x * y, 3, 4)
# print(result)  # 12


# 示例：筛选偶数并平方
# numbers = [1, 2, 3, 4, 5]

# # Lambda + map/filter
# result1 = list(map(lambda x: x**2, filter(lambda x: x%2==0, numbers)))

# # 列表推导式
# result2 = [x**2 for x in numbers if x%2 ==0]

# print(result1, result2)  # [4, 16] [4, 16]

# invalid = lambda x: if x > 0: x else -x  # SyntaxError


    