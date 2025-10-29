# 第七章:Pandas数据处理基础

> **AI大模型版** - 为AI训练师打造的Pandas实战课程
> **学习目标**: 掌握数据清洗核心技能,为AI训练数据准备工作打基础
> **课程时长**: 3小时(上午讲课+演示) + 3小时(下午练习)
> **实战案例**: AI训练数据预处理完整流程

---

## 本章学习路线图

```
数据读取 → 数据探索 → 数据清洗 → 数据筛选 → 数据保存
   ↓          ↓          ↓          ↓          ↓
CSV读写   查看结构    三板斧处理   条件筛选    结果导出
```

**为什么AI训练师必须学Pandas?**
- 90%的AI训练数据都是表格格式(CSV/Excel)
- 数据清洗是模型训练前的必经步骤
- 质检工作需要批量处理标注数据
- 数据统计和分析能力是晋升关键

---

## 7.1 Pandas环境准备

### 7.1.1 安装Pandas

```bash
# 方法1:使用pip安装(推荐)
pip install pandas

# 方法2:安装数据分析全家桶
pip install pandas numpy openpyxl

# 验证安装
python -c "import pandas as pd; print(pd.__version__)"
```

**版本选择建议**:
- Pandas >= 1.3.0 (推荐2.0+,性能更好)
- Python >= 3.8

### 7.1.2 导入Pandas

```python
import pandas as pd  # pd是约定俗成的别名

# 常用的配套库
import numpy as np   # 数值计算
```

**⚠️ 注意事项**:
- 必须使用`import pandas as pd`,这是行业标准
- 如果报错`No module named 'pandas'`,说明没安装成功

---

## 7.2 CSV文件读写

### 7.2.1 读取CSV文件

**基础读取**:
```python
# 读取CSV文件
df = pd.read_csv('data.csv')

# 查看前5行
print(df.head())

# 查看基本信息
print(df.info())
```

**常用参数**:
```python
# 指定编码(处理中文)
df = pd.read_csv('data.csv', encoding='utf-8')

# 指定分隔符(有些CSV用分号)
df = pd.read_csv('data.csv', sep=';')

# 跳过前N行
df = pd.read_csv('data.csv', skiprows=2)

# 只读取指定列
df = pd.read_csv('data.csv', usecols=['姓名', '年龄'])

# 处理缺失值
df = pd.read_csv('data.csv', na_values=['NA', '空', '未知'])
```

**🎯 实战场景**:
```python
# AI训练数据读取示例
# 假设标注团队导出的CSV格式为:文件名,标签,标注员,质检状态
df = pd.read_csv(
    'label_data.csv',
    encoding='utf-8',           # 支持中文标签
    na_values=['未标注', ''],   # 处理空标注
    parse_dates=['标注时间']    # 自动解析时间
)
```

### 7.2.2 保存CSV文件

```python
# 基础保存
df.to_csv('output.csv', index=False)  # index=False不保存行号

# 指定编码(推荐utf-8-sig,Excel能正常显示中文)
df.to_csv('output.csv', index=False, encoding='utf-8-sig')

# 只保存部分列
df[['文件名', '标签']].to_csv('output.csv', index=False)

# 追加模式(不覆盖原文件)
df.to_csv('output.csv', mode='a', header=False, index=False)
```

**💡 最佳实践**:
```python
# AI训练数据导出标准格式
df.to_csv(
    f'clean_data_{pd.Timestamp.now().strftime("%Y%m%d")}.csv',  # 文件名带日期
    index=False,
    encoding='utf-8-sig',  # Excel兼容
    float_format='%.2f'    # 浮点数保留2位小数
)
```

---

## 7.3 数据探索与查看

### 7.3.1 查看数据结构

```python
# 查看前5行
df.head()

# 查看后5行
df.tail()

# 查看指定行数
df.head(10)

# 查看数据维度(行数,列数)
df.shape  # 输出: (1000, 5) 表示1000行5列

# 查看列名
df.columns

# 查看数据类型
df.dtypes

# 查看详细信息
df.info()
```

**输出示例**:
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   文件名    1000 non-null   object
 1   标签     950 non-null    object  # ⚠️ 有50个缺失值
 2   标注员    1000 non-null   object
 3   质检状态   800 non-null    object  # ⚠️ 有200个缺失值
 4   标注时间   1000 non-null   object
```

### 7.3.2 数据统计

```python
# 数值型数据统计
df.describe()

