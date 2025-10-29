"""
【文件说明】
文件名: 7_1_pandas_basic.py
章节: 第七章 - Pandas数据处理基础
知识点: CSV读写、数据查看基础操作
难度: ⭐⭐ (基础)
预计学习时间: 40分钟

【学习目标】
1. 掌握Pandas的安装与导入
2. 学会CSV文件的读取和保存
3. 熟悉数据查看的常用方法(head/tail/info/describe)
4. 理解DataFrame的基本结构

【实际应用场景】
- AI训练: 读取标注团队导出的CSV数据
- 数据分析: 查看数据集的基本信息和统计特征
- 数据导出: 将处理后的数据保存为CSV供模型训练使用

【前置知识】
- Python基础语法(变量、输出)
- 文件路径概念

【注意事项】
⚠️ 如果运行报错"No module named 'pandas'",需要先安装: pip install pandas
⚠️ 读取中文CSV时,注意encoding参数,常用utf-8或gbk
⚠️ 保存CSV时建议加上index=False,否则会多一列行号

【工作流程对照】
这个文件模拟的是AI训练师工作的第一步:
1. 从标注平台导出原始数据(CSV格式)
2. 读取数据进行初步检查
3. 查看数据质量和分布情况
4. 为后续的数据清洗做准备
"""

# ========== 导入必需的库 ==========
import pandas as pd  # pd是Pandas的标准别名,业界通用
import numpy as np   # 通常配合使用,处理数值计算

# 📌 实战技巧: 为什么用别名pd?
# 1. 代码更简洁: pd.read_csv() vs pandas.read_csv()
# 2. 行业标准: 所有Pandas教程和文档都用pd
# 3. 避免冲突: 如果有同名函数,可以明确来源


# ========== 第一部分: CSV文件读取 ==========

print("=" * 50)
print("第一部分: CSV文件读取")
print("=" * 50)

# 🎯 场景: 读取AI标注团队导出的数据
# 假设有一个CSV文件包含图片标注信息

# 方法1: 最简单的读取(文件在当前目录)
# df = pd.read_csv('label_data.csv')

# 方法2: 指定编码读取(推荐,支持中文)
# df = pd.read_csv('label_data.csv', encoding='utf-8')

# 📌 因为我们没有真实文件,这里创建一个示例DataFrame
# 实际工作中,你会直接read_csv真实文件
data = {
    '文件名': ['IMG001.jpg', 'IMG002.jpg', 'IMG003.jpg', 'IMG004.jpg', 'IMG005.jpg',
             'IMG006.jpg', 'IMG007.jpg', 'IMG008.jpg', 'IMG009.jpg', 'IMG010.jpg'],
    '标签': ['猫', '狗', '猫', '鸟', '狗', '猫', None, '狗', '鸟', '猫'],  # None表示缺失值
    '标注员': ['张三', '李四', '张三', '王五', '李四', '张三', '王五', '李四', '张三', '王五'],
    '质检状态': ['通过', '通过', '通过', '待质检', '通过', '未通过', '待质检', '通过', '通过', '待质检'],
    '标注时间': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03',
              '2024-01-03', '2024-01-04', '2024-01-04', '2024-01-05', '2024-01-05']
}

df = pd.DataFrame(data)  # 创建DataFrame对象

# 💡 知识点: DataFrame是什么?
# DataFrame是Pandas的核心数据结构,可以理解为:
# - Excel表格的Python版本
# - 有行有列的二维表格
# - 每列可以是不同数据类型(数字、文本、日期等)

print("\n✅ 数据读取成功!")


# ========== 第二部分: 快速查看数据 ==========

print("\n" + "=" * 50)
print("第二部分: 快速查看数据")
print("=" * 50)

# 2.1 查看前几行(默认5行)
print("\n【df.head() - 查看前5行】")
print(df.head())

# 📌 实战技巧: head()用来快速预览数据
# - 读取大文件后,先用head()看看数据长什么样
# - 确认列名是否正确
# - 检查数据格式是否符合预期

print("\n【df.head(3) - 查看前3行】")
print(df.head(3))

# 2.2 查看后几行
print("\n【df.tail() - 查看后5行】")
print(df.tail())

