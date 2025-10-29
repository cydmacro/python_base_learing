# def greet():
#     print("Hello, World!")
#     print("Welcome to Python! 学习python")
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

