"""
【文件说明】
文件名: 7_3_pandas_filter.py
章节: 第七章 - Pandas数据处理基础
知识点: 数据筛选与过滤(条件筛选、字符串筛选、isin多值匹配)
难度: ⭐⭐⭐ (进阶)
预计学习时间: 45分钟

【学习目标】
1. 掌握单条件和多条件筛选
2. 学会字符串方法筛选(contains/startswith/endswith)
3. 熟练使用isin()进行多值匹配
4. 理解布尔索引的原理

【实际应用场景】
- AI训练: 按标签筛选特定类别的数据
- 质检工作: 筛选待质检或未通过的数据
- 数据统计: 按标注员筛选工作量
- 数据分配: 筛选特定条件的数据分配给不同模型

【前置知识】
- 7_1_pandas_basic.py(基础读写)
- 7_2_pandas_clean.py(数据清洗)
- 逻辑运算符(&、|、~)

【注意事项】
⚠️ 多条件筛选必须用&(与)、|(或),不能用and、or
⚠️ 每个条件必须用括号括起来,否则会报错
⚠️ 空值筛选要用notna()或isnull(),不能用== None

【工作流程对照】
AI训练师日常工作中的数据筛选场景:
1. 筛选某个标签的所有数据(训练集准备)
2. 筛选待质检的数据(质检任务分配)
3. 筛选特定标注员的数据(绩效统计)
4. 筛选符合多个条件的数据(复杂查询)
"""

import pandas as pd
import numpy as np

# ========== 准备测试数据 ==========

print("=" * 60)
print("准备测试数据集")
print("=" * 60)

# 创建一个较大的数据集,包含多种场景
data = {
    '文件名': [
        'cat_001.jpg', 'dog_002.jpg', 'cat_003.png', 'bird_004.jpg',
        'dog_005.jpg', 'cat_006.jpg', 'bird_007.png', 'dog_008.jpg',
        'cat_009.jpg', 'dog_010.jpg', 'cat_011.jpg', 'bird_012.jpg',
        'dog_013.jpg', 'cat_014.png', 'bird_015.jpg', 'dog_016.jpg'
    ],
    '标签': [
        '猫', '狗', '猫', '鸟', '狗', '猫', '鸟', '狗',
        '猫', '狗', '猫', '鸟', '狗', '猫', '鸟', '狗'
    ],
    '标注员': [
        '张三', '李四', '张三', '王五', '李四', '张三', '王五', '李四',
        '张三', '王五', '李四', '张三', '王五', '李四', '张三', '王五'
    ],
    '质检状态': [
        '通过', '通过', '待质检', '通过', '未通过', '通过', '待质检', '通过',
        '通过', '待质检', '通过', '未通过', '通过', '待质检', '通过', '通过'
    ],
    '分数': [
        95, 88, 75, 92, 65, 90, 78, 85,
        93, 72, 89, 68, 91, 76, 94, 87
    ],
    '标注日期': [
        '2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04',
        '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08',
        '2024-01-09', '2024-01-10', '2024-01-11', '2024-01-12',
        '2024-01-13', '2024-01-14', '2024-01-15', '2024-01-16'
    ]
}

df = pd.DataFrame(data)

print("\n完整数据集:")
print(df)
print(f"\n数据规模: {df.shape[0]}行 x {df.shape[1]}列")


# ========== 第一部分: 单条件筛选 ==========

print("\n" + "=" * 60)
print("第一部分: 单条件筛选")
print("=" * 60)

# 1.1 等值筛选

print("\n【1.1 等值筛选 - 筛选特定标签】")

# 场景: 筛选所有猫的图片
cats = df[df['标签'] == '猫']
print(f"\n筛选标签为'猫'的数据: {len(cats)}条")
print(cats)

# 💡 知识点: 布尔索引的原理
# df['标签'] == '猫'  # 返回True/False的Series
# df[布尔Series]     # 只保留True对应的行

print("\n【理解布尔索引】")
boolean_mask = df['标签'] == '猫'
print("布尔掩码(True表示匹配):")
print(boolean_mask)

