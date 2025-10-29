# 传统动态类型代码示例
# def calculate(a, b):
#     return a + b  # 无法直观看出参数类型和返回值类型

# result1 = calculate(3, 5)    # ✅ 正确用法
# result2 = calculate("3", 5)  # ❌ 运行时才报错

# age: int = 25                   # 整数类型
# name: str = "Alice"             # 字符串类型
# price: float = 9.99             # 浮点数类型
# is_valid: bool = True           # 布尔类型
# data: bytes = b"binary"         # 字节类型

# print(age, name, price, is_valid, data)

# def add(i:int,a:int)->int:
#     return i+a


# from typing import List, Union
#
# scores: List[int] = [90, 85, 95]                # 整型列表
# matrix: List[List[float]] = [[1.1, 2.2], [3.3]] # 嵌套列表
#
# print(f"scores: {scores}")
# print(f"matrix: {matrix}")
#
# from typing import Dict
#
# person: Dict[str, str] = {"name": "Bob", "job": "dev"}  # 字符串字典
# config: Dict[str, Union[int, str]] = {"timeout": 30,"url":"cydh.net"}     # 混合值类型
#
# print(config )
#
# from typing import Tuple, Union
#
# point: Tuple[float, float] = (3.14, 2.71)           # 二元坐标
# rgb: Tuple[int, int, int] = (255, 0, 128)           # 颜色值
# flexible: Tuple[str, ...] = ("a", "b", "c","d","e")         # 任意长度元组
#
# print(f"point :{point}")
# print(f"rgb :{rgb}")
# print(f"flexible :{flexible}")
#
# from typing import Set
#
# unique_ids: Set[int] = {1, 2, 3}                    # 整型集合
# tags: Set[Union[str, int]] = {"urgent", 1001}       # 混合类型集合
#
# print(f"unique_ids:  {unique_ids}")
# print(f"tags:  {tags}")
#
# from typing import Any
#
# def debug_log(obj: Any) -> None:
#     print(repr(obj))
#
# def greet(name: str) -> str:  # 参数类型 -> 返回值类型
#     return f"Hello, {name}"



# def calculate(a: int, b: int) -> int:
#     print(a,b)
#     return 1

# # 无返回值使用None
# def show_info(info: str) -> None:
#     print(info)

# calculate("age",1)


# from typing import Literal

# HttpMethod = Literal["GET", "POST", "PUT", "DELETE"]

# def send_request(method: HttpMethod, url: str) -> None:
#     print(f"Sending {method} request to {url}")
    
# send_request("PATCH", "https://example.com")



# from typing import Union

# def process_input(value: Union[int, str]) -> None:
#     if isinstance(value, int):
#         print(f"Number: {value}")
#     else:
#         print(f"String: {value}")

# process_input(42)      # Number: 42
# process_input("test")  # String: test


# from typing import Optional
#
# def greet1(name: Optional[str] = None) -> str:
#     if name:
#         return f"Hello, {name}!"
#     else:
#         return "Hello, world!"
#
# def greet2(name: Optional[str]) -> str:
#     if name:
#         return f"Hello, {name}!"
#     else:
#         return "Hello, world!"
#
# print(greet1())
# #print(greet2()) # 报错，必须要有参数 可以传 None
# print(greet1("老王"))
# print(greet2("冰冰"))


from typing import Tuple, List

# 基本别名
# UserId = int
# Point = Tuple[float, float]
#
#
# def get_user(id: UserId) -> str:
#     return f"User{id}"
#
# def plot(points: List[Point]) -> None:
#     for x, y in points:
#         print(f"({x}, {y})")


if __name__ == '__main__':
    my_tuple =1, "hello", True  # 这同样会创建一个元组
    print(type(my_tuple))  # <class 'tuple'>

# from typing import NewType

# # 创建强类型
# UserId = NewType('UserId', int)
# admin_id = UserId(1001)

# def print_id(user_id: UserId) -> None:
#     print(user_id)

# # 正确调用
# print_id(admin_id)        # ✅
# print_id(1001)            # ❌ mypy报错


# from typing import TypeVar, Sequence

# T = TypeVar('T')  # 无约束类型
# Num = TypeVar('Num', int, float)  # 受限类型

# def first(items: Sequence[T]) -> T:
#     return items[0]

# def sum(values: Sequence[Num]) -> Num:
#     return sum(values)


# from typing import TypeVar
#
# # 定义一个泛型变量T
# T = TypeVar('T')
#
# # 创建一个泛型函数
# def get_first_item(items: list[T]) -> T:
#     """获取列表的第一个元素"""
#     if items:
#         return items[0]
#     raise ValueError("列表为空")
#
# # 使用示例
# numbers = [1, 2, 3, 4, 5]
# words = ['apple', 'banana', 'cherry', 'fruit']
#
# print(get_first_item(numbers))  # 输出: 1
# print(get_first_item(words))    # 输出: apple