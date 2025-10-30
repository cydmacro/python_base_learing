#AI⼤模型版-Python异常处理和OOP编程

# try:
#     num = int(input("请输入一个数字："))
#     result = 100 / num
#     print(result)
# except ValueError:
#     print("请输入数字！")
# except ZeroDivisionError:
#     print("除数不能为0！")
# except Exception as e:
#     print("未知错误：", e)
# else:
#     print("没有异常发生！")
# finally:
#     print("无论是否发生异常，都会执行！")



try:
    with open("/daata/test.txt", "r") as f:
        content = f.read()
except (FileNotFoundError, PermissionError) as e:
    print(f"文件操作失败：{e}")

class InvalidAgeError(Exception):
    """年龄无效异常"""
    def __init__(self, age):
        self.age = age
        super().__init__(f"年龄{age}无效，必须大于0！")

def set_age(age):
    if age <= 0:
        raise InvalidAgeError(age)
    print("年龄设置成功：", age)

# 测试
try:
    set_age(-5)
except InvalidAgeError as e:
    print(e)  # 输出：年龄-5无效，必须大于0！




   