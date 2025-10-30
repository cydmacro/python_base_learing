"""
【第八章综合练习】
任务: 完整的标注数据处理流程

练习1: 处理Label Studio导出数据
练习2: 生成标注质量报告
练习3: 数据集划分(训练集/测试集)

下午练习时间: 2-3小时
"""

import json
import pandas as pd
import numpy as np

print("=" * 60)
print("第八章综合练习 - AI标注数据处理完整流程")
print("=" * 60)

# 练习1: 处理导出数据
print("\n【练习1: 处理Label Studio导出数据】")
print("需求: 将JSON格式转为CSV,并进行数据清洗")

# 模拟标注数据
annotations = []
for i in range(1, 51):
    label = np.random.choice(['猫', '狗', '鸟', None], p=[0.4, 0.3, 0.2, 0.1])
    annotations.append({
        'id': i,
        'data': {'image': f'/upload/img{i:03d}.jpg'},
        'annotations': [{
            'result': [{
                'value': {'choices': [label] if label else []},
                'from_name': 'label'
            }]
        }] if label else []
    })

# 处理数据
results = []
for item in annotations:
    filename = item['data']['image'].split('/')[-1]

    if item['annotations'] and item['annotations'][0]['result']:
        label = item['annotations'][0]['result'][0]['value']['choices'][0]
    else:
        label = None

    results.append({'文件名': filename, '标签': label})

df = pd.DataFrame(results)

print(f"\n原始数据: {len(df)}条")
print(f"缺失标签: {df['标签'].isnull().sum()}条")

# 清洗数据
df_clean = df.dropna(subset=['标签'])
print(f"清洗后: {len(df_clean)}条")

print("\n标签分布:")
print(df_clean['标签'].value_counts())

# 练习2: 质量报告
print("\n【练习2: 生成质量报告】")

report = f"""
===== 标注质量报告 =====
总样本数: {len(df)}
有效样本: {len(df_clean)}
缺失率: {df['标签'].isnull().sum()/len(df)*100:.1f}%

标签分布:
{df_clean['标签'].value_counts()}

质量评分: {100 - df['标签'].isnull().sum()/len(df)*100:.0f}/100
"""

print(report)

# 练习3: 数据集划分
print("【练习3: 划分训练集和测试集】")

# 80%训练,20%测试
train_size = int(len(df_clean) * 0.8)

df_shuffled = df_clean.sample(frac=1, random_state=42)  # 打乱数据
train_df = df_shuffled[:train_size]
test_df = df_shuffled[train_size:]

print(f"\n训练集: {len(train_df)}条")
print(train_df['标签'].value_counts())

print(f"\n测试集: {len(test_df)}条")
print(test_df['标签'].value_counts())

# 保存
train_df.to_csv('train.csv', index=False, encoding='utf-8-sig')
test_df.to_csv('test.csv', index=False, encoding='utf-8-sig')

print("\n✅ 数据集已保存: train.csv, test.csv")

print("""
💡 本章学到的技能:
1. JSON数据处理
2. 数据清洗流程
3. 质量报告生成
4. 数据集划分

🎯 下一章预告:
项目实战 - 文本清洗+图片分类完整项目
""")
