"""
Day 4 测评 - 实操题2: 数据筛选与统计
解法1: 基础版
"""

import random

print("=" * 60)
print("学生成绩筛选与统计系统")
print("=" * 60)

# 生成10个随机成绩(60-100)
scores = [random.randint(60, 100) for _ in range(10)]

print(f"\n原始成绩: {scores}")

# 筛选>=80的成绩
high_scores = [score for score in scores if score >= 80]

# 统计及格人数(>=60)
pass_count = sum(1 for score in scores if score >= 60)

# 计算平均分
average = sum(scores) / len(scores)

# 输出统计报告
print("\n" + "=" * 60)
print("【统计报告】")
print("=" * 60)
print(f"总人数: {len(scores)}")
print(f"优秀成绩(≥80): {high_scores}")
print(f"优秀人数: {len(high_scores)}人 ({len(high_scores)/len(scores)*100:.1f}%)")
print(f"及格人数: {pass_count}人 ({pass_count/len(scores)*100:.1f}%)")
print(f"平均分: {average:.2f}")
print(f"最高分: {max(scores)}")
print(f"最低分: {min(scores)}")
print("=" * 60)
