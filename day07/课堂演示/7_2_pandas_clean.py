"""
【文件说明】
文件名: 7_2_pandas_clean.py
章节: 第七章 - Pandas数据处理基础
知识点: 数据清洗三板斧(缺失值、异常值、重复值)
难度: ⭐⭐⭐ (进阶)
预计学习时间: 50分钟

【学习目标】
1. 掌握缺失值的检测与处理(dropna/fillna)
2. 学会异常值的识别与清洗
3. 熟练使用重复值去除(drop_duplicates)
4. 理解inplace参数的作用

【实际应用场景】
- AI训练: 清洗标注数据中的脏数据
- 数据质检: 处理标注员遗漏或错误的数据
- 数据准备: 确保训练集数据质量,提升模型效果

【前置知识】
- 7_1_pandas_basic.py(CSV读写、数据查看)
- 条件筛选基础

【注意事项】
⚠️ dropna()会永久删除数据,操作前建议备份
⚠️ fillna()填充要合理,不能乱填(如年龄缺失不能填0)
⚠️ inplace=True会直接修改原DataFrame,不返回新对象

【工作流程对照】
这是AI训练师数据清洗的标准流程:
1. 检测脏数据(缺失/异常/重复)
2. 制定清洗策略(删除还是修复)
3. 执行清洗操作
4. 验证清洗效果
5. 导出干净数据
"""

import pandas as pd
import numpy as np

# ========== 准备测试数据 ==========

print("=" * 60)
print("准备包含脏数据的测试数据集")
print("=" * 60)

# 🎯 场景: 模拟从标注平台导出的真实数据
# 包含各种常见问题:缺失值、异常值、重复数据

data = {
    '文件名': [
        'IMG001.jpg', 'IMG002.jpg', 'IMG003.jpg', 'IMG004.jpg', 'IMG005.jpg',
        'IMG006.jpg', 'IMG007.jpg', 'IMG003.jpg',  # ⚠️ 重复文件名
        'IMG008.jpg', 'IMG009.txt',  # ⚠️ 错误格式
        'IMG010.jpg', None,  # ⚠️ 文件名缺失
        'IMG011.jpg', 'IMG012.jpg', 'IMG013.jpg'
    ],
    '标签': [
        '猫', '狗', '猫', None,  # ⚠️ 标签缺失
        '狗', '鸟', '猫', '猫',
        '狗', '猫', '鸟', '狗',
        '大象',  # ⚠️ 异常标签(不在允许范围内)
        '狗', None  # ⚠️ 标签缺失
    ],
    '标注员': [
        '张三', '李四', '张三', '王五', '李四',
        '张三', '王五', '李四',
        '张三', '李四', '王五', '李四',
        '张三', '李四', '王五'
    ],
    '质检状态': [
        '通过', '通过', '待质检', '待质检', '通过',
        None,  # ⚠️ 质检状态缺失
        '待质检', '通过', '通过', '未通过',
        None, None,  # ⚠️ 质检状态缺失
        '通过', '通过', '待质检'
    ],
    '分数': [
        95, 88, 92, 85, 90,
        87, 93, 92,
        -10,  # ⚠️ 异常分数(不可能是负数)
        88, 91, 85,
        200,  # ⚠️ 异常分数(超出范围0-100)
        89, 94
    ]
}

df = pd.DataFrame(data)

print("\n原始数据(包含各种问题):")
print(df)
print(f"\n数据规模: {df.shape[0]}行 x {df.shape[1]}列")


# ========== 第一板斧: 处理缺失值 ==========

print("\n" + "=" * 60)
print("第一板斧: 处理缺失值(Missing Values)")
print("=" * 60)

# 步骤1: 检测缺失值
print("\n【步骤1: 检测缺失值】")

print("\n1.1 查看每个位置是否缺失:")
print(df.isnull())

print("\n1.2 统计每列缺失值数量(最常用!):")
missing_count = df.isnull().sum()
print(missing_count)

print("\n1.3 计算缺失率:")
missing_rate = (df.isnull().sum() / len(df) * 100).round(2)
for col in df.columns:
    if missing_count[col] > 0:
        print(f"{col}: {missing_count[col]}个缺失 ({missing_rate[col]}%)")

# 💡 知识点: 缺失值的表示
# - Python中用None表示
# - Pandas中会转换为NaN(Not a Number)
# - 两者本质相同,都表示"没有值"

# 步骤2: 处理缺失值 - 方法1(删除)

print("\n【步骤2.1: 删除缺失值】")

# 方法2.1.1: 删除任何列有缺失的行(最严格)
df_drop_all = df.dropna()
print(f"\n删除所有含缺失值的行:")
print(f"原始: {len(df)}行 → 删除后: {len(df_drop_all)}行 (删除了{len(df)-len(df_drop_all)}行)")

