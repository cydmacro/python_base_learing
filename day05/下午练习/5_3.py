# # class Date:
# #     def __init__(self, year, month, day):
# #         self.year = year
# #         self.month = month
# #         self.day = day
# #         print("__init__方法被调用")
    
# #     @classmethod
# #     def from_string(cls, date_str):
# #         """工厂方法：从'YYYY-MM-DD'字符串创建实例"""
# #         year, month, day = map(int, date_str.split('-'))
# #         return cls(year, month, day)
    
# #     @classmethod
# #     def get_current_date(cls):
# #         """获取当前日期（演示类方法访问类属性）"""
# #         import datetime
# #         now = datetime.datetime.now()
# #         return cls(now.year, now.month, now.day)

# # d1 = Date.from_string('2023-09-15')
# # d2 = Date.get_current_date()
# # print(f"{d1.year}-{d1.month}-{d1.day}")  # 输出指定日期的格式

# # print(f"{d2.year}-{d2.month}-{d2.day}")  # 输出当前日期

# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('self:', self)

#     # 定义build方法，返回一个person实例对象，这个方法等价于Person()。
#     @classmethod
#     def build(cls):
#         # cls()等于Person()
#         p = cls("老王八", 18)
#         print('cls:', cls)
#         return p

# person = Person.build()
# print(person, person.name, person.age)




# 魔术方法__repr__和__str__，在打印对象时能够获得对象的当前状态信息
# 如果一个类没有定义__str__方法，Python解释器会调用内置的__repr__方法来获取对象的字符串表示。
# 如果也没有定义__repr__方法 即 representation，Python会使用默认的字符串表示形式，即返回对象在计算机内存中的实际地址。


class StudentManager:
    __students = []  # 私有类属性
    
    def __init__(self, name):
        self.manager_name = name
    
    def add_student(self, student):
        self.__students.append(student)
        print(f"{student} 已添加")
    
    @classmethod
    def get_student_count(cls):
        return len(cls.__students)
    
    @staticmethod
    def validate_age(age):
        return 15 <= age <= 60
    
    def __str__(self):
        return f"管理员：{self.manager_name}，管理学生数：{len(self.__students)}"

class Student:
    def __init__(self, name, age):
        if not StudentManager.validate_age(age):
            raise ValueError("无效年龄")
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"<Student {self.name}>"

# 使用示例
mgr = StudentManager("王老师")
try:
    s1 = Student("张三", 18)
    mgr.add_student(s1)  # <Student 张三> 已添加
    s2 = Student("李四", 12)  # ValueError: 无效年龄
except ValueError as e:
    print(e)

print(mgr)  # 管理员：王老师，管理学生数：1
print(StudentManager.get_student_count())  # 1

