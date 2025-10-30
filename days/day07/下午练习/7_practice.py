"""
【文件说明】
文件名: 7_practice.py
章节: 第七章 - Pandas数据处理基础
知识点: 综合练习 - CSV读写、数据清洗、数据筛选
难度: ⭐⭐⭐⭐ (综合实战)
预计学习时间: 2-3小时(下午练习时间)

【学习目标】
1. 综合运用CSV读写、数据清洗、数据筛选技能
2. 完成3个真实工作场景的数据处理任务
3. 形成完整的数据处理工作流程思维
4. 为第8-10章的项目实战打基础

【实际应用场景】
本练习模拟AI训练师的3个真实工作任务:
1. 基础任务: 标注数据质检报告生成
2. 进阶任务: 训练集数据准备
3. 挑战任务: 标注团队绩效分析

【前置知识】
- 7_1_pandas_basic.py
- 7_2_pandas_clean.py
- 7_3_pandas_filter.py

【练习说明】
- 每个练习都有完整的需求描述和参考答案
- 建议先自己尝试,再查看答案
- 答案不唯一,关键是思路正确

【学习建议】
1. 先阅读需求,理解要做什么
2. 自己动手写代码,尝试解决
3. 遇到困难查看提示
4. 对照参考答案,学习更优的写法
5. 思考扩展问题,举一反三
"""

import pandas as pd
import numpy as np

# ========== 准备练习数据 ==========

print("=" * 70)
print("准备练习数据集")
print("=" * 70)

# 创建一个包含各种问题的模拟标注数据集
np.random.seed(42)  # 固定随机种子,结果可复现

# 生成100条标注数据
num_samples = 100

data = {
    '文件名': [f'IMG{str(i).zfill(3)}.jpg' if i % 15 != 0 else f'IMG{str(i).zfill(3)}.txt'  # 每15个有1个错误格式
               for i in range(1, num_samples + 1)],

    '标签': np.random.choice(
        ['猫', '狗', '鸟', None, '未知'],  # 包含缺失值和异常标签
        size=num_samples,
        p=[0.35, 0.30, 0.20, 0.10, 0.05]  # 10%缺失,5%异常
    ),

    '标注员': np.random.choice(
        ['张三', '李四', '王五', '赵六', '钱七'],
        size=num_samples
    ),

    '质检状态': np.random.choice(
        ['通过', '未通过', '待质检', None],
        size=num_samples,
        p=[0.60, 0.15, 0.20, 0.05]  # 5%缺失
    ),

    '分数': [np.random.randint(60, 100) if i % 20 != 0 else np.random.randint(-10, 60)  # 每20个有1个异常分数
             for i in range(num_samples)],

    '标注日期': pd.date_range('2024-01-01', periods=num_samples, freq='D').astype(str)
}

df_practice = pd.DataFrame(data)

# 人为添加一些重复数据(模拟重复标注)
df_practice = pd.concat([
    df_practice,
    df_practice.iloc[[5, 10, 15]].copy()  # 复制3条数据
], ignore_index=True)

# 保存为CSV供练习使用
practice_file = 'label_data_practice.csv'
df_practice.to_csv(practice_file, index=False, encoding='utf-8-sig')

print(f"\n✅ 练习数据已准备好: {practice_file}")
print(f"数据规模: {len(df_practice)}行")
print("\n前10行预览:")
print(df_practice.head(10))


# ========================================================================
# 练习1: 基础任务 - 生成标注数据质检报告
# ========================================================================

print("\n" + "=" * 70)
print("练习1: 基础任务 - 生成标注数据质检报告")
print("=" * 70)

