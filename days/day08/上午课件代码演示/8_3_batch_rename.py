"""
【文件说明】
章节: 第八章 - AI标注实战
知识点: 批量文件处理
实战应用: 标准化文件命名,便于标注管理

【核心技能】
- os模块文件操作
- 批量重命名
- 文件路径处理
"""

import os

print("=" * 60)
print("批量文件标准化命名工具")
print("=" * 60)

# 模拟文件列表
files = [
    'IMG_20240101_cat.jpg',
    'photo_dog_001.png',
    'bird_pic.jpg',
    '猫咪照片.jpg',
    'DOG002.JPG'
]

print("\n原始文件名:")
for f in files:
    print(f"  {f}")

# 标准化命名规则: 动物类型_序号.扩展名
rename_map = {
    'IMG_20240101_cat.jpg': 'cat_001.jpg',
    'photo_dog_001.png': 'dog_001.png',
    'bird_pic.jpg': 'bird_001.jpg',
    '猫咪照片.jpg': 'cat_002.jpg',
    'DOG002.JPG': 'dog_002.jpg'
}

print("\n重命名方案:")
for old, new in rename_map.items():
    print(f"  {old} → {new}")

print("""
💡 标准化命名的好处:
1. 方便管理和查找
2. 避免中文乱码问题
3. 统一格式便于批处理
4. 文件名直接体现类别

🎯 实际工作中:
- 收到原始数据先批量重命名
- 使用脚本自动化处理
- 按类别分文件夹存放
- 建立文件名与标签的映射表
""")

# 实际代码示例(需要真实文件才能执行)
print("\n完整代码示例:")
print('''
import os

# 批量重命名
for old_name, new_name in rename_map.items():
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"✅ {old_name} → {new_name}")
''')
