"""
Project 1: 客服对话文本清洗工具
版本: v1 - 基础版 (80行)
功能: 基础正则表达式清洗 + 单个文本处理
难度: ★★☆☆☆
适合: Day9学完后练习
"""

import re

print("=" * 70)
print("文本清洗工具 v1.0 - 基础版")
print("=" * 70)

# 单个文本清洗
text = "你好！！！   我想咨询一下产品信息😊😊   ###价格是多少啊？？？"

print("\n【原始文本】")
print(text)

# 清洗函数
def clean_text(text):
    """基础文本清洗"""
    # 去除表情符号
    text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9\s，。！？、：；""''（）【】]', '', text)

    # 去除多余空格
    text = re.sub(r'\s+', ' ', text)

    # 去除首尾空格
    text = text.strip()

    return text

# 清洗
cleaned = clean_text(text)

print("\n【清洗后文本】")
print(cleaned)

print("\n【统计】")
print(f"原始字符数: {len(text)}")
print(f"清洗后字符数: {len(cleaned)}")
print(f"减少: {len(text) - len(cleaned)}个字符")