print("""
【任务需求】
你是AI训练师,刚收到标注团队导出的数据。需要生成一份质检报告,包含:
1. 数据总体情况(总行数、总列数)
2. 数据质量问题统计:
   - 缺失值数量(按列统计)
   - 重复值数量
   - 异常值数量(文件格式不是.jpg/.png的, 分数<0或>100的)
3. 标签分布统计
4. 质检状态统计
5. 标注员工作量统计

【要求】
- 从CSV文件读取数据
- 使用Pandas统计各项指标
- 格式化输出为报告格式

【参考输出格式】
===== AI标注数据质检报告 =====
数据规模: 100行 x 6列
缺失值:
  标签: 10个
  质检状态: 5个
重复值: 3条
异常值:
  错误文件格式: 7个
  异常分数: 5个
标签分布:
  猫: 35个 (35.0%)
  狗: 30个 (30.0%)
  ...
""")

# 💡 提示:
# - 使用 pd.read_csv() 读取数据
# - 使用 isnull().sum() 统计缺失值
# - 使用 duplicated().sum() 统计重复值
# - 使用 str.endswith() 检查文件格式
# - 使用 value_counts() 统计分布

print("\n" + "-" * 70)
print("【参考答案】")
print("-" * 70)

# 读取数据
df = pd.read_csv(practice_file, encoding='utf-8')

# 开始生成报告
print("\n" + "=" * 70)
print(" " * 20 + "AI标注数据质检报告")
print("=" * 70)

# 1. 数据规模
print(f"\n【数据规模】")
print(f"总行数: {df.shape[0]}行")
print(f"总列数: {df.shape[1]}列")
print(f"列名: {', '.join(df.columns)}")

# 2. 数据质量问题

print(f"\n【数据质量问题】")

# 2.1 缺失值
print("\n缺失值统计:")
missing_counts = df.isnull().sum()
missing_counts = missing_counts[missing_counts > 0]  # 只显示有缺失的列

if len(missing_counts) > 0:
    for col, count in missing_counts.items():
        percentage = count / len(df) * 100
        print(f"  {col}: {count}个 ({percentage:.1f}%)")
else:
    print("  无缺失值 ✅")

# 2.2 重复值
dup_count = df.duplicated().sum()
print(f"\n重复值: {dup_count}条")

if dup_count > 0:
    print("重复数据详情:")
    print(df[df.duplicated(keep=False)].sort_values('文件名'))

# 2.3 异常值
print("\n异常值检测:")

# 文件格式异常
valid_formats = df['文件名'].str.endswith(('.jpg', '.png', '.jpeg'))
invalid_format_count = (~valid_formats).sum()
print(f"  错误文件格式: {invalid_format_count}个")

if invalid_format_count > 0:
    print("  异常文件:")
    invalid_files = df[~valid_formats]['文件名'].tolist()
    print(f"  {', '.join(invalid_files[:5])}" + ("..." if len(invalid_files) > 5 else ""))

# 分数异常
invalid_scores = df[(df['分数'] < 0) | (df['分数'] > 100)]
print(f"  异常分数: {len(invalid_scores)}个")

if len(invalid_scores) > 0:
    print(f"  异常分数范围: {invalid_scores['分数'].min()} ~ {invalid_scores['分数'].max()}")

# 标签异常(不在允许列表的)
allowed_labels = ['猫', '狗', '鸟']
label_with_value = df[df['标签'].notna()]
invalid_labels = label_with_value[~label_with_value['标签'].isin(allowed_labels)]
print(f"  异常标签: {len(invalid_labels)}个")

if len(invalid_labels) > 0:
    print(f"  异常标签值: {invalid_labels['标签'].unique()}")

# 3. 标签分布
print(f"\n【标签分布】")
label_dist = df['标签'].value_counts(dropna=False)  # dropna=False会统计缺失值

for label, count in label_dist.items():
    percentage = count / len(df) * 100
    label_name = "缺失值" if pd.isna(label) else label
    print(f"  {label_name}: {count}个 ({percentage:.1f}%)")

# 4. 质检状态
print(f"\n【质检状态】")
qc_dist = df['质检状态'].value_counts(dropna=False)

for status, count in qc_dist.items():
    percentage = count / len(df) * 100
    status_name = "待分配" if pd.isna(status) else status
    print(f"  {status_name}: {count}个 ({percentage:.1f}%)")

# 5. 标注员工作量
print(f"\n【标注员工作量】")
annotator_work = df['标注员'].value_counts()

