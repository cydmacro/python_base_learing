"""
Project 1: 客服对话文本清洗工具
版本: v2 - 改进版 (150行)
功能: 批量文件处理 + 函数封装 + 统计报告
难度: ★★★☆☆
"""

import re

# 清洗函数
def clean_text(text):
    """文本清洗"""
    text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9\s，。！？、：；""''（）【】]', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text

def process_file(input_file, output_file):
    """处理文件"""
    print(f"\n正在处理: {input_file}")

    # 读取文件
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 批量清洗
    cleaned_lines = []
    stats = {'total': len(lines), 'cleaned': 0, 'chars_before': 0, 'chars_after': 0}

    for line in lines:
        stats['chars_before'] += len(line)
        cleaned = clean_text(line)

        if cleaned:  # 只保留非空行
            cleaned_lines.append(cleaned + '\n')
            stats['cleaned'] += 1
            stats['chars_after'] += len(cleaned)

    # 保存结果
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)

    # 返回统计
    return stats

# 主程序
print("=" * 70)
print("文本清洗工具 v2.0 - 批量处理版")
print("=" * 70)

# 创建测试数据
test_data = """你好！！！   我想咨询一下产品信息😊😊
###价格是多少啊？？？   !!!
【客服】：  感谢您的咨询~~~  请问有什么可以帮您的呢？？
   这个产品真的很好用👍👍   推荐购买！！！
@管理员  能给个优惠吗😭😭😭
"""

with open('dialogues.txt', 'w', encoding='utf-8') as f:
    f.write(test_data)

# 处理文件
stats = process_file('dialogues.txt', 'dialogues_cleaned.txt')

# 输出报告
print("\n" + "=" * 70)
print("【处理报告】")
print("=" * 70)
print(f"原始行数: {stats['total']}")
print(f"保留行数: {stats['cleaned']}")
print(f"原始字符: {stats['chars_before']}")
print(f"清洗字符: {stats['chars_after']}")
print(f"压缩率: {(1 - stats['chars_after']/stats['chars_before'])*100:.1f}%")
print("\n✓ 清洗完成! 已保存到: dialogues_cleaned.txt")