# 场景: 筛选特定标注员的数据
zhang_data = df[df['标注员'] == '张三']
print(f"\n筛选标注员为'张三'的数据: {len(zhang_data)}条")
print(zhang_data[['文件名', '标签', '标注员']])

# 1.2 比较筛选(数值型)

print("\n【1.2 比较筛选 - 筛选高分数据】")

# 场景: 筛选分数大于90的数据
high_score = df[df['分数'] > 90]
print(f"\n筛选分数>90的数据: {len(high_score)}条")
print(high_score[['文件名', '标签', '分数']])

# 场景: 筛选分数在80-90之间的数据
medium_score = df[(df['分数'] >= 80) & (df['分数'] < 90)]
print(f"\n筛选分数在80-90之间的数据: {len(medium_score)}条")
print(medium_score[['文件名', '分数']])

# 📌 实战技巧: 常用比较运算符
# ==  等于
# !=  不等于
# >   大于
# >=  大于等于
# <   小于
# <=  小于等于

# 1.3 不等值筛选

print("\n【1.3 不等值筛选 - 排除特定数据】")

# 场景: 筛选非猫的数据
not_cats = df[df['标签'] != '猫']
print(f"\n筛选标签不是'猫'的数据: {len(not_cats)}条")
print(not_cats['标签'].value_counts())


# ========== 第二部分: 多条件筛选 ==========

print("\n" + "=" * 60)
print("第二部分: 多条件筛选(与、或、非)")
print("=" * 60)

# 2.1 多条件 - 与(&)

print("\n【2.1 与条件(&) - 同时满足多个条件】")

# 场景: 筛选猫且分数>90的数据
high_score_cats = df[(df['标签'] == '猫') & (df['分数'] > 90)]
print(f"\n筛选'猫'且分数>90的数据: {len(high_score_cats)}条")
print(high_score_cats[['文件名', '标签', '分数']])

# 场景: 筛选张三标注且质检通过的数据
zhang_passed = df[(df['标注员'] == '张三') & (df['质检状态'] == '通过')]
print(f"\n筛选'张三'标注且质检通过的数据: {len(zhang_passed)}条")
print(zhang_passed[['文件名', '标注员', '质检状态']])

# ⚠️ 常见错误: 使用and而不是&
# 错误: df[df['标签'] == '猫' and df['分数'] > 90]  # 会报错!
# 正确: df[(df['标签'] == '猫') & (df['分数'] > 90)]

# ⚠️ 常见错误: 忘记加括号
# 错误: df[df['标签'] == '猫' & df['分数'] > 90]  # 会报错!
# 正确: df[(df['标签'] == '猫') & (df['分数'] > 90)]

# 2.2 多条件 - 或(|)

print("\n【2.2 或条件(|) - 满足任一条件】")

# 场景: 筛选猫或狗的图片
cats_or_dogs = df[(df['标签'] == '猫') | (df['标签'] == '狗')]
print(f"\n筛选'猫'或'狗'的数据: {len(cats_or_dogs)}条")
print(cats_or_dogs['标签'].value_counts())

# 场景: 筛选分数特别高(>90)或特别低(<70)的数据
extreme_scores = df[(df['分数'] > 90) | (df['分数'] < 70)]
print(f"\n筛选分数>90或<70的数据: {len(extreme_scores)}条")
print(extreme_scores[['文件名', '分数']].sort_values('分数'))

# 📌 实战技巧: 什么时候用|?
# - 筛选多个类别: 猫或狗
# - 筛选异常值: 太高或太低
# - 筛选多种状态: 待质检或未通过

# 2.3 多条件 - 非(~)

print("\n【2.3 非条件(~) - 取反】")

# 场景: 筛选不是质检通过的数据
not_passed = df[~(df['质检状态'] == '通过')]
print(f"\n筛选质检状态不是'通过'的数据: {len(not_passed)}条")
print(not_passed[['文件名', '质检状态']])

# 等价写法
not_passed_v2 = df[df['质检状态'] != '通过']
print(f"\n等价写法结果: {len(not_passed_v2)}条")

