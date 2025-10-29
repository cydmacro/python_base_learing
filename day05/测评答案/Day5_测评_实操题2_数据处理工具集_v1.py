"""
Day 5 测评 - 实操题2: 数据处理工具集
解法1: 基础版 - 三个独立函数
"""

def calc_avg(scores):
    """计算平均分"""
    return sum(scores) / len(scores)


def filter_pass(scores):
    """筛选及格成绩(>=60)"""
    return [score for score in scores if score >= 60]


def count_level(scores):
    """统计各等级人数"""
    levels = {'优秀': 0, '良好': 0, '及格': 0, '不及格': 0}

    for score in scores:
        if score >= 90:
            levels['优秀'] += 1
        elif score >= 80:
            levels['良好'] += 1
        elif score >= 60:
            levels['及格'] += 1
        else:
            levels['不及格'] += 1

    return levels


# 测试数据
test_scores = [75, 85, 55, 95, 65, 45, 80]

print("=" * 60)
print("数据处理工具集测试")
print("=" * 60)

print(f"\n测试数据: {test_scores}")

# 1. 计算平均分
avg = calc_avg(test_scores)
print(f"\n【平均分】")
print(f"平均分: {avg:.2f}")

# 2. 筛选及格成绩
passed = filter_pass(test_scores)
print(f"\n【及格成绩】")
print(f"及格成绩: {passed}")
print(f"及格人数: {len(passed)}/{len(test_scores)} ({len(passed)/len(test_scores)*100:.1f}%)")

# 3. 统计各等级人数
levels = count_level(test_scores)
print(f"\n【等级分布】")
for level, count in levels.items():
    percentage = (count / len(test_scores)) * 100
    bar = '█' * count
    print(f"{level:6s}: {count}人 ({percentage:5.1f}%) {bar}")

# 完整统计报告
print("\n" + "=" * 60)
print("【完整统计报告】")
print("=" * 60)
print(f"总人数: {len(test_scores)}")
print(f"平均分: {avg:.2f}")
print(f"最高分: {max(test_scores)}")
print(f"最低分: {min(test_scores)}")
print(f"及格率: {len(passed)/len(test_scores)*100:.1f}%")
print("\n等级分布:")
for level, count in levels.items():
    print(f"  {level}: {count}人")
print("=" * 60)