# 📌 实战技巧: tail()用来检查数据末尾
# - 有些数据文件末尾可能有统计汇总行
# - 检查数据是否完整读取


# ========== 第三部分: 查看数据基本信息 ==========

print("\n" + "=" * 50)
print("第三部分: 查看数据基本信息")
print("=" * 50)

# 3.1 查看数据维度(多少行多少列)
print("\n【df.shape - 数据形状】")
print(f"数据维度: {df.shape}")  # 输出: (10, 5) 表示10行5列
print(f"行数: {df.shape[0]}, 列数: {df.shape[1]}")

# 💡 知识点: shape返回元组(行数, 列数)
# - shape[0] 是行数(样本数量)
# - shape[1] 是列数(特征数量)

# 3.2 查看列名
print("\n【df.columns - 列名列表】")
print(df.columns)
print(f"列名个数: {len(df.columns)}")

# 3.3 查看数据类型
print("\n【df.dtypes - 每列的数据类型】")
print(df.dtypes)

# 📌 常见数据类型:
# - object: 文本类型(字符串)
# - int64: 整数
# - float64: 浮点数(小数)
# - datetime64: 日期时间

# 3.4 查看详细信息(最重要!)
print("\n【df.info() - 详细信息汇总】")
df.info()

# 💡 知识点: info()会显示:
# - 数据集大小(行数)
# - 每列的名称
# - 每列的非空值数量(Non-Null Count) ⚠️ 重点关注这个!
# - 每列的数据类型
# - 内存占用

# ⚠️ 常见错误: 忽略Non-Null Count
# 如果某列有10行数据,但Non-Null只有8个,说明有2个缺失值!
# 例如上面的'标签'列有1个None


# ========== 第四部分: 数据统计 ==========

print("\n" + "=" * 50)
print("第四部分: 数据统计")
print("=" * 50)

# 4.1 描述性统计(数值型列)
print("\n【df.describe() - 数值列统计】")
print(df.describe())

# 📌 因为我们的数据都是文本,所以describe()显示不多
# 如果有数值列(如分数、年龄),会显示平均值、最小值、最大值等

# 4.2 查看所有列的统计(包括文本列)
print("\n【df.describe(include='all') - 所有列统计】")
print(df.describe(include='all'))

# 💡 知识点: 文本列的统计指标
# - count: 非空值数量
# - unique: 不同值的数量
# - top: 出现最多的值
# - freq: 最多值出现的次数

# 4.3 单列统计 - 最常用!
print("\n【df['标签'].value_counts() - 统计每个标签出现次数】")
print(df['标签'].value_counts())

# 📌 实战技巧: value_counts()是数据分析必备技能
# 用途:
# - 统计每个类别的样本数量
# - 检查数据是否均衡(如猫300张,狗50张,不均衡!)
# - 发现异常值(如突然出现一个"未知"类别)

print("\n【df['标注员'].value_counts() - 统计每个标注员的工作量】")
print(df['标注员'].value_counts())

print("\n【df['质检状态'].value_counts() - 统计质检情况】")
print(df['质检状态'].value_counts())


# ========== 第五部分: 缺失值检查 ==========

print("\n" + "=" * 50)
print("第五部分: 缺失值检查(重要!)")
print("=" * 50)

# 5.1 检查每个位置是否缺失
print("\n【df.isnull() - 返回True/False矩阵】")
print(df.isnull())

# 💡 知识点: isnull()逐个检查
# - True表示该位置是缺失值(NaN/None)
# - False表示有值

# 5.2 统计每列的缺失数量(最常用!)
print("\n【df.isnull().sum() - 统计每列缺失值数量】")
print(df.isnull().sum())

# 📌 实战技巧: 这是数据质检第一步!
# 工作流程:
# 1. 读取数据后,立即检查缺失值
# 2. 缺失值多的列可能需要删除或特殊处理
# 3. 关键列(如标签)不能有缺失

# 5.3 统计总共有多少个缺失值
total_missing = df.isnull().sum().sum()
print(f"\n总缺失值数量: {total_missing}个")

# 5.4 统计缺失值百分比
print("\n【缺失值百分比】")
missing_percent = (df.isnull().sum() / len(df)) * 100
print(missing_percent)

