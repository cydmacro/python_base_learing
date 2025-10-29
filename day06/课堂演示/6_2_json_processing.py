"""
Day 6 课堂演示代码 - JSON文件处理与Label Studio数据解析
主题: JSON读写 + Label Studio导出数据处理 + CSV转换
适合: 文件操作+AI标注数据处理实战
"""

import json
import csv
from datetime import datetime

# ============================================================
# 第一部分: JSON基础 - 读取和写入
# ============================================================

# ============ 知识点 ============
# 1. JSON: JavaScript Object Notation，轻量级数据交换格式
# 2. Python的json模块: json.dump(), json.load()
# 3. JSON与Python字典的对应关系

# ============ 实战技巧 ============
# 1. json.load(f): 从文件读取JSON
# 2. json.dump(data, f): 将数据写入文件
# 3. indent参数: 格式化JSON使其可读
# 4. ensure_ascii=False: 支持中文

# ============ 易错点 ============
# 1. JSON键必须是字符串（用双引号）
# 2. JSON不支持Python的None，要用null
# 3. 文件打开模式：读取用'r'，写入用'w'
# 4. 编码问题：使用encoding='utf-8'

# ============ 扩展思考 ============
# 1. JSON和Python字典有什么区别？
# 2. 什么情况下用JSON？什么情况用CSV？
# 3. 如何处理大型JSON文件？

print("="*70)
print("JSON文件操作基础")
print("="*70)

# 创建示例数据
student_data = {
    "name": "张三",
    "age": 20,
    "city": "北京",
    "scores": {
        "python": 95,
        "math": 88,
        "english": 92
    },
    "hobbies": ["编程", "阅读", "运动"],
    "is_active": True
}

# 写入JSON文件
json_file = "student_data.json"
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(student_data, f, ensure_ascii=False, indent=2)
print(f"\n✓ 已创建JSON文件: {json_file}")

# 读取JSON文件
with open(json_file, 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)

print("\n读取的数据:")
print(f"姓名: {loaded_data['name']}")
print(f"年龄: {loaded_data['age']}")
print(f"Python成绩: {loaded_data['scores']['python']}")
print(f"爱好: {', '.join(loaded_data['hobbies'])}")


# ============================================================
# 第二部分: Label Studio导出数据格式
# ============================================================

# ============ 知识点 ============
# 1. Label Studio: AI数据标注工具
# 2. 导出格式: JSON数组，每个元素是一条标注记录
# 3. 数据结构: data(原始数据) + annotations(标注结果)

# ============ 实战技巧 ============
# 1. Label Studio JSON结构是嵌套的
# 2. 需要逐层访问: record -> annotations -> result -> value
# 3. 可能有多个标注员标注同一数据
# 4. 提取时注意None值判断

# ============ 易错点 ============
# 1. annotations是列表，可能为空
# 2. result也是列表，可能包含多个标注
# 3. 不同标注任务的value结构不同
# 4. 文件路径可能是相对路径

# ============ 扩展思考 ============
# 1. 如何处理多人标注的一致性？
# 2. 如何批量验证标注质量？
# 3. 如何统计标注进度？

print("\n" + "="*70)
print("Label Studio数据格式解析")
print("="*70)

# 模拟Label Studio导出的JSON数据
label_studio_data = [
    {
        "id": 1,
        "data": {
            "image": "/upload/images/cat_001.jpg",
            "text": "这是一只可爱的猫咪"
        },
        "annotations": [
            {
                "id": 101,
                "completed_by": 1,
                "result": [
                    {
                        "value": {
                            "choices": ["猫"]
                        },
                        "from_name": "label",
                        "to_name": "image",
                        "type": "choices"
                    }
                ],
                "was_cancelled": False,
                "created_at": "2024-01-15T10:30:00.000000Z"
            }
        ],
        "file_upload": "cat_001.jpg",
        "created_at": "2024-01-15T10:00:00.000000Z"
    },
    {
        "id": 2,
        "data": {
            "image": "/upload/images/dog_002.jpg",
            "text": "这是一只忠诚的狗狗"
        },
        "annotations": [
            {
                "id": 102,
                "completed_by": 1,
                "result": [
                    {
                        "value": {
                            "choices": ["狗"]
                        },
                        "from_name": "label",
                        "to_name": "image",
                        "type": "choices"
                    }
                ],
                "was_cancelled": False,
                "created_at": "2024-01-15T10:35:00.000000Z"
            }
        ],
        "file_upload": "dog_002.jpg",
        "created_at": "2024-01-15T10:05:00.000000Z"
    },
    {
        "id": 3,
        "data": {
            "image": "/upload/images/bird_003.jpg",
            "text": "这是一只美丽的鸟儿"
        },
        "annotations": [
            {
                "id": 103,
                "completed_by": 2,
                "result": [
                    {
                        "value": {
                            "choices": ["鸟"]
                        },
                        "from_name": "label",
                        "to_name": "image",
                        "type": "choices"
                    }
                ],
                "was_cancelled": False,
                "created_at": "2024-01-15T10:40:00.000000Z"
            }
        ],
        "file_upload": "bird_003.jpg",
        "created_at": "2024-01-15T10:10:00.000000Z"
    }
]

