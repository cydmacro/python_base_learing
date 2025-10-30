# Day 10: 综合项目实战(下) - 毕业大作业

> **学习时长**: 1天 (6小时)
> **难度**: ★★★★★
> **目标**: 完成毕业项目，掌握完整数据处理工具开发流程

---

## 📚 学习目标

### 核心知识点
- [x] CSV数据处理：读写、清洗、筛选、统计
- [x] OOP完整设计：方法链式调用、插件系统
- [x] 生产级代码：异常处理、日志系统、报告生成
- [x] 工具类封装：可复用、可扩展的数据处理类库

### AI场景应用
- CSV工具 → 标注数据的批量导入导出
- 数据清洗 → 提高标注数据质量
- 链式调用 → 简化数据处理流程
- 插件系统 → 扩展自定义数据处理逻辑

---

## 🎯 毕业项目：CSV数据处理工具

### 📦 Project 3: CSV数据处理工具

**目录**: `项目3_csv工具/`

| 版本 | 文件 | 行数 | 难度 | 特点 |
|------|------|------|------|------|
| v1 | **v1_basic.py** | 120行 | ★★☆☆☆ | 基础读写+简单清洗 |
| v2 | **v2_enhanced.py** | 220行 | ★★★☆☆ | 函数模块化+多种筛选 |
| v3 | **v3_complete.py** | 350行 | ★★★★★ | 完整OOP+链式调用+插件系统 |

---

## 📋 功能清单

### v1_basic.py - 基础版 (120行)

**核心功能**：
- CSV文件读写
- 去除缺失值
- 去除重复数据
- 基础数据展示

**核心代码**：
```python
import csv

# 读取CSV
with open('data.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# 清洗数据
cleaned_data = [row for row in data if all(row.values())]  # 去除缺失值

# 去除重复
seen = set()
unique_data = []
for row in cleaned_data:
    row_tuple = tuple(row.items())
    if row_tuple not in seen:
        seen.add(row_tuple)
        unique_data.append(row)

# 保存结果
with open('data_cleaned.csv', 'w', newline='', encoding='utf-8-sig') as f:
    if unique_data:
        writer = csv.DictWriter(f, fieldnames=unique_data[0].keys())
        writer.writeheader()
        writer.writerows(unique_data)
```

---

### v2_enhanced.py - 改进版 (220行)

**新增功能**：
- 函数模块化设计
- 条件筛选
- 范围筛选
- 数据统计

**核心代码**：
```python
def load_csv(file_path):
    """加载CSV文件"""
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        return list(reader)

def clean_data(data):
    """数据清洗"""
    # 去除缺失值
    data = [row for row in data if all(row.values())]
    # 去除重复
    seen = set()
    unique_data = []
    for row in data:
        row_tuple = tuple(row.items())
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_data.append(row)
    return unique_data

def filter_data(data, conditions):
    """条件筛选"""
    filtered = []
    for row in data:
        match = True
        for key, value in conditions.items():
            if key not in row or str(row[key]) != str(value):
                match = False
                break
        if match:
            filtered.append(row)
    return filtered

def filter_by_range(data, field, min_val, max_val):
    """范围筛选"""
    filtered = []
    for row in data:
        try:
            val = int(row.get(field, 0))
            if min_val <= val <= max_val:
                filtered.append(row)
        except ValueError:
            continue
    return filtered
```

---

### v3_complete.py - 完整版 (350行) ⭐

**新增功能**：
- 完整OOP类设计
- **方法链式调用**
- 灵活的筛选器
- 字段转换
- 添加计算列
- 完整统计报告
- 操作历史记录

