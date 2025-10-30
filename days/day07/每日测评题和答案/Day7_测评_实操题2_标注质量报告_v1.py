"""
Day 7 测评 - 实操题2: AI标注数据质检报告
解法1: 完整版
"""

import pandas as pd

print("=" * 70)
print("AI标注数据质量检查报告生成器")
print("=" * 70)

# 创建标注数据
data = {
    '文件名': ['img001.jpg', 'img002.jpg', 'img003.jpg', 'img004.jpg',
               'img005.jpg', 'img006.jpg', 'img007.jpg', 'img008.jpg'],
    '标签': ['猫', '狗', '鸟', '猫', '狗', '鸟', '猫', '猫'],
    '标注员': ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B'],
    '分数': [95, 88, 92, 98, 85, 90, 96, 87],
    '状态': ['完成', '完成', '完成', '完成', '完成', '完成', '完成', '待审核']
}

df = pd.DataFrame(data)

print("\n【原始标注数据】")
print(df)

# 生成质检报告
print("\n" + "=" * 70)
print("【质量检查报告】")
print("=" * 70)

# 1. 基本统计
total_count = len(df)
completed_count = (df['状态'] == '完成').sum()
pending_count = total_count - completed_count

print("\n1. 基本统计:")
print(f"   总样本数: {total_count}")
print(f"   已完成: {completed_count} ({completed_count/total_count*100:.1f}%)")
print(f"   待审核: {pending_count}")

# 2. 标签分布
print("\n2. 标签分布:")
label_dist = df['标签'].value_counts()
for label, count in label_dist.items():
    print(f"   {label}: {count}个 ({count/total_count*100:.1f}%)")

# 3. 分数统计
completed_df = df[df['状态'] == '完成']
avg_score = completed_df['分数'].mean()
max_score = completed_df['分数'].max()
min_score = completed_df['分数'].min()

print("\n3. 质量分数:")
print(f"   平均分: {avg_score:.2f}")
print(f"   最高分: {max_score}")
print(f"   最低分: {min_score}")

# 4. 标注员工作量
print("\n4. 标注员工作量:")
annotator_work = df['标注员'].value_counts()
for annotator, count in annotator_work.items():
    avg_score_annotator = df[df['标注员'] == annotator]['分数'].mean()
    print(f"   标注员{annotator}: {count}个样本, 平均分 {avg_score_annotator:.2f}")

# 5. 质量等级
print("\n5. 质量等级分布:")
df['质量等级'] = df['分数'].apply(lambda x: '优秀' if x >= 95 else
                                      '良好' if x >= 85 else '合格')
quality_dist = df['质量等级'].value_counts()
for level, count in quality_dist.items():
    print(f"   {level}: {count}个")

# 6. 潜在问题
print("\n6. 潜在问题:")
low_score = df[df['分数'] < 85]
if len(low_score) > 0:
    print(f"   ⚠ 发现 {len(low_score)} 个低分样本(< 85分)")
    for idx, row in low_score.iterrows():
        print(f"     - {row['文件名']}: {row['分数']}分 (标注员{row['标注员']})")
else:
    print("   ✓ 无低分样本")

# 7. 总体评价
print("\n" + "=" * 70)
print("【总体评价】")
print("=" * 70)

if avg_score >= 90:
    overall = "优秀"
    comment = "标注质量很高，可以直接用于训练"
elif avg_score >= 85:
    overall = "良好"
    comment = "标注质量较好，建议复审低分样本"
else:
    overall = "需改进"
    comment = "标注质量有待提升，需要全面复审"

print(f"总体评价: {overall}")
print(f"建议: {comment}")
print(f"完成率: {completed_count/total_count*100:.1f}%")
print(f"平均质量: {avg_score:.2f}分")

print("\n" + "=" * 70)
print("✓ 报告生成完成!")
