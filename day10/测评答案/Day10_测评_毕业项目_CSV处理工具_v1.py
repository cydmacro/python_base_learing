"""
Day 10 测评 - 毕业项目: CSV数据处理综合工具
解法1: 完整OOP版本
难度: ★★★★☆
"""

import csv
from datetime import datetime

class DataProcessor:
    """CSV数据处理器"""

    def __init__(self, file_path):
        """初始化处理器"""
        self.file_path = file_path
        self.data = None
        self.original_count = 0
        self.cleaned_count = 0

    def load_data(self):
        """加载CSV数据"""
        try:
            with open(self.file_path, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                self.data = list(reader)
                self.original_count = len(self.data)
            print(f"✓ 成功加载 {self.original_count} 条数据")
            return True
        except FileNotFoundError:
            print(f"✗ 文件不存在: {self.file_path}")
            return False
        except Exception as e:
            print(f"✗ 加载失败: {str(e)}")
            return False

    def clean_data(self):
        """数据清洗"""
        if not self.data:
            print("✗ 没有数据需要清洗")
            return

        print("\n开始数据清洗...")

        # 1. 处理缺失值(删除有空值的行)
        before = len(self.data)
        self.data = [row for row in self.data if all(row.values())]
        after = len(self.data)
        print(f"  删除缺失值: {before - after}条")

        # 2. 去除重复数据
        before = len(self.data)
        seen = set()
        unique_data = []
        for row in self.data:
            row_tuple = tuple(row.items())
            if row_tuple not in seen:
                seen.add(row_tuple)
                unique_data.append(row)
        self.data = unique_data
        after = len(self.data)
        print(f"  去除重复: {before - after}条")

        # 3. 数据类型转换(如果有age和score字段)
        for row in self.data:
            if 'age' in row:
                try:
                    row['age'] = int(row['age'])
                except ValueError:
                    pass
            if 'score' in row:
                try:
                    row['score'] = int(row['score'])
                except ValueError:
                    pass

        self.cleaned_count = len(self.data)
        print(f"✓ 清洗完成,保留 {self.cleaned_count} 条数据")

    def filter_data(self, condition):
        """数据筛选"""
        if not self.data:
            print("✗ 没有数据需要筛选")
            return []

        filtered = [row for row in self.data if condition(row)]
        print(f"✓ 筛选结果: {len(filtered)} 条数据符合条件")
        return filtered

    def export_data(self, output_path, data=None):
        """导出数据"""
        if data is None:
            data = self.data

        if not data:
            print("✗ 没有数据可以导出")
            return False

        try:
            keys = data[0].keys()
            with open(output_path, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)
            print(f"✓ 成功导出到: {output_path}")
            return True
        except Exception as e:
            print(f"✗ 导出失败: {str(e)}")
            return False

    def get_report(self):
        """生成处理报告"""
        if not self.data:
            return "没有数据"

        report = f"""
{'=' * 70}
数据处理报告
{'=' * 70}
文件: {self.file_path}
生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

原始数据行数: {self.original_count}
清洗后行数: {self.cleaned_count}
删除行数: {self.original_count - self.cleaned_count}
数据保留率: {self.cleaned_count/self.original_count*100:.1f}%

数据字段: {', '.join(self.data[0].keys()) if self.data else '无'}
{'=' * 70}
"""
        return report


# ====================================================================
# 测试部分
# ====================================================================

print("=" * 70)
print("CSV数据处理综合工具 v1.0")
print("=" * 70)

# 1. 创建测试数据文件
print("\n【步骤1: 创建测试数据】")
test_data = """name,age,score
张三,20,85
李四,22,92
王五,21,78
赵六,20,85
张三,20,85
钱七,,88
孙八,23,
周九,24,95
吴十,22,88
郑一,21,82
"""

with open('test_data.csv', 'w', encoding='utf-8-sig') as f:
    f.write(test_data)
print("✓ 测试数据文件创建完成")

# 2. 使用DataProcessor处理数据
print("\n【步骤2: 加载数据】")
processor = DataProcessor('test_data.csv')
processor.load_data()

# 显示原始数据前5条
print("\n原始数据(前5条):")
for i, row in enumerate(processor.data[:5], 1):
    print(f"  {i}. {row}")

# 3. 数据清洗
print("\n【步骤3: 数据清洗】")
processor.clean_data()

# 4. 数据筛选
print("\n【步骤4: 数据筛选】")
# 筛选成绩>=80的学生
high_achievers = processor.filter_data(lambda row: int(row.get('score', 0)) >= 80)

print("\n优秀学生(成绩≥80):")
for student in high_achievers:
    print(f"  {student['name']}: {student['score']}分")

# 5. 导出数据
print("\n【步骤5: 导出数据】")
processor.export_data('cleaned_data.csv')
processor.export_data('high_achievers.csv', high_achievers)

# 6. 生成报告
print("\n【步骤6: 生成报告】")
print(processor.get_report())

# 7. 额外统计
print("【额外统计】")
if processor.data:
    scores = [int(row['score']) for row in processor.data]
    print(f"平均分: {sum(scores)/len(scores):.2f}")
    print(f"最高分: {max(scores)}")
    print(f"最低分: {min(scores)}")

    # 年龄分布
    ages = [int(row['age']) for row in processor.data]
    age_dist = {}
    for age in ages:
        age_dist[age] = age_dist.get(age, 0) + 1

    print("\n年龄分布:")
    for age, count in sorted(age_dist.items()):
        print(f"  {age}岁: {count}人")

print("\n" + "=" * 70)
print("✓ 所有处理完成!")
print("生成的文件:")
print("  - test_data.csv (原始数据)")
print("  - cleaned_data.csv (清洗后数据)")
print("  - high_achievers.csv (优秀学生)")
print("=" * 70)
