# list1 = [1, 2, 3]                # 直接定义
# list2 = list("abc")              # 通过可迭代对象转换 → ['a', 'b', 'c']
# list3 = []                       # 空列表
# list4 = [1, "hello", True, [2, 3]]  # 可混合多种类型

# print(list1, list2, list3, list4, sep="\n")



lst = ["a", "b", "c", "d", "e"]
# 索引
print(lst[0])    # a（正向索引，从0开始）
print(lst[-1])   # e（反向索引，从-1开始）

# 切片（返回新列表）
print(lst[1:3])  # ['b', 'c']（左闭右开）
print(lst[::2])  # ['a', 'c', 'e']（步长2）