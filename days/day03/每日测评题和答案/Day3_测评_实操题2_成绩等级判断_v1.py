"""
Day 3 测评 - 实操题2: 成绩等级判断系统
解法1: 基础版 - 使用if-elif-else
"""

print("=" * 60)
print("成绩等级判断系统")
print("=" * 60)

# 存储学生数据
students = []
grades_count = {'优秀': 0, '良好': 0, '及格': 0, '不及格': 0}

# 输入5个学生的成绩
for i in range(5):
    print(f"\n第{i+1}个学生:")
    score = int(input("  请输入成绩: "))

    # 判断等级
    if score >= 90:
        grade = '优秀'
    elif score >= 80:
        grade = '良好'
    elif score >= 60:
        grade = '及格'
    else:
        grade = '不及格'

    students.append({'序号': i+1, '成绩': score, '等级': grade})
    grades_count[grade] += 1

# 输出统计结果
print("\n" + "=" * 60)
print("【成绩统计】")
print("=" * 60)

for student in students:
    print(f"学生{student['序号']}: {student['成绩']}分 - {student['等级']}")

print("\n" + "-" * 60)
print("【等级分布】")
for grade, count in grades_count.items():
    percentage = (count / 5) * 100
    print(f"{grade}: {count}人 ({percentage:.1f}%)")
print("=" * 60)
