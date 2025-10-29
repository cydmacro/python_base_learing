"""
Day 9 测评 - 实操题2: 图片分类数据集准备(模拟版)
解法1: 完整版 - 分层采样 + 目录结构 + 统计报告
"""

import random

print("=" * 70)
print("图片分类数据集准备工具")
print("=" * 70)

# 1. 模拟创建图片文件列表(3个类别,每类10张)
categories = ['cat', 'dog', 'bird']
all_images = []

for category in categories:
    for i in range(1, 11):
        all_images.append({
            'filename': f'{category}_{i:03d}.jpg',
            'category': category
        })

print(f"\n总图片数: {len(all_images)}")
print("类别分布:")
for cat in categories:
    count = sum(1 for img in all_images if img['category'] == cat)
    print(f"  {cat}: {count}张")

# 2. 按8:2比例划分训练集和测试集(使用分层采样)
train_set = []
test_set = []

random.seed(42)  # 固定随机种子,确保可复现

for category in categories:
    # 获取该类别的所有图片
    category_images = [img for img in all_images if img['category'] == category]

    # 随机打乱
    random.shuffle(category_images)

    # 按8:2划分
    split_point = int(len(category_images) * 0.8)
    train_set.extend(category_images[:split_point])
    test_set.extend(category_images[split_point:])

print("\n" + "=" * 70)
print("【数据集划分】")
print("=" * 70)
print(f"训练集: {len(train_set)}张")
print(f"测试集: {len(test_set)}张")
print(f"划分比例: {len(train_set)/(len(train_set)+len(test_set))*100:.1f}% : {len(test_set)/(len(train_set)+len(test_set))*100:.1f}%")

# 3. 创建标准目录结构(模拟)
directory_structure = """
dataset/
├── train/
│   ├── cat/     (8张)
│   ├── dog/     (8张)
│   └── bird/    (8张)
└── test/
    ├── cat/     (2张)
    ├── dog/     (2张)
    └── bird/    (2张)
"""

print("\n【目录结构】")
print(directory_structure)

# 4. 输出划分报告
print("=" * 70)
print("【详细划分报告】")
print("=" * 70)

for dataset_name, dataset in [('训练集', train_set), ('测试集', test_set)]:
    print(f"\n{dataset_name} ({len(dataset)}张):")
    print("-" * 70)
    print(f"{'类别':<10} {'数量':<8} {'占比':<10} {'样本':<30}")
    print("-" * 70)

    for category in categories:
        cat_images = [img for img in dataset if img['category'] == category]
        percentage = len(cat_images) / len(dataset) * 100
        samples = ', '.join([img['filename'] for img in cat_images[:3]])
        if len(cat_images) > 3:
            samples += '...'

        print(f"{category:<10} {len(cat_images):<8} {percentage:>5.1f}%   {samples:<30}")

# 5. 类别平衡度检查
print("\n" + "=" * 70)
print("【类别平衡度检查】")
print("=" * 70)

def check_balance(dataset, name):
    """检查数据集的类别平衡度"""
    counts = {}
    for category in categories:
        counts[category] = sum(1 for img in dataset if img['category'] == category)

    max_count = max(counts.values())
    min_count = min(counts.values())

    balance_ratio = (min_count / max_count) * 100

    print(f"\n{name}:")
    print(f"  最多类别样本数: {max_count}")
    print(f"  最少类别样本数: {min_count}")
    print(f"  平衡度: {balance_ratio:.1f}%", end="")

    if balance_ratio >= 70:
        print(" ✓ (良好)")
    elif balance_ratio >= 50:
        print(" ! (一般)")
    else:
        print(" ✗ (需调整)")

check_balance(train_set, "训练集")
check_balance(test_set, "测试集")

# 6. 总结
print("\n" + "=" * 70)
print("【数据集准备总结】")
print("=" * 70)
print(f"✓ 总样本数: {len(all_images)}")
print(f"✓ 训练集: {len(train_set)}张 ({len(train_set)/len(all_images)*100:.0f}%)")
print(f"✓ 测试集: {len(test_set)}张 ({len(test_set)/len(all_images)*100:.0f}%)")
print(f"✓ 类别数: {len(categories)}")
print(f"✓ 使用分层采样: 是")
print(f"✓ 类别平衡: 良好")
print("\n数据集准备完成,可用于模型训练!")
print("=" * 70)