# 💡 知识点: ~什么时候用?
# - 取反复杂条件: ~((条件1) & (条件2))
# - 配合isin()取反: ~df['标签'].isin(['猫', '狗'])

# 2.4 三个及以上条件

print("\n【2.4 复杂多条件组合】")

# 场景: 筛选张三标注、猫类别、质检通过的数据
complex_filter = df[
    (df['标注员'] == '张三') &
    (df['标签'] == '猫') &
    (df['质检状态'] == '通过')
]
print(f"\n三条件筛选: {len(complex_filter)}条")
print(complex_filter)

# 场景: 筛选(猫且分数>90) 或 (狗且张三标注)的数据
mixed_filter = df[
    ((df['标签'] == '猫') & (df['分数'] > 90)) |
    ((df['标签'] == '狗') & (df['标注员'] == '张三'))
]
print(f"\n混合条件筛选: {len(mixed_filter)}条")
print(mixed_filter[['文件名', '标签', '标注员', '分数']])


# ========== 第三部分: 字符串筛选 ==========

print("\n" + "=" * 60)
print("第三部分: 字符串筛选(.str方法)")
print("=" * 60)

# 3.1 包含筛选(contains)

print("\n【3.1 contains - 包含某个关键词】")

# 场景: 筛选文件名包含'cat'的图片
contains_cat = df[df['文件名'].str.contains('cat')]
print(f"\n筛选文件名包含'cat'的数据: {len(contains_cat)}条")
print(contains_cat['文件名'])

# 场景: 筛选文件名包含数字'01'的图片
contains_01 = df[df['文件名'].str.contains('01')]
print(f"\n筛选文件名包含'01'的数据: {len(contains_01)}条")
print(contains_01['文件名'])

# 📌 实战技巧: contains的参数
# - case=False: 不区分大小写
# - na=False: 遇到缺失值返回False而不是NaN
# - regex=True: 支持正则表达式

# 示例: 不区分大小写
contains_cat_ignore_case = df[df['文件名'].str.contains('CAT', case=False)]
print(f"\n不区分大小写筛选'CAT': {len(contains_cat_ignore_case)}条")

# 3.2 开头筛选(startswith)

print("\n【3.2 startswith - 以某个前缀开头】")

# 场景: 筛选以'cat_'开头的文件
starts_with_cat = df[df['文件名'].str.startswith('cat_')]
print(f"\n筛选以'cat_'开头的文件: {len(starts_with_cat)}条")
print(starts_with_cat['文件名'])

# 场景: 筛选以'dog_'开头的文件
starts_with_dog = df[df['文件名'].str.startswith('dog_')]
print(f"\n筛选以'dog_'开头的文件: {len(starts_with_dog)}条")
print(starts_with_dog['文件名'])

# 3.3 结尾筛选(endswith)

print("\n【3.3 endswith - 以某个后缀结尾】")

# 场景: 筛选.jpg格式的图片
jpg_files = df[df['文件名'].str.endswith('.jpg')]
print(f"\n筛选.jpg格式的图片: {len(jpg_files)}条")
print(jpg_files['文件名'])

# 场景: 筛选.png格式的图片
png_files = df[df['文件名'].str.endswith('.png')]
print(f"\n筛选.png格式的图片: {len(png_files)}条")
print(png_files['文件名'])

# 场景: 筛选多种格式(jpg或png)
valid_formats = df[df['文件名'].str.endswith(('.jpg', '.png'))]
print(f"\n筛选.jpg或.png格式: {len(valid_formats)}条")

# 3.4 字符串长度筛选

print("\n【3.4 字符串长度筛选】")

# 场景: 筛选文件名长度>12的文件
long_filenames = df[df['文件名'].str.len() > 12]
print(f"\n筛选文件名长度>12的文件: {len(long_filenames)}条")
print(long_filenames[['文件名', df['文件名'].str.len()]])


# ========== 第四部分: isin多值匹配 ==========

print("\n" + "=" * 60)
print("第四部分: isin()多值匹配(最常用!)")
print("=" * 60)

