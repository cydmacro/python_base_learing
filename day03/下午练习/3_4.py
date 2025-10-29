# # 反转字典的键值对
# original = {'a': 1, 'b': 2, 'c': 3}
# reversed_dict = {v: k for k, v in original.items()}
# print(reversed_dict)  # {1: 'a', 2: 'b', 3: 'c'}


# students = [
#     {'name': 'Alice', 'math': 85, 'english': 90},
#     {'name': 'Bob', 'math': 78, 'english': 82},
#     {'name': 'Charlie', 'math': 92, 'english': 88}
# ]

# math_scores = {stu["name"] : stu["math"] for stu in students}
# print(math_scores)



# A = {1, 2, 3}
# B = {3, 4, 5}

# # 并集
# union = {x for x in A | B}  # {1,2,3,4,5}
# print(union)

# # 交集
# intersection = {x for x in A if x in B}  # {3}
# print(intersection)


# words = ['apple', 'banana', 'apple', 'orange', 'banana']
# unique_words = {word.upper() for word in words}
# print(unique_words)  # {'APPLE', 'BANANA', 'ORANGE'}


# text = "The quick brown fox jumps over the lazy dog"
# vowels = {'a', 'e', 'i', 'o', 'u'}

# # 提取文本中的唯一元音字母
# found_vowels = {char.lower() for char in text if char.lower() in vowels}
# print(found_vowels)  # {'a', 'e', 'i', 'o', 'u'}

a = (x for x in range(1,10)) # 返回的a是生成器对象
print(a)
b = tuple(a)       # 使用 tuple()函数，将生成器对象转换成元组
print(b)