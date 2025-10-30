"""
Day 9 测评 - 实操题1: 客服对话文本清洗工具
解法1: 基础版
"""

import re

print("=" * 70)
print("客服对话文本清洗工具")
print("=" * 70)

# 1. 创建测试数据(包含特殊符号、多余空格、表情符号)
test_dialogues = [
    "你好！！！   我想咨询一下产品信息😊",
    "【客服】：  感谢您的咨询~~~  请问有什么可以帮您的呢？？",
    "###产品价格是多少啊   ？？？   !!!",
    "   这个产品真的很好用👍👍   推荐购买！！！   ",
    "@管理员  能给个优惠吗😭😭😭   "
]

print("\n【原始对话】")
print("-" * 70)
for i, dialogue in enumerate(test_dialogues, 1):
    print(f"{i}. {dialogue}")

# 2. 实现清洗函数
def clean_text(text):
    """
    清洗文本:
    - 去除特殊字符(保留中英文、数字、常用标点)
    - 去除多余空格
    - 统一格式
    """
    # 去除表情符号和特殊字符
    # 只保留中文、英文、数字和常用标点
    text = re.sub(r'[^a-zA-Z0-9\u4e00-\u9fa5，。！？、：；""''（）【】\s]', '', text)

    # 将多个空格替换为单个空格
    text = re.sub(r'\s+', ' ', text)

    # 去除首尾空格
    text = text.strip()

    # 统一标点符号(将多个重复标点替换为单个)
    text = re.sub(r'！+', '！', text)
    text = re.sub(r'？+', '？', text)
    text = re.sub(r'~+', '', text)

    return text

# 3. 清洗所有对话
cleaned_dialogues = [clean_text(d) for d in test_dialogues]

# 4. 保存清洗前后对比结果
print("\n" + "=" * 70)
print("【清洗前后对比】")
print("=" * 70)

for i, (original, cleaned) in enumerate(zip(test_dialogues, cleaned_dialogues), 1):
    print(f"\n对话 {i}:")
    print(f"  原文: {original}")
    print(f"  清洗: {cleaned}")
    print(f"  字符数: {len(original)} → {len(cleaned)} (减少{len(original)-len(cleaned)})")

# 5. 统计清洗效果
total_original_chars = sum(len(d) for d in test_dialogues)
total_cleaned_chars = sum(len(d) for d in cleaned_dialogues)

print("\n" + "=" * 70)
print("【清洗效果统计】")
print("=" * 70)
print(f"对话总数: {len(test_dialogues)}")
print(f"原始总字符数: {total_original_chars}")
print(f"清洗后总字符数: {total_cleaned_chars}")
print(f"减少字符数: {total_original_chars - total_cleaned_chars}")
print(f"压缩率: {(1 - total_cleaned_chars/total_original_chars)*100:.1f}%")

print("\n" + "=" * 70)
print("✓ 文本清洗完成!")
