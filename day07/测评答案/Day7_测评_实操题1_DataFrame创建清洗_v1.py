"""
Day 7 测评 - 实操题1: DataFrame创建与清洗
解法1: 基础版
"""

import pandas as pd

print("=" * 70)
print("Pandas数据处理 - DataFrame创建与清洗")
print("=" * 70)

# 创建测试数据
data = {
    '文件名': ['cat_001.jpg', 'dog_002.jpg', 'bird_003.jpg', 'cat_001.jpg', 'fish_005.jpg'],
    '标签': ['猫', '狗', '鸟', '猫', None],
    '分数': [95, 88, 92, 95, 85]
}

df = pd.DataFrame(data)

print("\n【原始数据】")
print(df)
print(f"\n数据形状: {df.shape}")

# 数据清洗
print("\n" + "=" * 70)
print("【数据清洗】")
print("=" * 70)

# 1. 检查缺失值
print("\n1. 缺失值检查:")
print(df.isnull().sum())

# 2. 删除缺失值
df_cleaned = df.dropna()
print(f"\n删除缺失值后: {df_cleaned.shape[0]}条记录")

# 3. 去除重复数据
df_cleaned = df_cleaned.drop_duplicates()
print(f"去除重复后: {df_cleaned.shape[0]}条记录")

# 显示清洗后的数据
print("\n【清洗后数据】")
print(df_cleaned)

# 统计信息
print("\n" + "=" * 70)
print("【数据统计】")
print("=" * 70)
print(f"原始记录数: {df.shape[0]}")
print(f"清洗后记录数: {df_cleaned.shape[0]}")
print(f"删除记录数: {df.shape[0] - df_cleaned.shape[0]}")
print(f"数据质量: {df_cleaned.shape[0]/df.shape[0]*100:.1f}%")
