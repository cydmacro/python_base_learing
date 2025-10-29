"""
Day 6 测评 - 实操题2: 数据处理日志系统
解法1: 基础版 - 完整的文件处理+异常处理+日志
"""

from datetime import datetime

def log_message(message, log_file='log.txt'):
    """写入日志"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {message}\n")


print("=" * 60)
print("数据处理日志系统")
print("=" * 60)

# 清空日志文件
with open('log.txt', 'w', encoding='utf-8') as f:
    f.write("")

log_message("程序启动")

try:
    # 1. 创建测试数据文件
    test_data = """张三,85
李四,92
王五,78
赵六,88"""

    with open('student_scores.txt', 'w', encoding='utf-8') as f:
        f.write(test_data)

    log_message("✓ 测试数据文件创建成功")
    print("✓ 测试数据文件已创建")

    # 2. 读取文件
    log_message("开始读取student_scores.txt")

    with open('student_scores.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    log_message(f"✓ 成功读取 {len(lines)} 条记录")

    # 3. 计算平均分
    scores = []
    for line in lines:
        try:
            name, score_str = line.strip().split(',')
            score = int(score_str)
            scores.append(score)
        except ValueError as e:
            log_message(f"✗ 数据格式错误: {line.strip()} - {str(e)}")
            continue

    average = sum(scores) / len(scores)
    log_message(f"✓ 平均分计算完成: {average:.2f}")

    # 4. 将结果写入report.txt
    report_content = f"""学生成绩分析报告
生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

总人数: {len(scores)}
平均分: {average:.2f}
最高分: {max(scores)}
最低分: {min(scores)}

详细数据:
"""

    for line in lines:
        name, score = line.strip().split(',')
        report_content += f"  {name}: {score}分\n"

    with open('report.txt', 'w', encoding='utf-8') as f:
        f.write(report_content)

    log_message("✓ 报告文件生成成功: report.txt")
    print("✓ 报告已生成: report.txt")

except FileNotFoundError:
    log_message("✗ 错误: 文件不存在")
    print("✗ 错误: 找不到数据文件")
except ValueError as e:
    log_message(f"✗ 数据格式错误: {str(e)}")
    print(f"✗ 数据格式错误: {str(e)}")
except Exception as e:
    log_message(f"✗ 未知错误: {str(e)}")
    print(f"✗ 发生错误: {str(e)}")
finally:
    log_message("程序结束")

# 显示日志内容
print("\n" + "=" * 60)
print("【处理日志】")
print("=" * 60)

with open('log.txt', 'r', encoding='utf-8') as f:
    print(f.read())

print("=" * 60)
print("\n✓ 所有文件处理完成!")
print("  - student_scores.txt (原始数据)")
print("  - report.txt (分析报告)")
print("  - log.txt (处理日志)")