# ⚠️ 警告: 这种方法太激进,可能删除大量数据!
# 上面的例子中,15行数据只剩5行,损失太大!

# 方法2.1.2: 删除特定列有缺失的行(推荐)
df_drop_label = df.dropna(subset=['标签'])
print(f"\n只删除'标签'列有缺失的行:")
print(f"原始: {len(df)}行 → 删除后: {len(df_drop_label)}行 (删除了{len(df)-len(df_drop_label)}行)")

# 📌 实战技巧: 删除策略
# - 关键列(如标签)缺失 → 必须删除
# - 次要列(如质检状态)缺失 → 可以保留并填充

# 方法2.1.3: 删除全部为空的行
df_sample = pd.DataFrame({
    'A': [1, None, None],
    'B': [2, None, None],
    'C': [3, None, 4]
})
print("\n示例数据:")
print(df_sample)

df_drop_all_na = df_sample.dropna(how='all')
print("\n删除全部为空的行:")
print(df_drop_all_na)

# 步骤3: 处理缺失值 - 方法2(填充)

print("\n【步骤2.2: 填充缺失值】")

# 创建副本,避免修改原数据
df_fill = df.copy()

# 方法2.2.1: 用固定值填充
df_fill['质检状态'].fillna('待质检', inplace=True)
print("\n将'质检状态'的缺失值填充为'待质检':")
print(df_fill[['文件名', '质检状态']])

# 📌 实战技巧: 什么时候用固定值填充?
# - 缺失代表"未处理"状态 → 填充"待处理"
# - 缺失代表"默认值" → 填充合理的默认值
# - 例如: 质检状态缺失 → 默认为"待质检"

# 方法2.2.2: 用统计值填充(数值型数据)
mean_score = df['分数'].mean()  # 计算平均分
print(f"\n分数列的平均值: {mean_score:.2f}")

# 注意: 上面的平均值包含了异常值(-10和200),不合理!
# 应该先清洗异常值,再计算统计值

# 方法2.2.3: 用前一个值填充(时间序列常用)
df_ffill = df.copy()
df_ffill['质检状态'].fillna(method='ffill', inplace=True)
print("\n用前一个值填充'质检状态':")
print(df_ffill[['文件名', '质检状态']])

# 💡 知识点: inplace参数
print("\n【关于inplace参数】")
print("inplace=False(默认): 返回新DataFrame,原数据不变")
print("inplace=True: 直接修改原DataFrame,不返回值")

# 示例:
df_new = df.dropna(subset=['标签'])  # 返回新DataFrame
print(f"原数据行数: {len(df)}")
print(f"新数据行数: {len(df_new)}")

# df.dropna(subset=['标签'], inplace=True)  # 直接修改df
# print(f"修改后df行数: {len(df)}")  # df已经被修改


# ========== 第二板斧: 处理异常值 ==========

print("\n" + "=" * 60)
print("第二板斧: 处理异常值(Outliers)")
print("=" * 60)

# 步骤1: 检测异常值

print("\n【步骤1: 检测数值型异常值】")

# 场景: 分数应该在0-100之间
print("\n原始分数列:")
print(df['分数'])

# 找出异常分数
invalid_scores = df[(df['分数'] < 0) | (df['分数'] > 100)]
print(f"\n发现{len(invalid_scores)}个异常分数:")
print(invalid_scores[['文件名', '分数']])

# 📌 实战技巧: 如何发现异常值?
# 1. 业务逻辑判断: 年龄不能负数,分数不能超100
# 2. 统计方法: 3倍标准差之外的值
# 3. 箱线图: 超出箱体1.5倍IQR的值

print("\n【步骤2: 检测文本型异常值】")

# 场景: 只允许"猫"、"狗"、"鸟"三种标签
allowed_labels = ['猫', '狗', '鸟']

# 找出不在允许范围内的标签(排除缺失值)
df_with_label = df[df['标签'].notna()]  # 先过滤掉缺失值
invalid_labels = df_with_label[~df_with_label['标签'].isin(allowed_labels)]
print(f"\n发现{len(invalid_labels)}个异常标签:")
print(invalid_labels[['文件名', '标签']])

# 💡 知识点: ~符号的含义
# ~df['标签'].isin(allowed_labels)  # ~表示"取反"
# 相当于: df['标签'] not in allowed_labels

print("\n【步骤3: 检测文件格式异常】")

# 场景: 图片文件应该是.jpg/.png等格式
df_with_file = df[df['文件名'].notna()]
invalid_formats = df_with_file[~df_with_file['文件名'].str.endswith(('.jpg', '.png', '.jpeg'))]
print(f"\n发现{len(invalid_formats)}个无效文件格式:")
print(invalid_formats[['文件名', '标签']])

