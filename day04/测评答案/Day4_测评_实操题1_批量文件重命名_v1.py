"""
Day 4 测评 - 实操题1: 批量文件重命名
解法1: 基础版 - 使用循环
"""

print("=" * 60)
print("批量文件重命名工具")
print("=" * 60)

# 原始文件名列表
files = ['img1.jpg', 'img2.jpg', 'img3.jpg']

# 新文件名列表
new_files = []

# 重命名: photo_001.jpg, photo_002.jpg, photo_003.jpg
for i in range(len(files)):
    new_name = f'photo_{i+1:03d}.jpg'
    new_files.append(new_name)

# 输出重命名对照表
print("\n【重命名对照表】")
print("-" * 60)
print(f"{'原文件名':<20} {'→':<5} {'新文件名':<20}")
print("-" * 60)

for old, new in zip(files, new_files):
    print(f"{old:<20} {'→':<5} {new:<20}")

print("-" * 60)
print(f"\n✓ 共重命名 {len(files)} 个文件")
