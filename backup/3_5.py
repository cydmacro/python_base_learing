# # 验证可迭代对象  
# from collections.abc import Iterable

# print(isinstance([1,2,3], Iterable))  # True
# print(isinstance("hello", Iterable))  # True
# print(isinstance(123, Iterable))      # False

# # isinstance(object, classinfo) 判断一个对象是否为指定类型或指定类型的子类
# # 使用元组传递多个类型，如果对象是其中任意一个类型的实例，则返回 `True`。
# print(isinstance(10, (int, str)))  # 输出：True


# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# for x in it:
#     print (x, end=" ")

# 手动使用迭代器
numbers = [1, 2, 3]
iterator = iter(numbers)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
print(next(iterator))  # 抛出StopIteration异常