# 步骤4: 处理异常值

print("\n【步骤4.1: 删除异常值】")

# 创建副本
df_clean = df.copy()

# 删除分数异常的行
df_clean = df_clean[(df_clean['分数'] >= 0) & (df_clean['分数'] <= 100)]
print(f"删除异常分数后: {len(df)}行 → {len(df_clean)}行")

# 删除文件格式异常的行
df_clean = df_clean[
    df_clean['文件名'].notna() &  # 文件名不为空
    df_clean['文件名'].str.endswith(('.jpg', '.png', '.jpeg'))  # 格式正确
]
print(f"删除文件格式异常后: 剩余{len(df_clean)}行")

print("\n【步骤4.2: 替换异常值】")

# 创建副本
df_replace = df.copy()

# 将异常标签替换为"其他"
df_replace.loc[
    (df_replace['标签'].notna()) &  # 不是缺失值
    (~df_replace['标签'].isin(allowed_labels)),  # 不在允许列表
    '标签'
] = '其他'

print("\n替换异常标签后:")
print(df_replace['标签'].value_counts())

# 将异常分数修正(这里简单粗暴地取绝对值并截断)
df_replace.loc[df_replace['分数'] < 0, '分数'] = abs(df_replace.loc[df_replace['分数'] < 0, '分数'])
df_replace.loc[df_replace['分数'] > 100, '分数'] = 100

print("\n修正异常分数后:")
print(df_replace['分数'].describe())

# ⚠️ 常见错误: 不合理的填充
# 错误示例: df['年龄'].fillna(0)  # 年龄缺失不能填0!
# 正确做法: df['年龄'].fillna(df['年龄'].median())  # 用中位数


# ========== 第三板斧: 处理重复值 ==========

print("\n" + "=" * 60)
print("第三板斧: 处理重复值(Duplicates)")
print("=" * 60)

# 步骤1: 检测重复值

print("\n【步骤1: 检测重复值】")

# 方法1.1: 检测完全重复的行
print("\n完全重复的行:")
duplicated_mask = df.duplicated()
print(f"重复行数: {duplicated_mask.sum()}个")
print(df[duplicated_mask])

# 💡 知识点: duplicated()的参数
# - keep='first': 第一次出现标记为False,后续标记为True
# - keep='last': 最后一次出现标记为False,前面标记为True
# - keep=False: 所有重复的都标记为True

print("\n查看所有重复的行(包括第一次出现):")
print(df[df.duplicated(keep=False)])

# 方法1.2: 基于特定列检测重复
print("\n【基于'文件名'列检测重复】")
file_duplicated = df.duplicated(subset=['文件名'])
print(f"文件名重复: {file_duplicated.sum()}个")
print("\n重复的文件名:")
print(df[df.duplicated(subset=['文件名'], keep=False)].sort_values('文件名'))

# 📌 实战技巧: 为什么要基于文件名去重?
# - 同一个文件被多次标注
# - 数据导出时重复了
# - 不同标注员标注了同一文件

# 步骤2: 删除重复值

print("\n【步骤2: 删除重复值】")

# 方法2.1: 删除完全重复的行
df_no_dup = df.drop_duplicates()
print(f"\n删除完全重复行: {len(df)}行 → {len(df_no_dup)}行")

# 方法2.2: 基于文件名去重(保留第一次出现)
df_no_file_dup = df.drop_duplicates(subset=['文件名'], keep='first')
print(f"基于文件名去重(保留第一次): {len(df)}行 → {len(df_no_file_dup)}行")

print("\n保留的数据:")
print(df_no_file_dup[df_no_file_dup['文件名'] == 'IMG003.jpg'])

# 方法2.3: 基于文件名去重(保留最后一次)
df_no_file_dup_last = df.drop_duplicates(subset=['文件名'], keep='last')
print(f"\n基于文件名去重(保留最后一次): {len(df)}行 → {len(df_no_file_dup_last)}行")

# 📌 实战技巧: 保留哪一次?
# - 如果有时间戳,保留最新的 → keep='last'
# - 如果有质检状态,保留"通过"的
# - 如果有分数,保留分数最高的

# 方法2.4: 智能去重(保留质量最好的)
print("\n【步骤3: 智能去重 - 保留质检通过的】")

# 策略: 同一文件名,优先保留质检通过的
df_smart = df.copy()

# 先按文件名和质检状态排序(质检"通过"排在前面)
df_smart = df_smart.sort_values(
    by=['文件名', '质检状态'],
    ascending=[True, True],  # 文件名升序,质检状态升序("通过"在"待质检"之前)
    na_position='last'  # 缺失值放最后
)