**核心设计**：
```python
class DataProcessor:
    """CSV数据处理器 - 支持链式调用"""

    def __init__(self, file_path=None):
        self.file_path = file_path
        self.data = []
        self.original_count = 0
        self.operations = []  # 操作历史

    def load(self, file_path=None):
        """加载CSV文件 - 支持链式调用"""
        file_path = file_path or self.file_path
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            self.data = list(reader)
            self.original_count = len(self.data)
        self.operations.append(f"加载文件: {file_path} ({self.original_count}条)")
        return self  # 返回self实现链式调用

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
        """数据筛选 - 支持lambda条件"""
        before = len(self.data)
        self.data = [row for row in self.data if condition(row)]
        self.operations.append(f"筛选数据: 保留{len(self.data)}条,删除{before - len(self.data)}条")
        return self

    def transform(self, field, func):
        """数据转换 - 对指定字段应用函数"""
        for row in self.data:
            if field in row:
                row[field] = func(row[field])
        self.operations.append(f"转换字段: {field}")
        return self

    def add_column(self, col_name, func):
        """添加新列 - 根据现有数据计算"""
        for row in self.data:
            row[col_name] = func(row)
        self.operations.append(f"添加列: {col_name}")
        return self

    def save(self, file_path):
        """保存文件"""
        if not self.data:
            self.operations.append("保存失败: 没有数据")
            return self

        with open(file_path, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=self.data[0].keys())
            writer.writeheader()
            writer.writerows(self.data)
        self.operations.append(f"保存文件: {file_path} ({len(self.data)}条)")
        return self

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

        report += "\n" + "=" * 70
        return report
```

**链式调用示例**：
```python
# 这是v3的核心亮点 - 优雅的链式调用
processor = DataProcessor('data.csv') \
    .load() \
    .clean() \
    .filter(lambda row: int(row.get('score', 0)) >= 80) \
    .add_column('grade', lambda row: '优秀' if int(row.get('score', 0)) >= 90 else '良好') \
    .save('output.csv')

# 生成报告
print(processor.get_report())
```

---

## 📂 测评答案 (1个)

| 文件 | 说明 | 难度 |
|------|------|------|
| **Day10_测评_毕业项目_CSV处理工具_v1.py** | 毕业大作业标准答案 | ★★★★☆ |

**毕业要求**：
- 能独立完成v2级别代码(220行，函数封装)
- 理解v3级别的OOP设计和链式调用
- 能将工具应用到实际AI标注数据处理中

**测评题目**：查看 [`../../测评/Day10_测评.md`](../../测评/Day10_测评.md)

---

## 📖 配套教案

- **教案位置**: [`../../教案/第十章.md`](../../教案/第十章.md)
- **章节标题**: 综合项目实战(下) - 毕业大作业
- **内容范围**: 第十章全部内容

---

## 🎯 学习路径建议 (6小时)

### Step 1: v1_basic.py (1小时)
1. 理解CSV文件格式
2. 掌握csv模块的Reader和Writer
3. 实现基础清洗逻辑
4. 测试基础功能

### Step 2: v2_enhanced.py (2小时)
1. 学习函数模块化设计
2. 实现多种筛选方式
3. 添加数据统计功能
4. 理解模块化的好处

### Step 3: v3_complete.py (3小时) ⭐ 重点
1. **掌握OOP类设计** (1小时)
   - __init__初始化
   - 实例属性与方法
   - 返回self实现链式调用

2. **理解链式调用模式** (1小时)
   - 为什么每个方法都返回self
   - 如何设计可链式调用的API
   - 链式调用的优雅之处

3. **完整功能实战** (1小时)
   - 加载→清洗→筛选→转换→保存
   - 生成处理报告
   - 应用到真实数据

---

## 💡 链式调用深度解析

### 为什么需要链式调用？

**传统方式**（冗长繁琐）：
```python
processor = DataProcessor()
processor.load('data.csv')
processor.clean()
processor.filter(lambda row: int(row['score']) >= 80)
processor.add_column('grade', lambda row: '优秀' if int(row['score']) >= 90 else '良好')
processor.save('output.csv')
```

**链式调用**（优雅简洁）：
```python
processor = DataProcessor('data.csv') \
    .load() \
    .clean() \
    .filter(lambda row: int(row['score']) >= 80) \
    .add_column('grade', lambda row: '优秀' if int(row['score']) >= 90 else '良好') \
    .save('output.csv')
```

