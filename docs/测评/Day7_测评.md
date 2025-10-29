# Day 7 测评 - Pandas数据处理

**时间**: 30分钟 | **总分**: 100分

---

## 一、选择题(40分,10题)

### 1. 以下哪个是正确的CSV读取方式?(4分)
A. `df = pandas.read_csv('data.csv')`
B. `df = pd.read_csv('data.csv', encoding='utf-8')`
C. `df = read_csv('data.csv')`
D. `df = pd.load('data.csv')`

**答案**: B

---

### 2. 如何统计DataFrame中每列的缺失值数量?(4分)
A. `df.missing()`
B. `df.isnull().sum()`
C. `df.count_na()`
D. `df.check_null()`

**答案**: B

---

### 3. 删除重复值的正确方法是?(4分)
A. `df.remove_duplicates()`
B. `df.drop_duplicates()`
C. `df.delete_duplicates()`
D. `df.unique()`

**答案**: B

---

### 4. 以下哪个条件筛选语法是正确的?(4分)
A. `df[df['年龄'] > 18 and df['性别'] == '男']`
B. `df[(df['年龄'] > 18) & (df['性别'] == '男')]`
C. `df[df['年龄'] > 18 && df['性别'] == '男']`
D. `df[(df['年龄'] > 18) and (df['性别'] == '男')]`

**答案**: B

---

### 5. 如何只保存CSV的特定列?(4分)
A. `df.to_csv('out.csv', columns=['A', 'B'])`
B. `df[['A', 'B']].to_csv('out.csv', index=False)`
C. `df.save(['A', 'B'], 'out.csv')`
D. `df.export('out.csv', cols=['A', 'B'])`

**答案**: B

---

### 6. value_counts()函数的作用是?(4分)
A. 计算数值列的总和
B. 统计每个值出现的次数
C. 计算列的平均值
D. 删除重复值

**答案**: B

---

### 7. fillna()函数的作用是?(4分)
A. 删除缺失值
B. 填充缺失值
C. 查找缺失值
D. 统计缺失值

**答案**: B

---

### 8. 如何筛选标签为"猫"或"狗"的数据?(4分)
A. `df[df['标签'] == '猫' or '狗']`
B. `df[df['标签'] in ['猫', '狗']]`
C. `df[df['标签'].isin(['猫', '狗'])]`
D. `df[df['标签'] == ['猫', '狗']]`

**答案**: C

---

### 9. 以下哪个会导致CSV保存时多一列行号?(多选,8分)
A. `df.to_csv('out.csv')`
B. `df.to_csv('out.csv', index=True)`
C. `df.to_csv('out.csv', index=False)`
D. `df.save('out.csv')`

**答案**: AB

---

### 10. 数据清洗三板斧包括?(多选,8分)
A. 处理缺失值
B. 处理异常值
C. 处理重复值
D. 数据加密

**答案**: ABC

---

## 二、实操题(60分)

### 实操题1(20分): 基础数据处理

编写Python代码完成以下任务:

1. 创建一个DataFrame,包含以下数据:
   ```python
   data = {
       '文件名': ['img1.jpg', 'img2.png', 'img3.jpg', 'img1.jpg'],
       '标签': ['猫', '狗', None, '猫'],
       '分数': [95, 88, 75, 95]
   }
   ```

2. 删除标签缺失的行
3. 删除重复的行
4. 保存为`clean_data.csv`(不保存行号)
5. 打印清洗前后的行数

**要求**:
- 使用Pandas库
- 代码能正常运行
- 输出格式清晰

---

### 实操题2(40分): AI标注数据质检

某AI项目有一份标注数据`label_data.csv`,包含以下字段:
- 文件名
- 标签(猫/狗/鸟)
- 标注员
- 质检状态(通过/未通过/待质检)

请编写代码完成:
1. 读取数据(自己创建测试数据,至少10条)
2. 统计每个标签的数量
3. 统计每个标注员的工作量
4. 计算质检通过率
5. 生成质检报告(打印到控制台)

**质检报告格式**:
```
===== 质检报告 =====
总数据: XX条
标签分布:
  猫: XX条
  狗: XX条
  鸟: XX条
标注员工作量:
  张三: XX条
  李四: XX条
质检通过率: XX%
```

**评分标准**:
- 数据创建正确(10分)
- 统计功能实现(20分)
- 报告格式规范(10分)

---

## 答案示例

### 实操题1参考答案

```python
import pandas as pd

# 1. 创建DataFrame
data = {
    '文件名': ['img1.jpg', 'img2.png', 'img3.jpg', 'img1.jpg'],
    '标签': ['猫', '狗', None, '猫'],
    '分数': [95, 88, 75, 95]
}
df = pd.DataFrame(data)

print(f"原始数据: {len(df)}行")

# 2. 删除标签缺失
df = df.dropna(subset=['标签'])

# 3. 删除重复
df = df.drop_duplicates()

print(f"清洗后: {len(df)}行")

# 4. 保存
df.to_csv('clean_data.csv', index=False, encoding='utf-8-sig')

print("✅ 已保存到clean_data.csv")
```

### 实操题2参考答案

```python
import pandas as pd

# 创建测试数据
data = {
    '文件名': [f'img{i}.jpg' for i in range(1, 11)],
    '标签': ['猫', '狗', '鸟', '猫', '狗', '鸟', '猫', '狗', '鸟', '猫'],
    '标注员': ['张三']*5 + ['李四']*5,
    '质检状态': ['通过', '通过', '未通过', '通过', '待质检',
                 '通过', '通过', '未通过', '通过', '通过']
}

df = pd.DataFrame(data)

# 生成报告
print("=" * 50)
print(" " * 15 + "质检报告")
print("=" * 50)

print(f"\n总数据: {len(df)}条")

print("\n标签分布:")
label_counts = df['标签'].value_counts()
for label, count in label_counts.items():
    print(f"  {label}: {count}条")

print("\n标注员工作量:")
annotator_counts = df['标注员'].value_counts()
for name, count in annotator_counts.items():
    print(f"  {name}: {count}条")

pass_rate = (df['质检状态'] == '通过').sum() / len(df) * 100
print(f"\n质检通过率: {pass_rate:.1f}%")

print("=" * 50)
```

---

**提交要求**:
- 文件名: `学号_Day7.py`
- 代码能运行
- 包含必要注释