# ⚠️ 常见错误: 忽略缺失值会导致:
# - 训练模型时报错
# - 统计结果不准确
# - 数据处理出现异常


# ========== 第六部分: 保存CSV文件 ==========

print("\n" + "=" * 50)
print("第六部分: 保存CSV文件")
print("=" * 50)

# 6.1 基础保存
# df.to_csv('output.csv')  # ⚠️ 会多一列行号!

# 6.2 正确保存(推荐)
output_file = 'output_label_data.csv'
df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"\n✅ 数据已保存到: {output_file}")

# 📌 实战技巧: 保存CSV的最佳实践
# 1. index=False  - 不保存行号(否则会多一列Unnamed: 0)
# 2. encoding='utf-8-sig' - 保证Excel能正常显示中文
#    - utf-8: 标准编码,但Excel可能显示乱码
#    - utf-8-sig: 带BOM头,Excel能识别
#    - gbk: 老式编码,不推荐

# 6.3 只保存部分列
print("\n【只保存文件名和标签两列】")
df[['文件名', '标签']].to_csv('simple_output.csv', index=False, encoding='utf-8-sig')
print("✅ 已保存简化版数据到: simple_output.csv")

# 💡 知识点: 为什么只保存部分列?
# - 训练模型时,通常只需要文件名和标签
# - 减小文件大小
# - 保护隐私(不导出标注员信息)


# ========== 第七部分: 实战案例 - AI数据质检报告 ==========

print("\n" + "=" * 50)
print("第七部分: 实战案例 - 生成数据质检报告")
print("=" * 50)

print("\n" + "=" * 50)
print("  AI标注数据质检报告")
print("=" * 50)

print(f"\n【数据规模】")
print(f"总样本数: {len(df)}条")
print(f"总字段数: {len(df.columns)}个")

print(f"\n【数据质量】")
print(f"缺失标注: {df['标签'].isnull().sum()}个 ({df['标签'].isnull().sum()/len(df)*100:.1f}%)")
print(f"重复样本: {df.duplicated().sum()}个")

print(f"\n【标签分布】")
label_dist = df['标签'].value_counts()
for label, count in label_dist.items():
    percentage = count / len(df) * 100
    print(f"{label}: {count}个 ({percentage:.1f}%)")

print(f"\n【标注员工作量】")
annotator_work = df['标注员'].value_counts()
for name, count in annotator_work.items():
    print(f"{name}: {count}个")

print(f"\n【质检情况】")
qc_status = df['质检状态'].value_counts()
for status, count in qc_status.items():
    percentage = count / len(df) * 100
    print(f"{status}: {count}个 ({percentage:.1f}%)")

# 💡 扩展思考: 如何改进这个质检报告?
# 1. 可以导出为HTML格式,更美观
# 2. 可以添加图表(使用matplotlib)
# 3. 可以计算质检通过率
# 4. 可以按标注员分组,看谁的通过率最高


# ========== 总结与下一步 ==========

print("\n" + "=" * 50)
print("总结")
print("=" * 50)

print("""
✅ 本文件学到的核心技能:
1. Pandas的导入: import pandas as pd
2. CSV读取: pd.read_csv(file, encoding='utf-8')
3. 数据查看: head() tail() info() describe()
4. 缺失值检查: isnull().sum()
5. 单列统计: value_counts()
6. CSV保存: to_csv(file, index=False, encoding='utf-8-sig')

🎯 实战应用:
- 读取标注平台导出的CSV数据
- 快速检查数据质量
- 生成数据质检报告
- 为数据清洗做准备

📚 下一步学习:
- 7_2_pandas_clean.py: 学习数据清洗三板斧
- 7_3_pandas_filter.py: 学习数据筛选与过滤
""")

# ⚠️ 常见错误总结:
print("\n⚠️ 新手常见错误:")
print("1. 忘记安装Pandas: pip install pandas")
print("2. 读取中文CSV乱码: 没加encoding='utf-8'")
print("3. 保存时多一列行号: 没加index=False")
print("4. 忽略缺失值检查: 直接处理数据导致报错")
print("5. 混淆head()和head(n): 前者默认5行,后者指定n行")
