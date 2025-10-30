"""
Day 2 测评 - 实操题2: 学生成绩管理系统
解法1: 基础版 - 使用列表
难度: ★★☆☆☆
"""

print("=" * 60)
print("学生成绩管理系统 - 基础版")
print("=" * 60)

# 学生姓名和成绩列表
names = ['张三', '李四', '王五']
scores = [85, 92, 78]

# 添加新学生
print("\n【添加学生】")
new_name = input("请输入学生姓名: ")
new_score = int(input("请输入学生成绩: "))

names.append(new_name)
scores.append(new_score)
print(f"✓ 已添加: {new_name} - {new_score}分")

# 计算平均分
average = sum(scores) / len(scores)

# 输出所有学生信息
print("\n" + "=" * 60)
print("【学生成绩列表】")
print("=" * 60)
print(f"{'序号':<8} {'姓名':<12} {'成绩':<10} {'等级':<10}")
print("-" * 60)

for i in range(len(names)):
    # 判断等级
    if scores[i] >= 90:
        grade = "优秀"
    elif scores[i] >= 80:
        grade = "良好"
    elif scores[i] >= 60:
        grade = "及格"
    else:
        grade = "不及格"

    print(f"{i+1:<8} {names[i]:<12} {scores[i]:<10} {grade:<10}")

print("-" * 60)
print(f"平均分: {average:.2f}")
print(f"最高分: {max(scores)} ({names[scores.index(max(scores))]})")
print(f"最低分: {min(scores)} ({names[scores.index(min(scores))]})")
print("=" * 60)
