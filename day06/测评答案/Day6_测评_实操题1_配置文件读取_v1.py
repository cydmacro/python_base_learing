"""
Day 6 测评 - 实操题1: 配置文件读取
解法1: 基础版
"""

print("=" * 60)
print("配置文件读取器")
print("=" * 60)

# 1. 创建配置文件
config_content = """name=张三
age=20
city=北京"""

with open('config.txt', 'w', encoding='utf-8') as f:
    f.write(config_content)

print("✓ 配置文件已创建: config.txt")

# 2. 读取文件
print("\n【读取配置文件】")
with open('config.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"读取到 {len(lines)} 行配置")

# 3. 解析为字典格式
config_dict = {}

for line in lines:
    line = line.strip()  # 去除首尾空白
    if '=' in line:
        key, value = line.split('=')
        config_dict[key] = value

# 4. 输出配置信息
print("\n" + "=" * 60)
print("【配置信息】")
print("=" * 60)

for key, value in config_dict.items():
    print(f"{key}: {value}")

print("=" * 60)

# 验证
print("\n【验证】")
print(f"配置项数量: {len(config_dict)}")
print(f"是否包含name: {'name' in config_dict}")
print(f"name的值: {config_dict.get('name', '未设置')}")
