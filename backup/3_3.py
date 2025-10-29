
#生成1-10的平方列表

# for x in range(1,11):
#     print(x**2)

# sq = [x**2 for x in range(1,11)]
# print(sq)


# evens = [ x**2 for x in range(20) if x%2==0 ]
# print(evens)

# nums = [12, -5, 8, -3, 0]
# abs_nums = [x if x >= 0 else -x for x in nums]
# print(abs_nums)  # [12, 5, 8, 3, 0]

# 原始成绩列表
scores = [78, 92, 65, 88, 54]

# 转换为等级制（80分以上为A，其他为B）
grades = ['A' if score >=80 else 'B' for score in scores]
print(grades)  # 输出：['B', 'A', 'B', 'A', 'B']