# 4.1 基础用法

print("\n【4.1 isin基础 - 匹配多个值】")

# 场景: 筛选多个标签
selected_labels = ['猫', '狗']
cats_dogs = df[df['标签'].isin(selected_labels)]
print(f"\n筛选标签为['猫', '狗']的数据: {len(cats_dogs)}条")
print(cats_dogs['标签'].value_counts())

# 💡 知识点: isin vs 多个|条件
# 方法1(推荐): df[df['标签'].isin(['猫', '狗'])]
# 方法2: df[(df['标签'] == '猫') | (df['标签'] == '狗')]
# isin更简洁,性能更好!

# 场景: 筛选多个标注员的数据
team_a = ['张三', '李四']
team_a_data = df[df['标注员'].isin(team_a)]
print(f"\n筛选A组标注员的数据: {len(team_a_data)}条")
print(team_a_data['标注员'].value_counts())

# 4.2 取反(不在列表中)

print("\n【4.2 isin取反 - 不在列表中】")

# 场景: 筛选不是猫和狗的数据
not_cats_dogs = df[~df['标签'].isin(['猫', '狗'])]
print(f"\n筛选标签不是['猫', '狗']的数据: {len(not_cats_dogs)}条")
print(not_cats_dogs['标签'].value_counts())

# 📌 实战技巧: ~配合isin()
# ~df['列'].isin([值1, 值2])  # 不在列表中
# 等价于: (df['列'] != 值1) & (df['列'] != 值2)

# 4.3 isin结合其他条件

print("\n【4.3 isin结合其他条件】")

# 场景: 筛选(猫或狗) 且 (分数>85)的数据
filtered = df[
    df['标签'].isin(['猫', '狗']) &
    (df['分数'] > 85)
]
print(f"\n筛选(猫或狗)且分数>85的数据: {len(filtered)}条")
print(filtered[['文件名', '标签', '分数']])


# ========== 第五部分: 空值筛选 ==========

print("\n" + "=" * 60)
print("第五部分: 空值筛选(notna/isnull)")
print("=" * 60)

# 添加一些缺失值用于演示
df_with_na = df.copy()
df_with_na.loc[0, '分数'] = None
df_with_na.loc[3, '质检状态'] = None

print("\n包含缺失值的数据:")
print(df_with_na.head())

# 5.1 筛选非空值

print("\n【5.1 notna() - 筛选非空值】")

# 场景: 筛选分数不为空的数据
has_score = df_with_na[df_with_na['分数'].notna()]
print(f"\n筛选分数不为空的数据: {len(has_score)}条")

# 5.2 筛选空值

print("\n【5.2 isnull() - 筛选空值】")

# 场景: 筛选质检状态为空的数据
no_qc = df_with_na[df_with_na['质检状态'].isnull()]
print(f"\n筛选质检状态为空的数据: {len(no_qc)}条")
print(no_qc[['文件名', '质检状态']])

# ⚠️ 常见错误: 用==None筛选空值
# 错误: df[df['分数'] == None]  # 不会工作!
# 正确: df[df['分数'].isnull()]


# ========== 第六部分: 实战案例 ==========

print("\n" + "=" * 60)
print("第六部分: 实战案例 - AI训练师日常筛选任务")
print("=" * 60)

# 案例1: 分配质检任务

print("\n【案例1: 分配质检任务】")

# 需求: 筛选待质检的数据,按标注员分组分配
to_review = df[df['质检状态'] == '待质检']
print(f"待质检数据: {len(to_review)}条")

for annotator in to_review['标注员'].unique():
    tasks = to_review[to_review['标注员'] == annotator]
    print(f"{annotator}的待质检任务: {len(tasks)}条")
    print(tasks[['文件名', '标签']])
    print()

# 案例2: 准备特定类别的训练集

print("\n【案例2: 准备训练集 - 只要猫和狗】")

# 需求: 筛选猫和狗、质检通过、分数>80的数据用于训练
train_data = df[
    df['标签'].isin(['猫', '狗']) &         # 只要猫和狗
    (df['质检状态'] == '通过') &           # 质检通过
    (df['分数'] > 80)                      # 高质量(分数>80)
]