# 然后去重,保留第一个(即质检通过的)
df_smart = df_smart.drop_duplicates(subset=['文件名'], keep='first')

print(f"智能去重后: {len(df)}行 → {len(df_smart)}行")


# ========== 综合实战: 完整数据清洗流程 ==========

print("\n" + "=" * 60)
print("综合实战: AI训练数据完整清洗流程")
print("=" * 60)

# 重新加载原始数据
df_raw = df.copy()
print(f"\n原始数据: {len(df_raw)}行")

# 步骤1: 删除文件名缺失的数据
df_clean = df_raw.dropna(subset=['文件名'])
print(f"步骤1 - 删除文件名缺失: 剩余{len(df_clean)}行")

# 步骤2: 删除标签缺失的数据
df_clean = df_clean.dropna(subset=['标签'])
print(f"步骤2 - 删除标签缺失: 剩余{len(df_clean)}行")

# 步骤3: 填充质检状态缺失值
df_clean['质检状态'].fillna('待质检', inplace=True)
print(f"步骤3 - 填充质检状态缺失: 完成")

# 步骤4: 清洗异常分数
df_clean = df_clean[(df_clean['分数'] >= 0) & (df_clean['分数'] <= 100)]
print(f"步骤4 - 删除异常分数: 剩余{len(df_clean)}行")

# 步骤5: 清洗无效文件格式
df_clean = df_clean[df_clean['文件名'].str.endswith(('.jpg', '.png', '.jpeg'))]
print(f"步骤5 - 删除无效文件格式: 剩余{len(df_clean)}行")

# 步骤6: 清洗无效标签
df_clean = df_clean[df_clean['标签'].isin(allowed_labels)]
print(f"步骤6 - 删除无效标签: 剩余{len(df_clean)}行")

# 步骤7: 去除重复文件
df_clean = df_clean.drop_duplicates(subset=['文件名'], keep='first')
print(f"步骤7 - 删除重复文件: 剩余{len(df_clean)}行")

# 步骤8: 只保留质检通过的数据(可选,根据需求)
df_final = df_clean[df_clean['质检状态'] == '通过']
print(f"步骤8 - 只保留质检通过: 剩余{len(df_final)}行")

# 数据清洗报告
print("\n" + "=" * 60)
print("数据清洗报告")
print("=" * 60)
print(f"原始数据: {len(df_raw)}行")
print(f"清洗后数据: {len(df_final)}行")
print(f"删除数据: {len(df_raw) - len(df_final)}行 ({(len(df_raw)-len(df_final))/len(df_raw)*100:.1f}%)")

print("\n最终数据预览:")
print(df_final)

print("\n最终标签分布:")
print(df_final['标签'].value_counts())

# 保存清洗后的数据
output_file = 'cleaned_data.csv'
df_final.to_csv(output_file, index=False, encoding='utf-8-sig')
print(f"\n✅ 清洗完成!已保存到: {output_file}")


# ========== 总结 ==========

print("\n" + "=" * 60)
print("总结")
print("=" * 60)

print("""
✅ 数据清洗三板斧:

1️⃣ 处理缺失值:
   - 检测: isnull().sum()
   - 删除: dropna(subset=['列名'])
   - 填充: fillna(value)

2️⃣ 处理异常值:
   - 数值异常: 条件筛选 + 删除/修正
   - 文本异常: isin() + 替换/删除
   - 格式异常: str方法 + 筛选

3️⃣ 处理重复值:
   - 检测: duplicated(subset=['列名'])
   - 删除: drop_duplicates(subset=['列名'], keep='first/last')

🎯 AI训练师工作中的应用:
   - 标注数据质检: 删除标签缺失、重复、异常的数据
   - 训练集准备: 确保数据干净,提升模型效果
   - 数据统计: 生成清洗报告,汇报给项目经理

📚 下一步学习:
   - 7_3_pandas_filter.py: 数据筛选与过滤
   - 7_practice.py: 综合练习
""")

print("\n⚠️ 常见错误:")
print("1. 忘记备份原数据,直接用inplace=True修改")
print("2. 缺失值填充不合理(如年龄填0)")
print("3. 删除重复时keep参数用错,删掉了想要的数据")
print("4. 异常值判断标准不合理,把正常数据当异常删除")
print("5. 清洗顺序错误,导致数据损失过多")

print("\n💡 扩展思考:")
print("1. 如何判断数据清洗是否过度?(删除率>30%需警惕)")
print("2. 如何平衡数据质量和数据数量?")
print("3. 能否自动化数据清洗流程?(编写清洗脚本)")
print("4. 如何记录清洗日志,方便后续追溯?")
