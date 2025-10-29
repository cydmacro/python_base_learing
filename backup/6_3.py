# import os

# # 1.1 获取当前工作目录
# current_dir = os.getcwd()
# print("当前目录:", current_dir)  # 输出：/Users/yourname/projects

# # 1.2 遍历目录下的文件
# files = os.listdir(".")  # 当前目录所有文件和子目录
# print("文件列表:", files)

# # 1.3 路径拼接（跨平台安全）
# file_path = os.path.join("data", "test.txt")  # data/test.txt（Windows自动转反斜杠）

# # 1.4 创建目录（如果不存在）
# if not os.path.exists("backup"):
#     os.makedirs("backup")  # 创建多级目录

# # 1.5 删除文件
# os.remove("1.png")  # 文件不存在会报错



# import json

# # 2.1 字典转JSON字符串
# data = {"name": "小明", "age": 18, "is_student": True}
# json_str = json.dumps(data, ensure_ascii=False)  # 禁用ASCII转码
# print("JSON字符串:", json_str)  # {"name": "小明", "age": 18, "is_student": true}

# # 2.2 JSON字符串转字典
# data_restored = json.loads(json_str)
# print("恢复的字典:", data_restored["name"])  # 小明

# # 2.3 读写JSON文件
# # 写入
# with open("user.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, indent=4)  # 缩进美化

# # 读取
# with open("user.json", "r", encoding="utf-8") as f:
#     loaded_data = json.load(f)
#     print("文件内容:", loaded_data)


# import sys

# # 3.1 获取命令行参数
# # 运行命令：python script.py arg1 arg2
# print("脚本名:", sys.argv[0])     # script.py
# print("第一个参数:", sys.argv[1])  # arg1

# # 3.2 强制退出程序（带状态码）
# if len(sys.argv) < 2:
#     print("缺少参数！")
#     sys.exit(1)  # 非0表示异常退出

# # 3.3 添加自定义模块搜索路径
# sys.path.append("/my_modules")  # 临时添加



# import random

# # 4.1 生成随机整数（包含两端）
# num = random.randint(1, 10)  # 1~10之间的整数
# print("随机数:", num)

# # 4.2 随机选择元素
# fruits = ["苹果", "香蕉", "橘子"]
# choice = random.choice(fruits)  # 随机选一个
# print("随机水果:", choice)  # e.g. 橘子

# # 4.3 打乱列表顺序（原地修改）
# cards = ["A", "2", "3", "J", "Q", "K"]
# random.shuffle(cards)
# print("洗牌后:", cards)  # e.g. ['Q', 'A', '3', ...]

# # 4.4 生成随机验证码（6位字母+数字）
# import string
# chars = string.ascii_letters + string.digits  # 所有字母和数字
# code = ''.join(random.choices(chars, k=6))    # 生成6位
# print("验证码:", code)  # e.g. aB3dE7


import math

# 5.1 计算平方根和幂
a = math.sqrt(25)     # 5.0
b = math.pow(2, 3)    # 8.0
print(f"平方根: {a}, 幂: {b}")

# 5.2 向上/向下取整
c = math.ceil(3.2)    # 4
d = math.floor(3.8)   # 3
print(f"向上取整: {c}, 向下取整: {d}")

# 5.3 常数π和弧度转换
radius = 5
area = math.pi * radius ** 2  # 圆面积公式
degrees = math.degrees(math.pi)  # 180.0
print(f"圆面积: {area:.2f}, 弧度转角度: {degrees}")

# 5.4 对数运算
log_value = math.log(100, 10)  # 以10为底的log(100) → 2.0
print("对数结果:", log_value)