# 保存模拟数据
label_studio_file = "label_studio_export.json"
with open(label_studio_file, 'w', encoding='utf-8') as f:
    json.dump(label_studio_data, f, ensure_ascii=False, indent=2)
print(f"\n✓ 已创建Label Studio示例文件: {label_studio_file}")

# 读取Label Studio数据
with open(label_studio_file, 'r', encoding='utf-8') as f:
    ls_data = json.load(f)

print(f"\n总共有 {len(ls_data)} 条标注记录")


# ============================================================
# 第三部分: Label Studio数据解析
# ============================================================

# ============ 知识点 ============
# 1. 嵌套数据的访问方法
# 2. 列表索引和字典键的组合使用
# 3. 安全的数据提取(处理缺失值)

# ============ 实战技巧 ============
# 1. 先检查列表是否为空
# 2. 使用get()方法安全访问字典
# 3. 提取关键信息到简化的数据结构

# ============ 易错点 ============
# 1. 直接索引可能导致IndexError
# 2. 直接访问键可能导致KeyError
# 3. annotations可能为空列表

# ============ 扩展思考 ============
# 1. 如何处理多人标注的数据？
# 2. 如何筛选特定标注员的结果？
# 3. 如何验证标注的完整性？

print("\n" + "="*70)
print("解析Label Studio数据")
print("="*70)

# 解析每条记录
parsed_results = []

for record in ls_data:
    # 提取基本信息
    record_id = record.get('id')
    file_name = record.get('file_upload')
    image_path = record.get('data', {}).get('image')
    text = record.get('data', {}).get('text')

    # 提取标注结果
    annotations = record.get('annotations', [])
    if annotations:
        annotation = annotations[0]  # 取第一个标注
        result = annotation.get('result', [])

        if result:
            # 提取标签
            label = result[0].get('value', {}).get('choices', ['未标注'])[0]
        else:
            label = '未标注'

        annotator = annotation.get('completed_by')
        created_at = annotation.get('created_at')
    else:
        label = '未标注'
        annotator = None
        created_at = None

    # 保存解析结果
    parsed_results.append({
        'id': record_id,
        'file_name': file_name,
        'image_path': image_path,
        'text': text,
        'label': label,
        'annotator': annotator,
        'created_at': created_at
    })

# 显示解析结果
print("\n解析结果:")
print("-"*70)
for item in parsed_results:
    print(f"ID: {item['id']:2d} | 文件: {item['file_name']:15s} | 标签: {item['label']:4s} | 标注员: {item['annotator']}")
print("-"*70)


# ============================================================
# 第四部分: 转换为CSV格式
# ============================================================

# ============ 知识点 ============
# 1. CSV: Comma-Separated Values，逗号分隔值
# 2. csv模块: DictWriter用于写入字典数据
# 3. CSV适合表格数据，Excel可直接打开

# ============ 实战技巧 ============
# 1. 使用DictWriter自动处理表头
# 2. newline=''避免空行
# 3. extrasaction='ignore'忽略多余字段
# 4. 可以用Pandas简化操作

# ============ 易错点 ============
# 1. Windows下CSV乱码：使用utf-8-sig编码
# 2. 字段名顺序影响CSV列顺序
# 3. 包含逗号的字段要用引号包裹

# ============ 扩展思考 ============
# 1. CSV和Excel有什么区别？
# 2. 大数据量时如何优化？
# 3. 如何处理特殊字符？

print("\n" + "="*70)
print("转换为CSV格式")
print("="*70)

# 定义CSV字段
csv_fields = ['id', 'file_name', 'label', 'text', 'annotator', 'created_at']

# 写入CSV文件
csv_file = "label_data.csv"
with open(csv_file, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=csv_fields, extrasaction='ignore')
    writer.writeheader()  # 写入表头
    writer.writerows(parsed_results)  # 写入数据

print(f"\n✓ 已导出CSV文件: {csv_file}")
print(f"  包含 {len(parsed_results)} 条记录")
print(f"  字段: {', '.join(csv_fields)}")


# ============================================================
# 第五部分: 数据统计分析
# ============================================================

# ============ 知识点 ============
# 1. 字典统计: Counter或手动计数
# 2. 集合去重: set()
# 3. 列表推导式筛选数据

# ============ 实战技巧 ============
# 1. 统计各类别数量
# 2. 统计标注员工作量
# 3. 计算标注完成率

# ============ 易错点 ============
# 1. 空列表的统计
# 2. None值的处理
# 3. 除零错误

# ============ 扩展思考 ============
# 1. 如何可视化统计结果？
# 2. 如何计算标注一致性？
# 3. 如何识别异常标注？

print("\n" + "="*70)
print("数据统计分析")
print("="*70)

# 统计标签分布
label_count = {}
for item in parsed_results:
    label = item['label']
    label_count[label] = label_count.get(label, 0) + 1

print("\n【标签分布】")
for label, count in sorted(label_count.items()):
    percentage = count / len(parsed_results) * 100
    print(f"  {label}: {count}条 ({percentage:.1f}%)")

