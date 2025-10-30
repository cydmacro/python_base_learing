"""
【文件说明】
章节: 第八章 - AI标注实战
知识点: Label Studio导出数据处理
实战应用: 将JSON格式转为CSV训练数据集

【核心技能】
- JSON文件读取与解析
- 嵌套数据提取
- 数据格式转换
"""

import json
import pandas as pd

# 模拟Label Studio导出的JSON数据
label_studio_data = [
    {
        "id": 1,
        "data": {"image": "/upload/cat001.jpg"},
        "annotations": [{
            "result": [{
                "value": {"choices": ["猫"]},
                "from_name": "label"
            }]
        }]
    },
    {
        "id": 2,
        "data": {"image": "/upload/dog002.jpg"},
        "annotations": [{
            "result": [{
                "value": {"choices": ["狗"]},
                "from_name": "label"
            }]
        }]
    },
    {
        "id": 3,
        "data": {"image": "/upload/bird003.jpg"},
        "annotations": [{
            "result": [{
                "value": {"choices": ["鸟"]},
                "from_name": "label"
            }]
        }]
    }
]

print("=" * 60)
print("Label Studio导出数据处理")
print("=" * 60)

# 提取文件名和标签
results = []

for item in label_studio_data:
    # 提取文件名(去除路径)
    filename = item['data']['image'].split('/')[-1]

    # 提取标签
    label = item['annotations'][0]['result'][0]['value']['choices'][0]

    results.append({
        '文件名': filename,
        '标签': label
    })

# 转为DataFrame
df = pd.DataFrame(results)

print("\n处理后的数据:")
print(df)

# 保存为CSV
output_file = 'training_labels.csv'
df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"\n✅ 已保存到: {output_file}")

print("""
💡 实战技巧:
1. Label Studio导出选择JSON格式
2. 用Python脚本批量处理
3. 转为CSV供模型训练使用
4. 检查数据质量后再训练

🎯 工作流程:
标注完成 → 导出JSON → Python处理 → CSV数据集 → 训练模型
""")