# 所有列统计(包括文本列)
df.describe(include='all')

# 单列统计
df['标签'].value_counts()  # 统计每个标签出现次数

# 缺失值统计
df.isnull().sum()

# 重复值统计
df.duplicated().sum()
```

**🎯 实战:快速质检标注数据**
```python
print("=== 标注数据质检报告 ===")
print(f"总样本数: {len(df)}")
print(f"缺失标注: {df['标签'].isnull().sum()}个")
print(f"重复样本: {df.duplicated().sum()}个")
print("\n标签分布:")
print(df['标签'].value_counts())
print("\n标注员工作量:")
print(df['标注员'].value_counts())
```

---

## 7.4 数据清洗三板斧

### 7.4.1 第一板斧:处理缺失值

**检测缺失值**:
```python
# 查看哪些地方有缺失
df.isnull()  # True表示缺失

# 统计每列缺失数量
df.isnull().sum()

# 可视化缺失(用*标记)
df.isnull().sum().plot(kind='bar')
```

**处理方法**:

**方法1:删除缺失值**
```python
# 删除任何列有缺失的行
df_clean = df.dropna()

# 删除特定列有缺失的行
df_clean = df.dropna(subset=['标签'])

# 删除全部为空的行
df_clean = df.dropna(how='all')
```

**方法2:填充缺失值**
```python
# 用固定值填充
df['标签'].fillna('未分类', inplace=True)

# 用前一个值填充
df['质检状态'].fillna(method='ffill', inplace=True)

# 用平均值填充(数值型)
df['分数'].fillna(df['分数'].mean(), inplace=True)
```

**🎯 实战:AI标注数据清洗**
```python
# 策略:标签缺失的删除,质检状态缺失的填充为"待质检"
df_clean = df.dropna(subset=['标签'])  # 标签必须有
df_clean['质检状态'].fillna('待质检', inplace=True)
```

### 7.4.2 第二板斧:处理异常值

**检测异常值**:
```python
# 数值型异常(如年龄不可能是-1或200)
df[(df['年龄'] < 0) | (df['年龄'] > 150)]

# 文本型异常(如标签不在允许范围内)
allowed_labels = ['猫', '狗', '鸟']
df[~df['标签'].isin(allowed_labels)]
```

**处理方法**:

**方法1:删除异常值**
```python
# 删除年龄异常的行
df_clean = df[(df['年龄'] >= 0) & (df['年龄'] <= 150)]
```

**方法2:替换异常值**
```python
# 将异常标签替换为"其他"
df.loc[~df['标签'].isin(allowed_labels), '标签'] = '其他'

# 将负数替换为绝对值
df.loc[df['分数'] < 0, '分数'] = df['分数'].abs()
```

**🎯 实战:清洗AI图片分类数据**
```python
# 允许的图片格式
valid_ext = ['.jpg', '.jpeg', '.png', '.bmp']

# 检查文件扩展名
df['扩展名'] = df['文件名'].str.lower().str[-4:]
invalid = df[~df['扩展名'].isin(valid_ext)]

print(f"发现{len(invalid)}个无效文件格式")
df_clean = df[df['扩展名'].isin(valid_ext)]
```

### 7.4.3 第三板斧:处理重复值

**检测重复**:
```python
# 检测完全重复的行
df.duplicated()

# 统计重复数量
df.duplicated().sum()

# 查看重复的行
df[df.duplicated(keep=False)]

# 基于特定列检测重复
df.duplicated(subset=['文件名'])
```

**处理重复**:
```python
# 删除完全重复的行(保留第一次出现)
df_clean = df.drop_duplicates()

# 基于文件名去重
df_clean = df.drop_duplicates(subset=['文件名'])

# 保留最后一次出现
df_clean = df.drop_duplicates(subset=['文件名'], keep='last')
```

**🎯 实战:去除重复标注**
```python
# 策略:同一文件如果被多次标注,保留最新的
df_clean = df.sort_values('标注时间')  # 按时间排序
df_clean = df_clean.drop_duplicates(subset=['文件名'], keep='last')

print(f"去重前:{len(df)}条,去重后:{len(df_clean)}条")
```

---

## 7.5 数据筛选与过滤

### 7.5.1 条件筛选

**单条件**:
```python
# 筛选猫的图片
cats = df[df['标签'] == '猫']

# 筛选分数大于80的
high_score = df[df['分数'] > 80]

