"""
【文件说明】
章节: 第八章 - AI标注实战
知识点: 标注质量检查脚本
实战应用: 自动检查标注数据质量,生成质检报告

【核心技能】
- 数据质量检查
- 标注一致性分析
- 质检报告生成
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("标注质量自动检查系统")
print("=" * 60)

# 模拟两个标注员的数据(用于一致性检查)
data_a = {
    '文件名': ['img001.jpg', 'img002.jpg', 'img003.jpg', 'img004.jpg', 'img005.jpg'],
    '标签': ['猫', '狗', '猫', '鸟', '狗']
}

data_b = {
    '文件名': ['img001.jpg', 'img002.jpg', 'img003.jpg', 'img004.jpg', 'img005.jpg'],
    '标签': ['猫', '狗', '狗', '鸟', '狗']  # img003标注不一致
}

df_a = pd.DataFrame(data_a)
df_b = pd.DataFrame(data_b)

print("\n标注员A的数据:")
print(df_a)

print("\n标注员B的数据:")
print(df_b)

# 合并对比
merged = df_a.merge(df_b, on='文件名', suffixes=('_A', '_B'))

print("\n对比结果:")
print(merged)

# 计算一致率
agreement = (merged['标签_A'] == merged['标签_B']).sum()
total = len(merged)
consistency = agreement / total * 100

print(f"\n标注一致率: {consistency:.1f}%")
print(f"一致样本: {agreement}个")
print(f"不一致样本: {total - agreement}个")

# 找出不一致的样本
inconsistent = merged[merged['标签_A'] != merged['标签_B']]

if len(inconsistent) > 0:
    print("\n需要复核的样本:")
    print(inconsistent)
else:
    print("\n✅ 所有样本标注一致!")

# 标签分布检查
print("\n" + "=" * 60)
print("标签分布检查")
print("=" * 60)

label_dist = df_a['标签'].value_counts()
print("\n标签分布:")
print(label_dist)

max_count = label_dist.max()
min_count = label_dist.min()
balance_ratio = min_count / max_count * 100

print(f"\n数据均衡度: {balance_ratio:.1f}%")

if balance_ratio < 70:
    print("⚠️ 警告: 数据不均衡,需要补充少数类别样本")
else:
    print("✅ 数据分布较为均衡")

print("""
💡 质检流程:
1. 双人标注同一批数据
2. 计算一致率(目标>95%)
3. 复核不一致样本
4. 分析常见错误,改进培训

🎯 质量标准:
- 标注一致率 > 95%
- 数据均衡度 > 70%
- 缺失率 < 1%
""")
