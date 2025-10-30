# # 创建字典的多种方式
# dict1 = {}                      # 空字典
# dict2 = {"name": "Alice", "age": 25}
# dict3 = dict(name="Bob", age=30)  # 关键字参数创建
# dict4 = dict([("id", 1001), ("city", "Beijing")])  # 可迭代对象
# print(dict1,dict2,dict3,dict4,sep="\n")



student = {"name": "Alice", "age": 20}

# 查：通过键访问
print(student["name"])          # Alice（键不存在会报KeyError）
print(student.get("age", 18))   # 20（键不存在返回默认值18）

# # 增/改
# student["gender"] = "Female"    # 添加新键值对
# print(student)
# student["age"] = 21             # 修改已有键的值
# print(student)
# # 删
# del student["gender"]           # 删除指定键值对
# print(student)
# age = student.pop("age")        # 删除并返回值 → 21
# print(student)
# student.clear()                 # 清空字典 → {}
# print(student)

# print(student.items())
# print(student.keys())
# print(student.values())

# 错误示例：列表作为键
# invalid_dict = {["id"]: 1001}  # TypeError: unhashable type: 'list'


# text = "apple banana apple orange banana apple"
# words = text.split()
# word_count = {}
# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1
#
# print(word_count)  # {'apple':3, 'banana':2, 'orange':1}