"""
Day 1 测评 - 实操题2: 用户信息收集系统
解法3: 完整版 - 数据验证+美化输出
难度: ★★★★☆
适合: 展示生产级代码的完整性
"""

# ============ 知识点 ============
# 1. 输入验证
# 2. 条件判断
# 3. 字符串方法(strip)

# ============ 实战技巧 ============
# 1. 去除输入首尾空格: strip()
# 2. 验证输入的合理性
# 3. 给出友好的提示信息

# ============ 易错点 ============
# 1. 忘记处理空输入
# 2. 年龄范围验证遗漏
# 3. 用户体验不够友好

# ============ 扩展思考 ============
# 1. 如何支持修改已输入的信息？
# 2. 如何保存到文件？
# 3. 如何实现登录验证？

from datetime import datetime

print("=" * 60)
print(" " * 20 + "用户信息收集系统")
print(" " * 22 + "完整版 v1.0")
print("=" * 60)

# 收集用户信息
print("\n请输入您的个人信息(必填项):")
print("-" * 60)

# 姓名输入(去除空格，验证非空)
while True:
    name = input("  姓名: ").strip()
    if name:
        break
    else:
        print("    ❌ 姓名不能为空，请重新输入！")

# 年龄输入(验证范围)
while True:
    try:
        age = int(input("  年龄: "))
        if 1 <= age <= 150:
            break
        else:
            print("    ❌ 年龄必须在1-150之间，请重新输入！")
    except ValueError:
        print("    ❌ 请输入有效的数字！")

# 城市输入
while True:
    city = input("  城市: ").strip()
    if city:
        break
    else:
        print("    ❌ 城市不能为空，请重新输入！")

# 爱好输入
while True:
    hobby = input("  爱好: ").strip()
    if hobby:
        break
    else:
        print("    ❌ 爱好不能为空，请重新输入！")

# 创建用户字典
user_info = {
    "姓名": name,
    "年龄": age,
    "城市": city,
    "爱好": hobby,
    "注册时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

# 美化输出
print("\n" + "=" * 60)
print(" " * 22 + "信息确认")
print("=" * 60)

# 基本信息
print("\n【基本信息】")
print(f"  姓名: {user_info['姓名']}")
print(f"  年龄: {user_info['年龄']}岁", end="")

# 年龄段判断
if age < 18:
    age_group = "(未成年)"
elif age < 60:
    age_group = "(成年人)"
else:
    age_group = "(老年人)"
print(f" {age_group}")

print(f"  城市: {user_info['城市']}")
print(f"  爱好: {user_info['爱好']}")
print(f"  注册时间: {user_info['注册时间']}")

# 统计信息
print("\n【统计信息】")
print(f"  姓名长度: {len(name)}个字符")
print(f"  出生年份: 约{2024 - age}年")

print("\n" + "=" * 60)
print("✓ 信息已成功录入系统！")
print(f"✓ 欢迎您，{name}！")
print("=" * 60)

# 模拟数据总结
print("\n【数据概览】")
print(f"用户ID: {abs(hash(name)) % 100000:05d}")  # 模拟生成ID
print(f"档案完整度: 100%")
print(f"数据质量: 优秀")