for name, count in annotator_work.items():
    percentage = count / len(df) * 100
    print(f"  {name}: {count}个 ({percentage:.1f}%)")

# 6. 数据质量评分
print(f"\n【数据质量评分】")

# 计算质量分: 100分 - 各种问题扣分
quality_score = 100
deductions = []

missing_rate = df.isnull().sum().sum() / (len(df) * len(df.columns)) * 100
if missing_rate > 0:
    deduction = min(missing_rate * 2, 20)  # 最多扣20分
    quality_score -= deduction
    deductions.append(f"缺失值率{missing_rate:.1f}% -> 扣{deduction:.0f}分")

dup_rate = dup_count / len(df) * 100
if dup_rate > 0:
    deduction = min(dup_rate * 2, 15)
    quality_score -= deduction
    deductions.append(f"重复率{dup_rate:.1f}% -> 扣{deduction:.0f}分")

invalid_rate = (invalid_format_count + len(invalid_scores) + len(invalid_labels)) / len(df) * 100
if invalid_rate > 0:
    deduction = min(invalid_rate * 3, 25)
    quality_score -= deduction
    deductions.append(f"异常率{invalid_rate:.1f}% -> 扣{deduction:.0f}分")

print(f"综合质量分: {quality_score:.1f}/100")

if deductions:
    print("扣分明细:")
    for item in deductions:
        print(f"  - {item}")

# 质量评级
if quality_score >= 90:
    grade = "优秀 ⭐⭐⭐"
elif quality_score >= 75:
    grade = "良好 ⭐⭐"
elif quality_score >= 60:
    grade = "及格 ⭐"
else:
    grade = "不及格 ⚠️"

print(f"质量评级: {grade}")

print("\n" + "=" * 70)

# 💡 知识点总结:
print("""
💡 本练习用到的技能:
1. CSV读取: pd.read_csv()
2. 数据统计: shape, isnull().sum(), duplicated().sum()
3. 字符串方法: str.endswith()
4. 条件筛选: 布尔索引
5. 分布统计: value_counts()
6. 格式化输出: f-string, 百分比计算
""")


# ========================================================================
# 练习2: 进阶任务 - 训练集数据准备
# ========================================================================

print("\n" + "=" * 70)
print("练习2: 进阶任务 - 训练集数据准备")
print("=" * 70)

print("""
【任务需求】
项目经理要求你准备一个干净的训练数据集,用于训练图片分类模型。

数据清洗要求:
1. 只保留标签为"猫"、"狗"、"鸟"的数据
2. 删除标签缺失的数据
3. 删除文件格式不是.jpg/.png的数据
4. 删除分数<70的低质量数据
5. 删除重复文件
6. 只保留质检通过的数据

数据均衡要求:
7. 检查三个类别的样本数量是否均衡
8. 如果某个类别样本数<最多类别的70%,给出警告

输出要求:
9. 保存清洗后的数据为: train_dataset.csv (只保存文件名和标签两列)
10. 生成数据清洗报告

【预期结果】
清洗前: 103行
清洗后: 约40-50行
保留率: 约40-50%
""")

print("\n" + "-" * 70)
print("【参考答案】")
print("-" * 70)

# 重新读取原始数据
df_raw = pd.read_csv(practice_file, encoding='utf-8')

print(f"\n原始数据: {len(df_raw)}行")
print(f"原始标签分布:\n{df_raw['标签'].value_counts(dropna=False)}\n")

# 数据清洗流程
df_clean = df_raw.copy()

# 步骤1: 删除标签缺失的数据
df_clean = df_clean.dropna(subset=['标签'])
print(f"步骤1 - 删除标签缺失: {len(df_raw)} -> {len(df_clean)}行 (删除{len(df_raw)-len(df_clean)}行)")

# 步骤2: 只保留有效标签
allowed_labels = ['猫', '狗', '鸟']
df_clean = df_clean[df_clean['标签'].isin(allowed_labels)]
print(f"步骤2 - 只保留有效标签: 剩余{len(df_clean)}行")

