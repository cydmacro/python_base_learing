"""
Project 1: 客服对话文本清洗工具
版本: v3 - 完整版 (250行)
功能: OOP设计 + 配置文件 + 日志系统 + 完整错误处理
难度: ★★★★☆
"""

import re
import json
from datetime import datetime

class TextCleaner:
    """文本清洗器 - OOP封装"""

    def __init__(self, config_file=None):
        """初始化清洗器"""
        self.config = self.load_config(config_file)
        self.stats = {'total': 0, 'cleaned': 0, 'chars_before': 0, 'chars_after': 0}
        self.log_file = 'cleaner.log'

    def load_config(self, config_file):
        """加载配置"""
        default_config = {
            'keep_punctuation': True,
            'remove_emojis': True,
            'remove_special_chars': True,
            'strip_whitespace': True
        }

        if config_file:
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                pass

        return default_config

    def log(self, message):
        """写入日志"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {message}\n")

    def clean_text(self, text):
        """清洗单个文本"""
        original_len = len(text)

        # 去除表情符号
        if self.config['remove_emojis']:
            text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9\s，。！？、：；""''（）【】]', '', text)

        # 去除多余空格
        if self.config['strip_whitespace']:
            text = re.sub(r'\s+', ' ', text)
            text = text.strip()

        # 统计标点符号
        text = re.sub(r'！+', '！', text)
        text = re.sub(r'？+', '？', text)

        # 更新统计
        self.stats['chars_before'] += original_len
        self.stats['chars_after'] += len(text)

        return text

    def process_file(self, input_file, output_file):
        """处理文件"""
        try:
            self.log(f"开始处理文件: {input_file}")

            # 读取
            with open(input_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            self.stats['total'] = len(lines)

            # 清洗
            cleaned_lines = []
            for i, line in enumerate(lines, 1):
                cleaned = self.clean_text(line)
                if cleaned:
                    cleaned_lines.append(cleaned + '\n')
                    self.stats['cleaned'] += 1

                if i % 10 == 0:
                    self.log(f"进度: {i}/{len(lines)}")

            # 保存
            with open(output_file, 'w', encoding='utf-8') as f:
                f.writelines(cleaned_lines)

            self.log(f"✓ 处理完成: {output_file}")
            return True

        except FileNotFoundError:
            self.log(f"✗ 文件不存在: {input_file}")
            return False
        except Exception as e:
            self.log(f"✗ 错误: {str(e)}")
            return False

    def get_report(self):
        """生成报告"""
        compression = (1 - self.stats['chars_after'] / self.stats['chars_before']) * 100 if self.stats['chars_before'] > 0 else 0

        report = f"""
{'=' * 70}
文本清洗报告
{'=' * 70}
生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

原始行数: {self.stats['total']}
保留行数: {self.stats['cleaned']}
删除行数: {self.stats['total'] - self.stats['cleaned']}

原始字符数: {self.stats['chars_before']}
清洗后字符数: {self.stats['chars_after']}
减少字符数: {self.stats['chars_before'] - self.stats['chars_after']}
压缩率: {compression:.1f}%

配置:
  去除表情: {self.config['remove_emojis']}
  去除特殊字符: {self.config['remove_special_chars']}
  去除多余空格: {self.config['strip_whitespace']}
{'=' * 70}
"""
        return report

# 主程序
print("=" * 70)
print("文本清洗工具 v3.0 - 完整版(OOP)")
print("=" * 70)

# 创建测试数据
test_data = """你好！！！   我想咨询一下产品信息😊😊
###价格是多少啊？？？   !!!
【客服】：  感谢您的咨询~~~  请问有什么可以帮您的呢？？
   这个产品真的很好用👍👍   推荐购买！！！
@管理员  能给个优惠吗😭😭😭
产品质量不错，服务态度也很好
下次还会再来购买的
已经推荐给朋友了
物流很快，包装也很好
性价比很高，值得购买
"""

with open('dialogues_v3.txt', 'w', encoding='utf-8') as f:
    f.write(test_data)

# 创建清洗器
cleaner = TextCleaner()

# 处理文件
print("\n正在处理...")
success = cleaner.process_file('dialogues_v3.txt', 'dialogues_v3_cleaned.txt')

if success:
    # 输出报告
    print(cleaner.get_report())

    # 显示部分日志
    print("【处理日志】")
    with open(cleaner.log_file, 'r', encoding='utf-8') as f:
        print(f.read())

    print("\n✓ 所有处理完成!")
    print("  - dialogues_v3_cleaned.txt (清洗结果)")
    print("  - cleaner.log (处理日志)")
else:
    print("\n✗ 处理失败，请查看日志")
