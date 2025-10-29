


# numbers = [1, 2, 3, 4, 5]
# # squared = map(lambda x : x**2,numbers)
# # print(list(squared))

# # squared2 = [ x**2 for x in numbers]
# # print(squared2)
# even = filter(lambda x: x % 2 == 0, numbers)
# print(list(even))  # [2, 4]

#even = (x for x in numbers if x % 2 == 0)  # 惰性计算，节省内存

# from functools import reduce
# product = reduce(lambda a,b: a*b,[1,2,3,4])
# print(product)

# words = ["apple", "banana", "cherry", "date"]
# sorted_words = sorted(words, key=lambda x: len(x))
# print(sorted_words)  # ['date', 'apple', 'banana', 'cherry']


# data = [5, 12, 8, "10", 3.5, "7"]

# # 步骤1：过滤非整数
# filtered = filter(lambda x: isinstance(x, int), data)
# # 步骤2：转换为绝对值
# processed = map(abs, filtered)
# print(list(processed))  # [5, 12, 8, 3]



from functools import reduce

dicts = [{"a": 1}, {"b": 2}, {"a": 3, "c": 4}]
merged = reduce(lambda d1, d2: {**d1, **d2}, dicts)
print(merged)  # {'a':3, 'b':2, 'c':4}

