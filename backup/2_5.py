# t1 = ()                 # 空元组
# t2 = (1,)               # 单元素元组 → (1,)
# t3 = (1, "a", True)     # 混合类型
# t4 = 4, 5, 6            # 括号可省略 → (4,5,6)

# print(t1, t2, t3, t4, sep="\n")

# print(type(t4))

# # t = (1, 2, 3)
# # t[0] = 100  # 报错：TypeError（不可修改元素）

# # t = ([1,23,4,5], 2, 3)
# # t[0].append(1111)
# # print(t[0])


# t9 = (1,)   # 正确 → 元组
# t10 = (1)    # 错误 → 整数1

# print(type(t9))
# print(type(t10))


# t = (1, 2, 2, 3, 2)
# print(t.count(2))  # 3

# t = ("a", "b", "c", "b")
# print(t.index("b"))  # 1


t = (10, 20, 30, 40, 50)

# # 索引
# print(t[0])     # 10（正向索引，从0开始）
# print(t[-1])    # 50（反向索引，从-1开始）

# # 切片（返回新元组）
# print(t[1:3])   # (20,30)（左闭右开）
# print(t[::2])   # (10,30,50)（步长2）


# t1 = (1, 2)
# t2 = (3, 4)

# # 拼接（生成新元组）
# t3 = t1 + t2    # (1,2,3,4)
# print(t3)

# # 重复
# t4 = t1 * 3     # (1,2,1,2,1,2)
# print(t4)


a, b, c = (10, 20, 30)
print(a, b, c)  # 10 20 30
print(type(a))


student = ("学习python-老王", 20, "Computer Science")
name, age, major = student
print(f"{name}主修{major}")  # 学习python-老王主修Computer Science

print(type(name))