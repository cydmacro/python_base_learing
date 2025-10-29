"""
Day 1 测评 - 实操题1: 简单计算器
解法1: 基础版 - 直接实现
难度: ★☆☆☆☆
适合: 完全按照题目要求，最简单直接的实现
"""

# ============ 知识点 ============
# 1. input()获取用户输入
# 2. float()类型转换
# 3. 四则运算符: +、-、*、/
# 4. print()格式化输出

# ============ 实战技巧 ============
# 1. 一步到位转换类型: float(input())
# 2. 使用f-string格式化输出
# 3. 保留2位小数: :.2f

# ============ 易错点 ============
# 1. 忘记类型转换，直接用字符串计算
# 2. 除法时除数可能为0
# 3. 输出格式不美观

# ============ 扩展思考 ============
# 1. 如何处理除数为0的情况？
# 2. 如何让用户选择运算类型？
# 3. 如何实现连续计算？

print("=" * 50)
print("简单计算器 - 基础版")
print("=" * 50)

# 获取两个数字
num1 = float(input("请输入第一个数字: "))
num2 = float(input("请输入第二个数字: "))

# 计算四则运算结果
add_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2  # 假设除数不为0

# 输出结果
print("\n" + "-" * 50)
print("计算结果:")
print("-" * 50)
print(f"{num1} + {num2} = {add_result:.2f}")
print(f"{num1} - {num2} = {sub_result:.2f}")
print(f"{num1} × {num2} = {mul_result:.2f}")
print(f"{num1} ÷ {num2} = {div_result:.2f}")
print("-" * 50)
