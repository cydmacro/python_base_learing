"""
Project 3: CSV数据处理工具
版本: v1 - 基础版 (120行)
功能: 基础读写 + 简单清洗
难度: ★★☆☆☆
"""

import csv

print("=" * 70)
print("CSV数据处理工具 v1.0 - 基础版")
print("=" * 70)

# 创建测试数据
test_data = [
    ['name', 'age', 'score'],
    ['张三', '20', '85'],
    ['李四', '22', '92'],
    ['王五', '21', '78'],
    ['张三', '20', '85'],  # 重复
    ['赵六', '', '88'],    # 缺失值
]

# 写入CSV
with open('data.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerows(test_data)

print("✓ 测试数据已创建")

# 读取CSV
with open('data.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    data = list(reader)

print(f"\n读取到 {len(data)} 条数据")

# 简单清洗
print("\n开始清洗...")

# 去除缺失值
cleaned_data = [row for row in data if all(row.values())]
print(f"  删除缺失值: {len(data) - len(cleaned_data)}条")

# 去除重复
seen = set()
unique_data = []
for row in cleaned_data:
    row_tuple = tuple(row.items())
    if row_tuple not in seen:
        seen.add(row_tuple)
        unique_data.append(row)

print(f"  去除重复: {len(cleaned_data) - len(unique_data)}条")
print(f"\n清洗后剩余: {len(unique_data)}条")

# 保存结果
with open('data_cleaned.csv', 'w', newline='', encoding='utf-8-sig') as f:
    if unique_data:
        writer = csv.DictWriter(f, fieldnames=unique_data[0].keys())
        writer.writeheader()
        writer.writerows(unique_data)

print("\n✓ 已保存到: data_cleaned.csv")
