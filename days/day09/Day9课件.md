# 第九章:项目实战(一)

> **实战导向** - 两个完整项目带你入门AI数据处理
> **学习目标**: 综合运用前8章知识,完成真实工作任务
> **课程时长**: 上午3小时(项目1) + 下午3小时(项目2)

---

## 项目1: 客服对话文本清洗工具

### 项目背景
某电商公司需要训练客服AI,有10000条客服对话记录,需要清洗后用于训练。

### 数据问题
- 包含无效字符(表情符号、特殊符号)
- 存在重复对话
- 部分对话为空或过短
- 格式不统一

### 任务要求
1. 去除特殊字符,保留中文、英文、数字
2. 删除重复对话
3. 删除长度<5的无效对话
4. 统一转为小写(英文)
5. 保存为clean_dialogs.csv

### 核心代码
```python
import pandas as pd
import re

# 读取数据
df = pd.read_csv('raw_dialogs.csv')

# 清洗函数
def clean_text(text):
    if pd.isna(text):
        return ''
    # 只保留中英文数字和常用标点
    text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9,。!?、]', '', str(text))
    return text.strip()

# 应用清洗
df['对话'] = df['对话'].apply(clean_text)

# 删除空值和过短文本
df = df[df['对话'].str.len() >= 5]

# 去重
df = df.drop_duplicates(subset=['对话'])

# 保存
df.to_csv('clean_dialogs.csv', index=False, encoding='utf-8-sig')

print(f"清洗完成!原始:{len(df)}条 → 清洗后:{len(df)}条")
```

### 技能点
- 正则表达式文本清洗
- Pandas数据处理
- 函数封装复用

---

## 项目2: 商品图片智能分类器

### 项目背景
电商平台有5000张商品图片,需要分类为:服装/电子/食品/家居四类。

### 数据情况
- 图片已标注(使用Label Studio)
- 需要验证标注质量
- 准备训练数据集

### 任务要求
1. 读取标注数据
2. 检查数据质量(缺失值/异常值)
3. 分析类别分布
4. 划分训练集(80%)和测试集(20%)
5. 生成数据集统计报告

### 核心代码
```python
import pandas as pd
from sklearn.model_selection import train_test_split

# 读取标注数据
df = pd.read_csv('product_labels.csv')

# 数据质量检查
print(f"总样本: {len(df)}")
print(f"缺失值: {df.isnull().sum().sum()}")
print(f"重复值: {df.duplicated().sum()}")

# 清洗
df = df.dropna()
df = df.drop_duplicates()

# 类别分布
print("\n类别分布:")
print(df['类别'].value_counts())

# 划分数据集
train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    stratify=df['类别'],  # 分层抽样,保持类别比例
    random_state=42
)

print(f"\n训练集: {len(train_df)}张")
print(f"测试集: {len(test_df)}张")

# 保存
train_df.to_csv('train.csv', index=False)
test_df.to_csv('test.csv', index=False)
```

### 技能点
- 数据集划分(train_test_split)
- 分层抽样保证数据均衡
- 完整项目流程

---

## 项目总结

### 完成的工作
✅ 文本清洗工具(正则表达式)
✅ 图片分类数据准备(数据集划分)

### 掌握的技能
- 完整项目流程思维
- 数据清洗实战
- 数据集准备
- 质量检查

### 职业应用
这两个项目就是AI训练师的日常工作!

---

📚 **下一章**: 项目实战(二) - CSV处理工具 + 毕业项目
