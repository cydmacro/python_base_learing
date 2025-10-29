"""
Day 8 测评 - 实操题1: Label Studio JSON数据解析
解法1: 基础版
"""

import json
import csv

print("=" * 70)
print("Label Studio数据导出处理")
print("=" * 70)

# 模拟Label Studio导出的JSON数据
data = {
    "data": {"image": "/upload/cat001.jpg"},
    "annotations": [{
        "result": [{
            "value": {"choices": ["猫"]}
        }]
    }]
}

print("\n【原始JSON数据】")
print(json.dumps(data, ensure_ascii=False, indent=2))

# 1. 提取文件名
file_name = data["data"]["image"].split("/")[-1]
print(f"\n1. 提取文件名: {file_name}")

# 2. 提取标签
label = data["annotations"][0]["result"][0]["value"]["choices"][0]
print(f"2. 提取标签: {label}")

# 3. 保存为CSV格式
csv_data = [
    ['文件名', '标签'],
    [file_name, label]
]

csv_file = 'label_output.csv'
with open(csv_file, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)

print(f"\n3. 已保存为CSV: {csv_file}")

# 验证CSV内容
print("\n【CSV文件内容】")
with open(csv_file, 'r', encoding='utf-8-sig') as f:
    print(f.read())

print("=" * 70)
print("✓ 处理完成!")
