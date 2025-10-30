"""
Day 2 测评 - 实操题1: 文件名批量处理
解法2: 列表推导式版 - 更Python化
难度: ★★★☆☆
"""

print("=" * 60)
print("文件名批量处理工具 - 列表推导式版")
print("=" * 60)

# 原始文件名列表
files = ['data.txt', 'image.jpg', 'report.pdf']

# 使用列表推导式批量添加前缀（Day4会学）
new_files = ['2024_' + file for file in files]

# 输出结果
print("\n【重命名对照表】")
print("-" * 60)
print(f"{'原文件名':<20} {'→':<5} {'新文件名':<20}")
print("-" * 60)

# 使用zip同时遍历两个列表
for old, new in zip(files, new_files):
    print(f"{old:<20} {'→':<5} {new:<20}")

print("-" * 60)
print(f"\n✓ 共处理 {len(files)} 个文件")

# 额外功能：统计文件类型
print("\n【文件类型统计】")
extensions = [file.split('.')[-1] for file in files]
for ext in set(extensions):
    count = extensions.count(ext)
    print(f"  .{ext}: {count}个")