# 统计标注员工作量
annotator_count = {}
for item in parsed_results:
    annotator = item['annotator']
    if annotator:
        annotator_count[annotator] = annotator_count.get(annotator, 0) + 1

print("\n【标注员工作量】")
for annotator, count in sorted(annotator_count.items()):
    print(f"  标注员{annotator}: {count}条")

# 完成率统计
total = len(parsed_results)
completed = sum(1 for item in parsed_results if item['label'] != '未标注')
completion_rate = completed / total * 100

print("\n【完成率统计】")
print(f"  总任务数: {total}")
print(f"  已完成: {completed}")
print(f"  未完成: {total - completed}")
print(f"  完成率: {completion_rate:.1f}%")


# ============================================================
# 第六部分: 完整工作流 - 封装为函数
# ============================================================

# ============ 知识点 ============
# 1. 函数封装提高代码复用性
# 2. 文档字符串说明函数用途
# 3. 返回值便于后续处理

# ============ 实战技巧 ============
# 1. 一个函数完成一个功能
# 2. 参数提供灵活性
# 3. 错误处理保证健壮性

# ============ 易错点 ============
# 1. 函数命名要清晰
# 2. 参数默认值的设置
# 3. 异常处理的位置

# ============ 扩展思考 ============
# 1. 如何设计更通用的转换函数？
# 2. 如何添加日志记录？
# 3. 如何支持批量处理？

def parse_label_studio_json(json_file):
    """
    解析Label Studio导出的JSON文件

    参数:
        json_file: JSON文件路径

    返回:
        解析后的数据列表
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    results = []
    for record in data:
        annotations = record.get('annotations', [])
        if annotations and annotations[0].get('result'):
            label = annotations[0]['result'][0]['value']['choices'][0]
        else:
            label = '未标注'

        results.append({
            'id': record.get('id'),
            'file_name': record.get('file_upload'),
            'label': label,
            'text': record.get('data', {}).get('text', ''),
            'annotator': annotations[0].get('completed_by') if annotations else None
        })

    return results


def save_to_csv(data, csv_file, fields=None):
    """
    将数据保存为CSV文件

    参数:
        data: 数据列表（字典列表）
        csv_file: CSV文件路径
        fields: 字段列表，None则使用第一条数据的keys
    """
    if not data:
        print("警告: 数据为空")
        return

    if fields is None:
        fields = list(data[0].keys())

    with open(csv_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(data)

    print(f"✓ 已保存 {len(data)} 条记录到 {csv_file}")


print("\n" + "="*70)
print("使用封装函数处理数据")
print("="*70)

# 使用函数处理
results = parse_label_studio_json(label_studio_file)
save_to_csv(results, "processed_labels.csv")

# 生成处理报告
report = {
    "处理时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "输入文件": label_studio_file,
    "输出文件": "processed_labels.csv",
    "总记录数": len(results),
    "标注完成数": sum(1 for r in results if r['label'] != '未标注'),
    "标签类型": list(set(r['label'] for r in results))
}

# 保存报告
report_file = "processing_report.json"
with open(report_file, 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print(f"\n✓ 处理报告已保存: {report_file}")


# ============================================================
# 课后练习题
# ============================================================
"""
基础题:
1. 读取一个JSON配置文件，修改某些参数后保存
2. 将学生信息列表(字典列表)保存为JSON
3. 读取CSV文件，转换为JSON格式

进阶题:
4. 处理多层嵌套的JSON数据
   例如: {"a": {"b": {"c": "value"}}}
   提取深层嵌套的值

5. 合并多个Label Studio导出文件
   读取多个JSON文件，合并为一个

6. 标注数据验证器
   检查Label Studio导出数据的完整性:
   - 是否有未标注的数据
   - 是否有重复标注
   - 标签是否在允许范围内

实战题:
7. 批量处理Label Studio数据
   - 读取指定目录下所有JSON文件
   - 统一解析并合并
   - 按标签分类保存为不同CSV

8. 标注质量分析系统
   - 读取多人标注的相同数据
   - 计算标注一致性
   - 生成质量报告(JSON格式)

9. Label Studio数据转换工具
   - 支持JSON转CSV
   - 支持CSV转JSON(反向导入)
   - 支持数据筛选和清洗
   - 生成统计图表

挑战题:
10. 完整的AI数据处理pipeline
    - 读取Label Studio导出数据
    - 数据清洗(去重、验证)
    - 格式转换(JSON/CSV/COCO)
    - 统计分析和可视化
    - 生成训练集/验证集/测试集
    - 导出为模型训练格式
"""

print("\n" + "="*70)
print("JSON处理演示完成")
print("="*70)
print("\n提示: 已生成的文件:")
print("  - student_data.json (基础示例)")
print("  - label_studio_export.json (Label Studio模拟数据)")
print("  - label_data.csv (CSV导出)")
print("  - processed_labels.csv (处理后数据)")
print("  - processing_report.json (处理报告)")
print("\n请完成课后练习，巩固JSON处理技能!")
print("="*70)
