"""
Project 2: 图片分类数据集准备工具
版本: v2 - 改进版 (180行)
功能: 分层采样 + 类别平衡检查 + 统计报告
难度: ★★★☆☆
"""

import random

def stratified_split(images, test_ratio=0.2, random_seed=42):
    """分层采样划分"""
    # 按类别分组
    categories = {}
    for img in images:
        category = img.split('_')[0]
        if category not in categories:
            categories[category] = []
        categories[category].append(img)

    # 对每个类别进行划分
    train_set = []
    test_set = []

    random.seed(random_seed)

    for category, imgs in categories.items():
        random.shuffle(imgs)
        split_point = int(len(imgs) * (1 - test_ratio))
        train_set.extend(imgs[:split_point])
        test_set.extend(imgs[split_point:])

    return train_set, test_set, categories

# 主程序
print("=" * 70)
print("图片数据集准备工具 v2.0 - 分层采样版")
print("=" * 70)

# 模拟图片
images = []
for category in ['cat', 'dog', 'bird']:
    for i in range(1, 11):
        images.append(f'{category}_{i:03d}.jpg')

# 分层采样划分
train_set, test_set, categories = stratified_split(images, test_ratio=0.2)

print(f"\n总图片数: {len(images)}")
print(f"训练集: {len(train_set)}张 ({len(train_set)/len(images)*100:.0f}%)")
print(f"测试集: {len(test_set)}张 ({len(test_set)/len(images)*100:.0f}%)")

# 类别平衡检查
print("\n" + "=" * 70)
print("【类别分布检查】")
print("=" * 70)

def check_distribution(dataset, name):
    """检查类别分布"""
    dist = {}
    for img in dataset:
        cat = img.split('_')[0]
        dist[cat] = dist.get(cat, 0) + 1

    print(f"\n{name}:")
    for cat, count in sorted(dist.items()):
        percentage = count / len(dataset) * 100
        print(f"  {cat}: {count}张 ({percentage:.1f}%)")

check_distribution(train_set, "训练集")
check_distribution(test_set, "测试集")

# 平衡度检查
print("\n" + "=" * 70)
print("【平衡度检查】")
print("=" * 70)

for name, dataset in [("训练集", train_set), ("测试集", test_set)]:
    counts = {}
    for img in dataset:
        cat = img.split('_')[0]
        counts[cat] = counts.get(cat, 0) + 1

    max_count = max(counts.values())
    min_count = min(counts.values())
    balance_ratio = (min_count / max_count) * 100

    print(f"\n{name}平衡度: {balance_ratio:.1f}%", end="")
    if balance_ratio >= 70:
        print(" ✓")
    else:
        print(" ⚠")

print("\n✓ 数据集准备完成!")