# 筛选特定标注员的数据
zhang_data = df[df['标注员'] == '张三']
```

**多条件(与)**:
```python
# 筛选猫且分数>80的
result = df[(df['标签'] == '猫') & (df['分数'] > 80)]
```

**多条件(或)**:
```python
# 筛选猫或狗的图片
result = df[(df['标签'] == '猫') | (df['标签'] == '狗')]
```

**🎯 实战:筛选待质检数据**
```python
# 筛选已标注但未质检的数据
to_review = df[
    (df['标签'].notnull()) &              # 有标签
    (df['质检状态'] == '待质检')           # 未质检
]
```

### 7.5.2 字符串筛选

```python
# 包含某个关键词
df[df['文件名'].str.contains('cat')]

# 以某个前缀开头
df[df['文件名'].str.startswith('IMG')]

# 以某个后缀结尾
df[df['文件名'].str.endswith('.jpg')]

# 正则匹配
df[df['文件名'].str.match(r'\d{8}\.jpg')]  # 匹配8位数字.jpg
```

### 7.5.3 isin()多值匹配

```python
# 筛选多个标签
animals = ['猫', '狗', '鸟']
df[df['标签'].isin(animals)]

# 筛选多个标注员
team_a = ['张三', '李四', '王五']
df[df['标注员'].isin(team_a)]
```

---

## 7.6 综合实战:AI训练数据预处理

### 案例:图片分类数据集清洗

**场景描述**:
- 你是AI训练师,收到一批图片分类标注数据
- 数据格式:CSV文件,包含文件名、标签、标注员、质检状态
- 任务:清洗数据,导出符合训练要求的数据集

**完整代码**:
```python
import pandas as pd

# ========== 1. 读取数据 ==========
df = pd.read_csv('raw_label_data.csv', encoding='utf-8')
print(f"原始数据:{df.shape[0]}条")

# ========== 2. 数据探索 ==========
print("\n=== 数据质量检查 ===")
print(f"缺失标签:{df['标签'].isnull().sum()}个")
print(f"重复文件:{df.duplicated(subset=['文件名']).sum()}个")
print("\n标签分布:")
print(df['标签'].value_counts())

# ========== 3. 数据清洗 ==========
# 3.1 删除标签缺失的行
df_clean = df.dropna(subset=['标签'])

# 3.2 删除重复文件(保留最新标注)
df_clean = df_clean.sort_values('标注时间', ascending=False)
df_clean = df_clean.drop_duplicates(subset=['文件名'], keep='first')

# 3.3 只保留有效标签
valid_labels = ['猫', '狗', '鸟']
df_clean = df_clean[df_clean['标签'].isin(valid_labels)]

# 3.4 只保留已质检通过的
df_clean = df_clean[df_clean['质检状态'] == '通过']

# ========== 4. 数据验证 ==========
print(f"\n清洗后数据:{df_clean.shape[0]}条")
print("最终标签分布:")
print(df_clean['标签'].value_counts())

# ========== 5. 导出结果 ==========
# 只保存训练需要的列
df_clean[['文件名', '标签']].to_csv(
    'train_data_clean.csv',
    index=False,
    encoding='utf-8-sig'
)

print("\n✅ 数据清洗完成!已保存到train_data_clean.csv")
```

**预期输出**:
```
原始数据:1000条

=== 数据质量检查 ===
缺失标签:50个
重复文件:80个

标签分布:
猫     350
狗     320
鸟     180
其他    100

清洗后数据:720条
最终标签分布:
猫     300
狗     280
鸟     140

