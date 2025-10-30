"""
Day 8 测评 - 实操题2: 标注质量检查(一致性计算)
解法1: 完整版
"""

print("=" * 70)
print("标注一致性检查系统")
print("=" * 70)

# 标注员A的标注结果
annotator_a = [
    {'id': 1, 'file': 'img001.jpg', 'label': '猫'},
    {'id': 2, 'file': 'img002.jpg', 'label': '狗'},
    {'id': 3, 'file': 'img003.jpg', 'label': '鸟'},
    {'id': 4, 'file': 'img004.jpg', 'label': '猫'},
    {'id': 5, 'file': 'img005.jpg', 'label': '狗'},
    {'id': 6, 'file': 'img006.jpg', 'label': '鸟'},
    {'id': 7, 'file': 'img007.jpg', 'label': '猫'},
    {'id': 8, 'file': 'img008.jpg', 'label': '狗'},
    {'id': 9, 'file': 'img009.jpg', 'label': '鸟'},
    {'id': 10, 'file': 'img010.jpg', 'label': '猫'}
]

# 标注员B的标注结果
annotator_b = [
    {'id': 1, 'file': 'img001.jpg', 'label': '猫'},
    {'id': 2, 'file': 'img002.jpg', 'label': '狗'},
    {'id': 3, 'file': 'img003.jpg', 'label': '猫'},  # 不一致
    {'id': 4, 'file': 'img004.jpg', 'label': '猫'},
    {'id': 5, 'file': 'img005.jpg', 'label': '猫'},  # 不一致
    {'id': 6, 'file': 'img006.jpg', 'label': '鸟'},
    {'id': 7, 'file': 'img007.jpg', 'label': '猫'},
    {'id': 8, 'file': 'img008.jpg', 'label': '狗'},
    {'id': 9, 'file': 'img009.jpg', 'label': '鸟'},
    {'id': 10, 'file': 'img010.jpg', 'label': '狗'}  # 不一致
]

print("\n【对比两位标注员的结果】")
print("-" * 70)

# 计算一致性
total_samples = len(annotator_a)
consistent_samples = 0
inconsistent_list = []

for a, b in zip(annotator_a, annotator_b):
    if a['label'] == b['label']:
        consistent_samples += 1
    else:
        inconsistent_list.append({
            'id': a['id'],
            'file': a['file'],
            'label_a': a['label'],
            'label_b': b['label']
        })

# 计算一致率
consistency_rate = (consistent_samples / total_samples) * 100

# 生成质检报告
print("\n" + "=" * 70)
print("【质检报告】")
print("=" * 70)

print(f"\n总样本数: {total_samples}")
print(f"一致样本数: {consistent_samples}")
print(f"不一致样本数: {len(inconsistent_list)}")
print(f"一致率: {consistency_rate:.2f}%")

# 显示不一致样本列表
if inconsistent_list:
    print("\n【不一致样本列表】")
    print("-" * 70)
    print(f"{'ID':<6} {'文件名':<15} {'标注员A':<10} {'标注员B':<10}")
    print("-" * 70)

    for item in inconsistent_list:
        print(f"{item['id']:<6} {item['file']:<15} {item['label_a']:<10} {item['label_b']:<10}")

    print("-" * 70)
else:
    print("\n✓ 所有样本标注一致!")

# 质量评价
print("\n【质量评价】")
if consistency_rate >= 95:
    quality = "优秀"
    comment = "标注质量很高，可以直接使用"
elif consistency_rate >= 85:
    quality = "良好"
    comment = "标注质量较好，建议复审不一致样本"
elif consistency_rate >= 75:
    quality = "一般"
    comment = "需要重新培训标注员"
else:
    quality = "差"
    comment = "需要重新标注所有数据"

print(f"质量等级: {quality}")
print(f"建议: {comment}")

print("\n" + "=" * 70)
print("✓ 质检完成!")
