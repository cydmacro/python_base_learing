#AI⼤模型版-⾼级函数和Lambda实战

# def add(a, b):
#     """ 定义一个函数相加"""
#     r = a +b
#     return r


# result = add(88, 1)
# print(result)


# def modify_num(n):
#     n += 10
#     print("函数内n:", n)  # 20

# num = 10
# modify_num(num)
# print("函数外num:", num)  # 10（未改变）



# def modify_list(lst):
#     lst.append(4)
#     print("函数内lst:", lst)  # [1,2,3,4]

# my_list = [1,2,3]
# modify_list(my_list)
# print("函数外my_list:", my_list)  # [1,2,3,4]（原列表被修改）

# def calculate(a, b):
#     return a + b, a - b, a * b

# sum_result, sub_result, mul_result = calculate(5, 3)
# print(sum_result)  # 8

# def greet(name):
#     print(f"Hello, {name}!")

# result = greet("Alice")  # Hello, Alice!
# print(result)            # None

# a = None
# print(type(a))  # <class 'NoneType'>


# 错误示范：不能直接声明未初始化的变量
#x =  # SyntaxError

# 正确方式必须给初始值（可以是None）
# x = None
# y = [None] * 5  # 创建包含5个None的列表

# print(y)

# def greet(name=None):
#     print(f"Hello, {name or 'Guest'}!")

# greet("老王")  # 输出：Hello, Guest!

# 学生成绩分析器，接收成绩列表，返回最高分、平均分
def analyze_scores(scores):
    """学生成绩分析器，接收成绩列表，返回最高分、平均分"""
    max_score = max(scores)
    avg_score = sum(scores)/len(scores)
    return max_score, avg_score

max_result , avg_result = analyze_scores([80, 95, 72, 100, 88])
print(f"最高分：{max_result}，平均分：{avg_result}")