"""
Day 5 测评 - 实操题1: 文本清洗函数
解法1: 基础版
"""

import re

def clean_text(text):
    """
    文本清洗函数
    1. 去除首尾空格
    2. 转为小写
    3. 去除特殊字符(只保留字母数字)
    4. 返回处理后的文本
    """
    # 1. 去除首尾空格
    text = text.strip()

    # 2. 转为小写
    text = text.lower()

    # 3. 去除特殊字符(只保留字母、数字、空格)
    text = re.sub(r'[^a-z0-9\s]', '', text)

    return text


# 测试函数
print("=" * 60)
print("文本清洗工具")
print("=" * 60)

test_texts = [
    "  Hello World!  ",
    "Python@2024#Programming",
    " Data-Science & AI  ",
    "  Test_123... "
]

print("\n【清洗前后对比】")
print("-" * 60)

for text in test_texts:
    cleaned = clean_text(text)
    print(f"原文本: '{text}'")
    print(f"清洗后: '{cleaned}'")
    print(f"字符数: {len(text)} → {len(cleaned)}")
    print("-" * 60)

print("\n✓ 清洗完成!")
