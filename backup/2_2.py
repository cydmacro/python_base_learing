# num = int("123")        # 字符串→整数 → 123  
# price = float("9.9")    # 字符串→浮点数 → 9.9  
# text = str(100)         # 整数→字符串 → "100"

# print(type(num), type(price), type(text),sep="\n")




# 1. 字符串转列表（按字符拆分）
# chars = list("Python")
# print(chars)  # 输出：['P', 'y', 't', 'h', 'o', 'n']

# # 2. 元组转列表
# tup = (1, 2, 3)
# lst = list(tup)
# print(lst)    # 输出：[1, 2, 3]

# #创建空列表（等效于 []）
# empty = list()
# print(empty)   # 输出：[]





# 1. 列表转元组
# lst = [10, 20, 30]
# tup = tuple(lst)
# print(tup)    # 输出：(10, 20, 30)

# # 2. 字典转元组（仅保留键）
# dct = {'a': 1, 'b': 2}
# keys = tuple(dct)
# print(keys)   # 输出：('a', 'b')

# #创建空元组（等效于 ()）
# empty = tuple()
# print(empty)   # 输出：()




# # 1. 键值对列表转字典
# pairs = [('a', 1), ('b', 2)]
# dct = dict(pairs)
# print(dct)    # 输出：{'a': 1, 'b': 2}

# # 2. 关键字参数创建
# dct = dict(name='Alice', age=25)
# print(dct)    # 输出：{'name': 'Alice', 'age': 25}

# #创建空字典（等效于 {}）
# empty = dict()
# print(empty)  # 输出：{}




# 1. 列表去重
# nums = [1, 2, 2, 3, 3]
# unique = set(nums)
# print(unique)  # 输出：{1, 2, 3}

# # 2. 字符串转字符集合
# chars = set("apple")
# print(chars)   # 输出：{'a', 'p', 'l', 'e'}

# #创建空集合（注意不能用 {}）
# empty = set()
# #empty = {}
# print(type(empty))
# print(empty)   # 输出：set()




# 生成 0-4
# r1 = range(5)
# print(list(r1))  # 输出 [0, 1, 2, 3, 4]

# # 生成 2-5（不包含5）
# r2 = range(2, 5)
# print(list(r2))  # 输出 [2, 3, 4]

# # for i in range(2, 10, 2):  
# #     print(i)  # 输出 2 4 6 8

# for i in range(10):  
#     print(i)  # 输出 0~9


# nums = [1, 2, 3]  
# print(sum(nums))   # 6  
# print(max(nums))   # 3


# import time  
# start = time.time()  
# print(start)
# time.sleep(2)  # 暂停2秒  
# end = time.time()  
# print(end)
# print(f"耗时：{end - start:.2f}秒")  # 耗时：2.00秒


import time  
now = time.strftime("%Y-%m-%d %H:%M:%S")  
print(now)  # 2030-10-01 14:30:00