# 步骤3: 删除文件格式错误的
df_clean = df_clean[df_clean['文件名'].str.endswith(('.jpg', '.png'))]
print(f"步骤3 - 删除格式错误: 剩余{len(df_clean)}行")

# 步骤4: 删除低分数据
df_clean = df_clean[df_clean['分数'] >= 70]
print(f"步骤4 - 删除分数<70: 剩余{len(df_clean)}行")

# 步骤5: 去除重复
df_clean = df_clean.drop_duplicates(subset=['文件名'])
print(f"步骤5 - 删除重复文件: 剩余{len(df_clean)}行")

# 步骤6: 只保留质检通过
df_clean = df_clean[df_clean['质检状态'] == '通过']
print(f"步骤6 - 只保留质检通过: 剩余{len(df_clean)}行")

# 数据均衡检查
print(f"\n【数据均衡性检查】")
label_counts = df_clean['标签'].value_counts()
print(f"最终标签分布:\n{label_counts}\n")

max_count = label_counts.max()
min_count = label_counts.min()
balance_ratio = min_count / max_count * 100

print(f"均衡度: {balance_ratio:.1f}% (最少类别/最多类别)")

if balance_ratio < 70:
    print(f"⚠️ 警告: 数据不均衡!最少的类别只有最多类别的{balance_ratio:.1f}%")
    print("建议: 考虑欠采样(删除多的)或过采样(复制少的)")
else:
    print("✅ 数据较为均衡")

# 保存清洗后的数据
train_file = 'train_dataset.csv'
df_clean[['文件名', '标签']].to_csv(train_file, index=False, encoding='utf-8-sig')
print(f"\n✅ 训练数据已保存到: {train_file}")

# 生成清洗报告
print(f"\n" + "=" * 70)
print(" " * 20 + "数据清洗报告")
print("=" * 70)

print(f"\n原始数据: {len(df_raw)}行")
print(f"清洗后数据: {len(df_clean)}行")
print(f"删除数据: {len(df_raw) - len(df_clean)}行")
print(f"保留率: {len(df_clean)/len(df_raw)*100:.1f}%")

print(f"\n清洗操作明细:")
print(f"  1. 删除标签缺失: {df_raw['标签'].isnull().sum()}行")
print(f"  2. 删除异常标签: {len(df_raw[df_raw['标签'].notna() & ~df_raw['标签'].isin(allowed_labels)])}行")
print(f"  3. 删除格式错误: {len(df_raw[~df_raw['文件名'].str.endswith(('.jpg', '.png'))])}行")
print(f"  4. 删除低分数据: {len(df_raw[df_raw['分数'] < 70])}行")
print(f"  5. 删除重复数据: {df_raw.duplicated(subset=['文件名']).sum()}行")
print(f"  6. 删除未通过质检: {len(df_raw[df_raw['质检状态'] != '通过'])}行")

print(f"\n最终数据集特征:")
print(f"  - 类别数: {df_clean['标签'].nunique()}个")
print(f"  - 最少样本类别: {label_counts.idxmin()} ({label_counts.min()}个)")
print(f"  - 最多样本类别: {label_counts.idxmax()} ({label_counts.max()}个)")
print(f"  - 平均分数: {df_clean['分数'].mean():.1f}")
print(f"  - 分数范围: {df_clean['分数'].min()} - {df_clean['分数'].max()}")

print("\n" + "=" * 70)

print("""
💡 本练习用到的技能:
1. 数据清洗: dropna(), drop_duplicates()
2. 条件筛选: isin(), 比较运算符, 布尔索引
3. 字符串方法: str.endswith()
4. 数据统计: value_counts(), min(), max(), mean()
5. 数据保存: to_csv()
6. 流程化思维: 按步骤清洗并记录每步结果
""")


# ========================================================================
# 练习3: 挑战任务 - 标注团队绩效分析
# ========================================================================

print("\n" + "=" * 70)
print("练习3: 挑战任务 - 标注团队绩效分析")
print("=" * 70)

