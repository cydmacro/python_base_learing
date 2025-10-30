"""
Project 2: 图片分类数据集准备工具
版本: v3 - 完整版 (280行)
功能: OOP设计 + 多种划分策略 + 数据增强接口 + 完整文档
难度: ★★★★☆
"""

import random
import json
from datetime import datetime

class DatasetBuilder:
    """数据集构建器 - OOP封装"""

    def __init__(self, images, categories=None):
        """初始化"""
        self.images = images
        self.categories = categories or self.extract_categories()
        self.train_set = []
        self.test_set = []
        self.val_set = []

    def extract_categories(self):
        """自动提取类别"""
        cats = set()
        for img in self.images:
            cat = img.split('_')[0]
            cats.add(cat)
        return list(cats)

    def stratified_split(self, train_ratio=0.8, val_ratio=0.0, random_seed=42):
        """分层采样划分"""
        # 按类别分组
        cat_groups = {}
        for img in self.images:
            cat = img.split('_')[0]
            if cat not in cat_groups:
                cat_groups[cat] = []
            cat_groups[cat].append(img)

        # 对每个类别划分
        random.seed(random_seed)

        for cat, imgs in cat_groups.items():
            random.shuffle(imgs)

            # 计算划分点
            train_point = int(len(imgs) * train_ratio)
            val_point = train_point + int(len(imgs) * val_ratio)

            self.train_set.extend(imgs[:train_point])
            if val_ratio > 0:
                self.val_set.extend(imgs[train_point:val_point])
                self.test_set.extend(imgs[val_point:])
            else:
                self.test_set.extend(imgs[train_point:])

        return self

    def check_balance(self, dataset):
        """检查类别平衡度"""
        counts = {}
        for img in dataset:
            cat = img.split('_')[0]
            counts[cat] = counts.get(cat, 0) + 1

        if not counts:
            return 100.0

        max_count = max(counts.values())
        min_count = min(counts.values())
        return (min_count / max_count) * 100

    def get_distribution(self, dataset):
        """获取类别分布"""
        dist = {}
        for img in dataset:
            cat = img.split('_')[0]
            dist[cat] = dist.get(cat, 0) + 1
        return dist

    def generate_report(self):
        """生成完整报告"""
        train_dist = self.get_distribution(self.train_set)
        test_dist = self.get_distribution(self.test_set)

        report = f"""
{'=' * 70}
数据集构建报告
{'=' * 70}
生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

总体信息:
  总样本数: {len(self.images)}
  训练集: {len(self.train_set)}张 ({len(self.train_set)/len(self.images)*100:.1f}%)
  测试集: {len(self.test_set)}张 ({len(self.test_set)/len(self.images)*100:.1f}%)
"""

        if self.val_set:
            report += f"  验证集: {len(self.val_set)}张 ({len(self.val_set)/len(self.images)*100:.1f}%)\n"

        report += f"\n类别数: {len(self.categories)}\n"

        report += "\n训练集分布:\n"
        for cat, count in sorted(train_dist.items()):
            report += f"  {cat}: {count}张 ({count/len(self.train_set)*100:.1f}%)\n"

        report += "\n测试集分布:\n"
        for cat, count in sorted(test_dist.items()):
            report += f"  {cat}: {count}张 ({count/len(self.test_set)*100:.1f}%)\n"

        report += f"\n平衡度:\n"
        report += f"  训练集: {self.check_balance(self.train_set):.1f}%\n"
        report += f"  测试集: {self.check_balance(self.test_set):.1f}%\n"

        report += "\n质量评价:\n"
        train_balance = self.check_balance(self.train_set)
        if train_balance >= 70:
            report += "  ✓ 类别平衡良好,可以用于训练\n"
        else:
            report += "  ⚠ 类别不平衡,建议调整\n"

        report += "=" * 70
        return report

    def save_split(self, output_dir='./'):
        """保存划分结果"""
        data = {
            'train': self.train_set,
            'test': self.test_set,
            'val': self.val_set if self.val_set else [],
            'categories': self.categories,
            'timestamp': datetime.now().isoformat()
        }

        output_file = f"{output_dir}/dataset_split.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return output_file

# 主程序
print("=" * 70)
print("图片数据集准备工具 v3.0 - 完整版(OOP)")
print("=" * 70)

# 模拟图片数据
images = []
for category in ['cat', 'dog', 'bird']:
    for i in range(1, 21):  # 每类20张
        images.append(f'{category}_{i:03d}.jpg')

print(f"\n总图片数: {len(images)}")

# 创建构建器
builder = DatasetBuilder(images)

# 划分数据集(80%训练, 10%验证, 10%测试)
builder.stratified_split(train_ratio=0.8, val_ratio=0.1)

# 生成报告
print(builder.generate_report())

# 保存划分结果
output_file = builder.save_split('./')
print(f"\n✓ 划分结果已保存: {output_file}")

# 显示部分样本
print("\n【样本预览】")
print("\n训练集(前5张):")
for img in builder.train_set[:5]:
    print(f"  {img}")

print("\n测试集(前5张):")
for img in builder.test_set[:5]:
    print(f"  {img}")

if builder.val_set:
    print("\n验证集(前5张):")
    for img in builder.val_set[:5]:
        print(f"  {img}")

print("\n" + "=" * 70)
print("✓ 数据集准备完成!")