### 实现链式调用的核心

**关键点**：每个方法都返回`self`
```python
def load(self, file_path=None):
    # ... 执行加载逻辑
    return self  # 返回自己，实现链式调用

def clean(self):
    # ... 执行清洗逻辑
    return self  # 返回自己

def filter(self, condition):
    # ... 执行筛选逻辑
    return self  # 返回自己
```

---

## 🔍 常见问题

### Q1: v3的OOP设计比v2好在哪里？
**A**:
- 代码更模块化，易于维护
- 支持链式调用，使用更优雅
- 状态管理更清晰(self.data、self.operations)
- 易于扩展新功能(添加新方法即可)

### Q2: 什么时候用链式调用，什么时候不用？
**A**:
- ✅ **适合**：数据处理流水线(加载→清洗→转换→保存)
- ❌ **不适合**：需要中间结果的复杂逻辑

### Q3: 如何在实际AI工作中应用这个工具？
**A**:
```python
# 标注数据质量检查
processor = DataProcessor('label_export.csv') \
    .load() \
    .clean() \
    .filter(lambda row: row['confidence'] >= '0.9') \  # 只保留高置信度
    .transform('label', lambda x: x.lower()) \          # 标签统一小写
    .add_column('status', lambda row: 'valid') \        # 添加状态字段
    .save('labels_cleaned.csv')

print(processor.get_report())
```

### Q4: 毕业后应该达到什么水平？
**A**:
- ✅ 能独立编写v2级别代码(220行)
- ✅ 理解v3的OOP设计思想
- ✅ 能根据需求修改和扩展代码
- ✅ 能应用到实际AI数据处理工作

---

## 📊 本日项目统计

| 版本 | 行数 | 难度 | 核心特性 |
|------|------|------|----------|
| v1_basic | 120行 | ★★☆☆☆ | 基础功能 |
| v2_enhanced | 220行 | ★★★☆☆ | 函数模块化 |
| v3_complete | 350行 | ★★★★★ | OOP+链式调用 |
| 测评答案 | 200行 | ★★★★☆ | 综合应用 |
| **Day10总计** | **890行** | - | - |

---

## 🎓 毕业认证标准

### ✅ 基础要求（必须达到）
- [ ] 能独立完成v2级别代码(220行)
- [ ] 通过Day10毕业测评
- [ ] 理解OOP基本概念
- [ ] 能阅读v3级别代码

### ⭐ 优秀要求（推荐达到）
- [ ] 能独立完成v3级别代码(350行)
- [ ] 理解链式调用设计模式
- [ ] 能根据需求扩展新功能
- [ ] 能应用到实际工作中

### 🏆 卓越要求（挑战目标）
- [ ] 能设计自己的数据处理类库
- [ ] 能实现插件系统
- [ ] 能编写单元测试
- [ ] 能优化代码性能

---

## 🎉 毕业寄语

恭喜完成10天Python基础教学！

通过这10天的学习，你已经：
- ✅ 掌握Python核心语法
- ✅ 完成3个完整项目
- ✅ 编写超过1000行代码
- ✅ 具备AI训练师所需的Python技能

下一步建议：
1. **实战应用**：将所学应用到实际AI标注工作
2. **深化学习**：学习Pandas、NumPy等数据分析库
3. **项目练习**：完成更多实战项目
4. **代码规范**：提升代码质量和可维护性

**记住**：编程是一门实践的技能，唯有不断练习才能精进！

---

## 🔗 相关链接

- [上一章: Day 9 - 综合项目实战(上)](../day09/README.md) | [下一章: 课程结束]
- [返回总目录](../README.md)
- [查看教案](../../教案/第十章.md)
- [查看测评](../../测评/Day10_测评.md)
- [原项目参考](../../项目案例/)

---

**最后更新**: 2025-10-29
**完成情况**: ✅ 所有代码已创建
**测试状态**: ✅ v1/v2/v3版本全部可运行
**毕业要求**: ✅ 独立完成v2级别，理解v3设计
