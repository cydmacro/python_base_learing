"""
Day 2 测评 - 实操题1: 文件名批量处理
解法1: 基础版 - 使用列表和循环
难度: ★★☆☆☆
"""

print("=" * 60)
print("文件名批量处理工具 - 基础版")
print("=" * 60)

# 原始文件名列表
files = ['data.txt', 'image.jpg', 'report.pdf']

# 新文件名列表
new_files = []

# 逐个添加前缀
for file in files:
    new_name = '2024_' + file
    new_files.append(new_name)

# 输出结果
print("\n【重命名对照表】")
print("-" * 60)
print(f"{'原文件名':<20} {'→':<5} {'新文件名':<20}")
print("-" * 60)

for i in range(len(files)):
    print(f"{files[i]:<20} {'→':<5} {new_files[i]:<20}")

print("-" * 60)
print(f"\n共处理 {len(files)} 个文件")
