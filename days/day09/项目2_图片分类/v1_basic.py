"""
Project 2: 图片分类数据集准备工具
版本: v1 - 基础版 (100行)
功能: 简单的文件列表划分
难度: ★★☆☆☆
"""

import random

print("=" * 70)
print("图片数据集准备工具 v1.0 - 基础版")
print("=" * 70)

# 模拟图片文件列表
images = [
    'cat_001.jpg', 'cat_002.jpg', 'cat_003.jpg', 'cat_004.jpg', 'cat_005.jpg',
    'dog_001.jpg', 'dog_002.jpg', 'dog_003.jpg', 'dog_004.jpg', 'dog_005.jpg',
    'bird_001.jpg', 'bird_002.jpg', 'bird_003.jpg', 'bird_004.jpg', 'bird_005.jpg'
]

print(f"\n总图片数: {len(images)}")

# 固定8:2划分
random.seed(42)
random.shuffle(images)

split_point = int(len(images) * 0.8)
train_set = images[:split_point]
test_set = images[split_point:]

print(f"训练集: {len(train_set)}张")
print(f"测试集: {len(test_set)}张")

# 显示划分结果
print("\n【训练集】")
for img in train_set[:5]:
    print(f"  {img}")
print(f"  ... (共{len(train_set)}张)")

print("\n【测试集】")
for img in test_set[:5]:
    print(f"  {img}")
print(f"  ... (共{len(test_set)}张)")

print("\n✓ 划分完成!")