print("""
【任务需求】
作为质检负责人,你需要分析标注团队的绩效,为团队管理提供数据支持。

分析要求:
1. 统计每个标注员的工作量(标注总数)
2. 计算每个标注员的质检通过率
3. 计算每个标注员的平均分
4. 找出表现最好的标注员(通过率最高且平均分>85)
5. 找出需要培训的标注员(通过率<60%或平均分<75)
6. 分析每个标注员擅长标注哪个类别(准确率最高的类别)
7. 生成绩效排行榜

【提示】
- 使用 groupby() 分组统计
- 使用 apply() 自定义聚合逻辑
- 使用 sort_values() 排序

【参考输出】
=== 标注团队绩效分析报告 ===
总标注员数: 5人
总标注量: 103条

个人绩效:
张三: 工作量20条, 通过率75%, 平均分85.3, 评级:良好
李四: 工作量22条, 通过率90%, 平均分88.5, 评级:优秀
...

绩效排行榜(按通过率):
1. 李四: 90%
2. 王五: 85%
...

需要培训:
赵六: 通过率55%, 平均分72.3
""")

print("\n" + "-" * 70)
print("【参考答案】")
print("-" * 70)

# 重新读取原始数据
df_perf = pd.read_csv(practice_file, encoding='utf-8')

print("\n" + "=" * 70)
print(" " * 15 + "标注团队绩效分析报告")
print("=" * 70)

# 基本统计
print(f"\n【总体情况】")
print(f"总标注员数: {df_perf['标注员'].nunique()}人")
print(f"总标注量: {len(df_perf)}条")
print(f"质检通过: {len(df_perf[df_perf['质检状态'] == '通过'])}条 ({len(df_perf[df_perf['质检状态'] == '通过'])/len(df_perf)*100:.1f}%)")

# 按标注员分组统计
print(f"\n【个人绩效详情】\n")

# 创建绩效表
perf_table = []

for annotator in df_perf['标注员'].unique():
    # 筛选该标注员的数据
    annotator_data = df_perf[df_perf['标注员'] == annotator]

    # 统计工作量
    total_count = len(annotator_data)

    # 计算通过率
    passed_count = len(annotator_data[annotator_data['质检状态'] == '通过'])
    pass_rate = passed_count / total_count * 100 if total_count > 0 else 0

    # 计算平均分
    avg_score = annotator_data['分数'].mean()

    # 评级
    if pass_rate >= 80 and avg_score >= 85:
        grade = "优秀 ⭐⭐⭐"
    elif pass_rate >= 60 and avg_score >= 75:
        grade = "良好 ⭐⭐"
    elif pass_rate >= 50 and avg_score >= 65:
        grade = "及格 ⭐"
    else:
        grade = "待提升 ⚠️"

    # 擅长类别(标注最多的类别)
    label_counts = annotator_data['标签'].value_counts()
    best_label = label_counts.idxmax() if len(label_counts) > 0 else "无"

    perf_table.append({
        '标注员': annotator,
        '工作量': total_count,
        '通过数': passed_count,
        '通过率': pass_rate,
        '平均分': avg_score,
        '评级': grade,
        '主要类别': best_label
    })

    print(f"{annotator}:")
    print(f"  工作量: {total_count}条")
    print(f"  通过率: {pass_rate:.1f}% ({passed_count}/{total_count})")
    print(f"  平均分: {avg_score:.1f}")
    print(f"  评级: {grade}")
    print(f"  主要标注: {best_label} ({label_counts.max()}条)")
    print()

# 转为DataFrame方便排序
perf_df = pd.DataFrame(perf_table)

# 绩效排行榜
print("【绩效排行榜】")

print("\n按通过率排序:")
perf_sorted = perf_df.sort_values('通过率', ascending=False)
for i, row in perf_sorted.head().iterrows():
    print(f"  {row['标注员']}: {row['通过率']:.1f}% (平均分{row['平均分']:.1f})")

print("\n按平均分排序:")
perf_sorted = perf_df.sort_values('平均分', ascending=False)
for i, row in perf_sorted.head().iterrows():
    print(f"  {row['标注员']}: {row['平均分']:.1f}分 (通过率{row['通过率']:.1f}%)")