print(f"符合训练要求的数据: {len(train_data)}条")
print("\n标签分布:")
print(train_data['标签'].value_counts())

# 检查数据是否均衡
cat_count = len(train_data[train_data['标签'] == '猫'])
dog_count = len(train_data[train_data['标签'] == '狗'])
print(f"\n数据均衡性: 猫{cat_count}条, 狗{dog_count}条")

if abs(cat_count - dog_count) > 2:
    print("⚠️ 警告: 数据不均衡,可能需要欠采样或过采样!")

# 案例3: 统计标注员绩效

print("\n【案例3: 统计标注员绩效】")

# 需求: 统计每个标注员的质检通过率
for annotator in df['标注员'].unique():
    # 筛选该标注员的所有数据
    annotator_data = df[df['标注员'] == annotator]
    total = len(annotator_data)

    # 筛选质检通过的数据
    passed = len(annotator_data[annotator_data['质检状态'] == '通过'])

    # 计算通过率
    pass_rate = passed / total * 100 if total > 0 else 0

    # 计算平均分
    avg_score = annotator_data['分数'].mean()

    print(f"{annotator}: 总数{total}条, 通过{passed}条, 通过率{pass_rate:.1f}%, 平均分{avg_score:.1f}")

# 案例4: 找出需要重新标注的数据

print("\n【案例4: 找出需要重新标注的数据】")

# 需求: 未通过且分数<70的数据需要重新标注
reannotate = df[
    (df['质检状态'] == '未通过') &
    (df['分数'] < 70)
]

print(f"需要重新标注的数据: {len(reannotate)}条")
print(reannotate[['文件名', '标签', '标注员', '分数', '质检状态']])


# ========== 总结 ==========

print("\n" + "=" * 60)
print("总结")
print("=" * 60)

print("""
✅ 数据筛选核心技能:

1️⃣ 单条件筛选:
   - 等值: df[df['列'] == 值]
   - 比较: df[df['列'] > 值]
   - 不等: df[df['列'] != 值]

2️⃣ 多条件筛选:
   - 与: df[(条件1) & (条件2)]
   - 或: df[(条件1) | (条件2)]
   - 非: df[~(条件)]
   ⚠️ 必须用&、|、~,不能用and、or、not
   ⚠️ 每个条件必须加括号

3️⃣ 字符串筛选:
   - 包含: df['列'].str.contains('关键词')
   - 开头: df['列'].str.startswith('前缀')
   - 结尾: df['列'].str.endswith('后缀')

4️⃣ 多值匹配:
   - 在列表中: df['列'].isin([值1, 值2])
   - 不在列表: ~df['列'].isin([值1, 值2])

5️⃣ 空值筛选:
   - 非空: df['列'].notna()
   - 为空: df['列'].isnull()

🎯 AI训练师工作应用:
   - 质检任务分配: 筛选待质检数据
   - 训练集准备: 筛选高质量数据
   - 绩效统计: 筛选特定标注员数据
   - 数据分析: 复杂条件组合筛选

📚 下一步学习:
   - 7_practice.py: 综合练习
   - 第八章: AI标注实战
""")

print("\n⚠️ 常见错误:")
print("1. 多条件用and/or而不是&/|: (df['A'] == 1) and (df['B'] == 2)  ❌")
print("2. 忘记加括号: df[df['A'] == 1 & df['B'] == 2]  ❌")
print("3. 空值用==None: df[df['列'] == None]  ❌")
print("4. 字符串筛选忘记.str: df['列'].contains('关键词')  ❌")
print("5. isin()参数不是列表: df['列'].isin('猫', '狗')  ❌")

print("\n💡 扩展思考:")
print("1. 如何优化复杂筛选条件的可读性?")
print("   提示: 可以先定义布尔掩码变量")
print("2. 如何处理多列组合筛选?")
print("   提示: 可以用query()方法")
print("3. 如何保存常用的筛选条件?")
print("   提示: 封装成函数")
