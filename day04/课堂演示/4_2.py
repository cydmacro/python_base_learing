# def greet(name, message):
#     print(f"{message}, {name}!")

# greet("Alice", "Hello")  # Hello, Alice!

# greet(message="Hi", name="Bob")  # Hi, Bob!


# def register(name, age=18, city="北京"):
#     print(f"姓名：{name}, 年龄：{age}, 城市：{city}")

# register("小明")              # 年龄和城市使用默认值
# register("小红", 20, "上海")   # 覆盖默认值


# def sum_numbers(*args):
#     return sum(args)

# result = sum_numbers(1,2)
# print(result)
    
    
# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_info(name="Alice", age=25)
# 输出：
# name: Alice
# age: 25


# def add(a, b, c):
#     return a + b + c

# numbers = [1, 2, 3]
# print(add(*numbers))  # 6（等价于 add(1,2,3)）

# def greet(name, message):
#     print(f"{message}, {name}!")

# params = {"name": "Alice", "message": "Hello"}
# greet(**params)  # Hello, Alice!


# def complex_func(a, b, c=0, *args, **kwargs):
#     print("a:", a)
#     print("b:", b)
#     print("c:", c)
#     print("args:", args)
#     print("kwargs:", kwargs)

# complex_func(1, 2, 3, 4, 5, name="Alice", age=25)
# 输出：
# a: 1
# b: 2
# c: 3
# args: (4,5)
# kwargs: {'name': 'Alice', 'age':25}

def build_sql(table, **conditions):
    query = f"SELECT * FROM {table}"
    if conditions:
        where_clause = " AND ".join([f"{key} = '{value}'" for key, value in conditions.items()])
        query += f" WHERE {where_clause}"
    return query

print(build_sql("users", name="Alice", age=25))
# SELECT * FROM users WHERE name = 'Alice' AND age = '25'

