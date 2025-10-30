"""
Day 2 测评 - 实操题2: 学生成绩管理系统
解法2: 字典版 - 更好的数据结构
难度: ★★★☆☆
"""

print("=" * 60)
print("学生成绩管理系统 - 字典版")
print("=" * 60)

# 使用字典存储学生信息（更合理）
students = {
    '张三': 85,
    '李四': 92,
    '王五': 78
}

# 添加新学生
print("\n【添加学生】")
new_name = input("请输入学生姓名: ")
new_score = int(input("请输入学生成绩: "))

students[new_name] = new_score
print(f"✓ 已添加: {new_name} - {new_score}分")

# 计算平均分
average = sum(students.values()) / len(students)

# 输出所有学生信息
print("\n" + "=" * 60)
print("【学生成绩列表】")
print("=" * 60)
print(f"{'序号':<8} {'姓名':<12} {'成绩':<10} {'等级':<10}")
print("-" * 60)

# 定义等级判断函数
def get_grade(score):
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

# 遍历字典
for index, (name, score) in enumerate(students.items(), 1):
    grade = get_grade(score)
    print(f"{index:<8} {name:<12} {score:<10} {grade:<10}")

print("-" * 60)

# 统计信息
scores_list = list(students.values())
max_score = max(scores_list)
min_score = min(scores_list)

# 找出最高分和最低分的学生
top_student = [name for name, score in students.items() if score == max_score]
low_student = [name for name, score in students.items() if score == min_score]

print(f"平均分: {average:.2f}")
print(f"最高分: {max_score} ({', '.join(top_student)})")
print(f"最低分: {min_score} ({', '.join(low_student)})")
print("=" * 60)