✅ 数据清洗完成!已保存到train_data_clean.csv
```

---

## 7.7 作业与练习

### 基础练习

**练习1:读取与探索**
```python
# 1. 读取data/students.csv
# 2. 查看数据的形状、列名、数据类型
# 3. 统计每列的缺失值数量
```

**练习2:数据清洗**
```python
# 基于students.csv:
# 1. 删除年龄列有缺失的行
# 2. 将成绩列的缺失值填充为平均分
# 3. 删除完全重复的行
# 4. 保存清洗后的数据
```

### 进阶练习

**练习3:AI数据质检**
```python
# 基于data/label_results.csv:
# 1. 统计每个标注员的工作量(标注数量)
# 2. 找出标注数量最多的前3名标注员
# 3. 统计每个标签的质检通过率
# 4. 筛选出质检未通过的数据,单独保存
```

**练习4:综合应用**
```python
# 基于data/image_annotations.csv:
# 任务:准备一个干净的训练数据集
# 要求:
# 1. 只保留.jpg和.png格式的图片
# 2. 删除标签为空的数据
# 3. 去除重复文件(保留最新标注)
# 4. 只保留质检通过的数据
# 5. 确保每个类别至少有100个样本
# 6. 导出文件名和标签两列,保存为train_dataset.csv
```

---

## 7.8 常见问题与解决

### Q1: 读取CSV时中文乱码

**问题**:
```python
df = pd.read_csv('data.csv')
# 中文显示为乱码
```

**解决**:
```python
# 尝试不同编码
df = pd.read_csv('data.csv', encoding='utf-8')
df = pd.read_csv('data.csv', encoding='gbk')
df = pd.read_csv('data.csv', encoding='gb18030')
```

### Q2: SettingWithCopyWarning警告

**问题**:
```python
df[df['年龄'] > 18]['成绩'] = 100  # ⚠️ 警告
```

**解决**:
```python
# 使用.loc[]
df.loc[df['年龄'] > 18, '成绩'] = 100
```

### Q3: inplace=True是什么意思?

**区别**:
```python
# 不使用inplace:返回新DataFrame,原数据不变
df_new = df.dropna()

# 使用inplace:直接修改原DataFrame,不返回值
df.dropna(inplace=True)
```

**建议**: 初学者不使用inplace,明确看到新旧数据的变化

### Q4: 如何保存时不要行号?

```python
# 错误:保存时会多一列Unnamed: 0
df.to_csv('output.csv')

# 正确:加上index=False
df.to_csv('output.csv', index=False)
```

---

## 7.9 本章小结

### 核心知识点

✅ **Pandas环境安装与导入**
- `pip install pandas`
- `import pandas as pd`

✅ **CSV读写**
- 读取:`pd.read_csv(file, encoding='utf-8')`
- 保存:`df.to_csv(file, index=False, encoding='utf-8-sig')`

✅ **数据探索**
- 查看:`head()` `tail()` `info()` `describe()`
- 统计:`shape` `columns` `dtypes` `value_counts()`

✅ **数据清洗三板斧**
- 缺失值:`isnull()` `dropna()` `fillna()`
- 异常值:条件筛选 + 替换/删除
- 重复值:`duplicated()` `drop_duplicates()`

✅ **数据筛选**
- 单条件:`df[df['列'] == 值]`
- 多条件:`df[(条件1) & (条件2)]`
- 字符串:`str.contains()` `str.startswith()`
- 多值匹配:`isin([值1, 值2])`

### 与AI训练师工作的关系

| 工作环节 | 用到的Pandas技能 |
|---------|-----------------|
| 标注数据质检 | 缺失值检测、重复值检测 |
| 数据格式转换 | CSV读写、列筛选 |
| 数据统计分析 | value_counts()、describe() |
| 训练集准备 | 条件筛选、数据清洗 |
| 质检报告生成 | 分组统计、数据导出 |

### 下一步学习

- **第八章**:AI标注实战(Label Studio使用)
- **第九章**:项目实战(文本清洗+图片分类)
- **第十章**:毕业项目(综合数据处理工具)

---

## 附录:Pandas速查表

### 读取数据
```python
pd.read_csv(file)           # 读取CSV
pd.read_excel(file)         # 读取Excel
```

### 查看数据
```python
df.head(n)                  # 查看前n行
df.tail(n)                  # 查看后n行
df.shape                    # 行列数
df.columns                  # 列名
df.info()                   # 详细信息
df.describe()               # 统计摘要
```

### 缺失值
```python
df.isnull()                 # 检测缺失
df.dropna()                 # 删除缺失
df.fillna(value)            # 填充缺失
```

### 重复值
```python
df.duplicated()             # 检测重复
df.drop_duplicates()        # 删除重复
```

### 筛选
```python
df[df['列'] == 值]          # 单条件
df[(条件1) & (条件2)]       # 多条件(与)
df[(条件1) | (条件2)]       # 多条件(或)
df['列'].isin([值1, 值2])   # 多值匹配
```

### 保存数据
```python
df.to_csv(file, index=False)           # 保存CSV
df.to_excel(file, index=False)         # 保存Excel
```

---

**课程结束!** 🎉

下一章我们将学习如何使用Label Studio进行AI数据标注实战!
