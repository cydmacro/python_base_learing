# # 创建集合
# s1 = {1, 2, 3}              # 直接定义
# s2 = set([1, 2, 2, 3])      # 通过可迭代对象 → {1, 2, 3}
# empty_set = set()           # 空集合（不能使用 {}，因为这是空字典）

# print(s1,s2,empty_set,sep="\n")


# s = {3, 1, 2}
# print(list(s))  # 输出顺序不确定（如 [1,2,3] 或 [3,1,2]）


# s = set()   # 正确（空集合）
# # print(type(s))
# # s = {}      # 错误（创建的是空字典）
# # print(type(s))

# s.add(4)
# print(s)

# s.update([4,5])
# print(s)


# lst = [1, 2, 2, 3, 3, 3]
# unique = set(lst)        # {1, 2, 3}
# new_lst = list(unique)  # [1, 2, 3]（但顺序可能丢失）
# print(new_lst)


# 统计两个列表的共同元素
# list1 = [1, 2, 3]
# list2 = [2, 3, 4]
# common = set(list1) & set(list2)  # {2, 3}

# print(common)


# 用户权限集合
user_permissions = {"read", "write"}
required_permissions = {"write", "execute"}

# 检查用户是否具备所有必需权限
if required_permissions.issubset(user_permissions):
    print("权限足够")
else:
    print("缺少权限：", required_permissions - user_permissions)
    # 输出：缺少权限：{'execute'}