print("\n按工作量排序:")
perf_sorted = perf_df.sort_values('工作量', ascending=False)
for i, row in perf_sorted.head().iterrows():
    print(f"  {row['标注员']}: {row['工作量']}条")

# 表现优秀的标注员
print("\n【表现优秀】")
excellent = perf_df[(perf_df['通过率'] >= 80) & (perf_df['平均分'] >= 85)]

if len(excellent) > 0:
    print("以下标注员表现优秀,建议奖励:")
    for _, row in excellent.iterrows():
        print(f"  {row['标注员']}: 通过率{row['通过率']:.1f}%, 平均分{row['平均分']:.1f}")
else:
    print("暂无达到优秀标准的标注员")

# 需要培训的标注员
print("\n【需要培训】")
need_training = perf_df[(perf_df['通过率'] < 60) | (perf_df['平均分'] < 75)]

if len(need_training) > 0:
    print("以下标注员需要加强培训:")
    for _, row in need_training.iterrows():
        reasons = []
        if row['通过率'] < 60:
            reasons.append(f"通过率低({row['通过率']:.1f}%)")
        if row['平均分'] < 75:
            reasons.append(f"分数低({row['平均分']:.1f})")

        print(f"  {row['标注员']}: {', '.join(reasons)}")
else:
    print("全员表现达标 ✅")

# 工作量分析
print("\n【工作量分析】")
max_work = perf_df['工作量'].max()
min_work = perf_df['工作量'].min()
avg_work = perf_df['工作量'].mean()

print(f"平均工作量: {avg_work:.1f}条")
print(f"最多: {perf_df[perf_df['工作量'] == max_work]['标注员'].values[0]} ({max_work}条)")
print(f"最少: {perf_df[perf_df['工作量'] == min_work]['标注员'].values[0]} ({min_work}条)")

if max_work > avg_work * 1.5:
    print("⚠️ 工作量分配不均,建议调整任务分配")

# 保存绩效报告
perf_report_file = 'performance_report.csv'
perf_df.to_csv(perf_report_file, index=False, encoding='utf-8-sig')
print(f"\n✅ 绩效报告已保存到: {perf_report_file}")

print("\n" + "=" * 70)

print("""
💡 本练习用到的技能:
1. 分组统计: 循环处理每个标注员的数据
2. 条件筛选: 复杂的多条件判断
3. 统计计算: 通过率、平均值计算
4. 排序: sort_values()
5. DataFrame创建: 将统计结果转为表格
6. 综合分析: 结合多个指标进行评价

🎯 扩展思考:
1. 如果用groupby()能否简化代码?
2. 如何可视化这些绩效数据?(提示:matplotlib)
3. 如何设计更科学的绩效评分公式?
4. 如何发现标注员的"专长"和"短板"?
""")


# ========== 总结 ==========

print("\n" + "=" * 70)
print("第七章练习总结")
print("=" * 70)

print("""
恭喜你完成第七章的所有练习!🎉

✅ 你已经掌握的技能:
1. CSV文件读写
2. 数据质量检查(缺失值、重复值、异常值)
3. 数据清洗三板斧
4. 数据筛选与过滤
5. 统计分析与报告生成
6. 完整的数据处理工作流程

🎯 这些技能在AI训练师工作中的应用:
- 标注数据质检: 发现并处理脏数据
- 训练集准备: 清洗数据并确保质量
- 绩效分析: 统计分析团队表现
- 数据统计: 生成各类数据报告

📚 下一步学习:
- 第八章: AI标注实战 (Label Studio使用)
- 第九章: 项目实战(一) - 文本清洗+图片分类
- 第十章: 项目实战(二) - CSV处理+毕业项目

💡 学习建议:
1. 多动手练习,熟能生巧
2. 理解每个函数的用途,不要死记硬背
3. 尝试用不同方法解决同一个问题
4. 将代码封装成函数,提高复用性
5. 关注实际工作场景,学以致用

继续加油!💪
""")
