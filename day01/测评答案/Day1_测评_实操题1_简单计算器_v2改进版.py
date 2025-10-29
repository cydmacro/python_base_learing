"""
Day 1 测评 - 实操题1: 简单计算器
解法2: 改进版 - 添加异常处理
难度: ★★☆☆☆
适合: 展示如何处理除数为0的情况
"""

# ============ 知识点 ============
# 1. 条件判断(if-else)
# 2. 除数为0的处理
# 3. 三元运算符的使用

# ============ 实战技巧 ============
# 1. 除法前先判断除数是否为0
# 2. 使用三元运算符简化代码
# 3. 给出友好的错误提示

# ============ 易错点 ============
# 1. 判断浮点数是否为0要小心精度问题
# 2. 错误信息要清晰明了

# ============ 扩展思考 ============
# 1. 如何处理非数字输入？
# 2. 如何支持更多运算（乘方、开方）？

print("=" * 50)
print("简单计算器 - 改进版(含异常处理)")
print("=" * 50)

# 获取两个数字
num1 = float(input("请输入第一个数字: "))
num2 = float(input("请输入第二个数字: "))

# 计算结果
add_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2

# 除法特殊处理
if num2 != 0:
    div_result = num1 / num2
    div_status = "正常"
else:
    div_result = "错误"
    div_status = "除数不能为0"

# 输出结果
print("\n" + "-" * 50)
print("计算结果:")
print("-" * 50)
print(f"{num1} + {num2} = {add_result:.2f}")
print(f"{num1} - {num2} = {sub_result:.2f}")
print(f"{num1} × {num2} = {mul_result:.2f}")

if div_result == "错误":
    print(f"{num1} ÷ {num2} = {div_result} ({div_status})")
else:
    print(f"{num1} ÷ {num2} = {div_result:.2f}")

print("-" * 50)

# 使用三元运算符的简洁写法（进阶）
print("\n【进阶写法 - 三元运算符】")
div_display = f"{div_result:.2f}" if num2 != 0 else "错误(除数为0)"
print(f"除法结果: {div_display}")
