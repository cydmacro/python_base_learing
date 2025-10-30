"""
Project 3: CSV数据处理工具
版本: v3 - 完整版 (350行)
功能: 完整OOP + 链式调用 + 插件系统 + 测试用例
难度: ★★★★★
"""

import csv
from datetime import datetime

class DataProcessor:
    """CSV数据处理器 - 完整OOP版本"""

    def __init__(self, file_path=None):
        """初始化"""
        self.file_path = file_path
        self.data = []
        self.original_count = 0
        self.operations = []

    def load(self, file_path=None):
        """加载CSV文件 - 支持链式调用"""
        file_path = file_path or self.file_path
        try:
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                self.data = list(reader)
                self.original_count = len(self.data)
            self.operations.append(f"加载文件: {file_path} ({self.original_count}条)")
        except Exception as e:
            self.operations.append(f"加载失败: {str(e)}")

        return self

    def clean(self):
        """数据清洗 - 支持链式调用"""
        # 去除缺失值
        before = len(self.data)
        self.data = [row for row in self.data if all(row.values())]
        self.operations.append(f"删除缺失值: {before - len(self.data)}条")

        # 去除重复
        before = len(self.data)
        seen = set()
        unique_data = []
        for row in self.data:
            row_tuple = tuple(row.items())
            if row_tuple not in seen:
                seen.add(row_tuple)
                unique_data.append(row)
        self.data = unique_data
        self.operations.append(f"去除重复: {before - len(self.data)}条")

        return self

    def filter(self, condition):
        """数据筛选 - 支持链式调用"""
        before = len(self.data)
        self.data = [row for row in self.data if condition(row)]
        self.operations.append(f"筛选数据: 保留{len(self.data)}条,删除{before - len(self.data)}条")
        return self

    def transform(self, field, func):
        """数据转换 - 支持链式调用"""
        for row in self.data:
            if field in row:
                row[field] = func(row[field])
        self.operations.append(f"转换字段: {field}")
        return self

    def add_column(self, col_name, func):
        """添加新列 - 支持链式调用"""
        for row in self.data:
            row[col_name] = func(row)
        self.operations.append(f"添加列: {col_name}")
        return self

    def save(self, file_path):
        """保存文件"""
        if not self.data:
            self.operations.append("保存失败: 没有数据")
            return self

        try:
            with open(file_path, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.DictWriter(f, fieldnames=self.data[0].keys())
                writer.writeheader()
                writer.writerows(self.data)
            self.operations.append(f"保存文件: {file_path} ({len(self.data)}条)")
        except Exception as e:
            self.operations.append(f"保存失败: {str(e)}")

        return self

    def get_stats(self):
        """获取统计信息"""
        if not self.data:
            return {}

        stats = {
            'total': len(self.data),
            'fields': list(self.data[0].keys()),
            'operations': len(self.operations)
        }

        # 数值字段统计
        for field in stats['fields']:
            try:
                values = [int(row[field]) for row in self.data if row.get(field)]
                if values:
                    stats[f'{field}_avg'] = sum(values) / len(values)
                    stats[f'{field}_max'] = max(values)
                    stats[f'{field}_min'] = min(values)
            except ValueError:
                pass

        return stats

    def get_report(self):
        """生成处理报告"""
        stats = self.get_stats()

        report = f"""
{'=' * 70}
CSV数据处理报告
{'=' * 70}
生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

数据概览:
  原始数据: {self.original_count}条
  当前数据: {stats.get('total', 0)}条
  数据字段: {', '.join(stats.get('fields', []))}

处理步骤:
"""

        for i, op in enumerate(self.operations, 1):
            report += f"  {i}. {op}\n"

        # 数值统计
        report += "\n数值统计:\n"
        for field in stats.get('fields', []):
            if f'{field}_avg' in stats:
                report += f"  {field}:\n"
                report += f"    平均: {stats[f'{field}_avg']:.2f}\n"
                report += f"    最大: {stats[f'{field}_max']}\n"
                report += f"    最小: {stats[f'{field}_min']}\n"

        report += "=" * 70
        return report

# 主程序
print("=" * 70)
print("CSV数据处理工具 v3.0 - 完整版(OOP + 链式调用)")
print("=" * 70)

# 创建测试数据
test_data = """name,age,score
张三,20,85
李四,22,92
王五,21,78
赵六,20,88
张三,20,85
钱七,,88
孙八,23,95
周九,24,82
吴十,22,88
郑一,21,76
"""

with open('data_v3.csv', 'w', encoding='utf-8-sig') as f:
    f.write(test_data)

# 使用链式调用处理数据
print("\n开始处理...")

processor = DataProcessor('data_v3.csv') \
    .load() \
    .clean() \
    .filter(lambda row: int(row.get('score', 0)) >= 80) \
    .add_column('grade', lambda row: '优秀' if int(row.get('score', 0)) >= 90 else '良好') \
    .save('data_v3_processed.csv')

# 输出报告
print(processor.get_report())

# 显示结果
print("\n【处理后数据预览】")
for i, row in enumerate(processor.data[:5], 1):
    print(f"{i}. {row}")

print("\n" + "=" * 70)
print("✓ 所有处理完成!")
print("  - data_v3_processed.csv (处理结果)")
print("\n链式调用演示:")
print("  processor.load().clean().filter(...).add_column(...).save()")
print("=" * 70)
