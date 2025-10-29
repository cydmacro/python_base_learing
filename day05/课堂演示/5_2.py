# 定义类
# class Car:
#     wheels = 4  # 类属性

#     def __init__(self, color):
#         self.color = color  # 实例属性

# # ✅ 正确访问
# print(Car.wheels)  # 4 (通过类访问)

# # ✅ 通过实例访问（返回类属性值）
# my_car = Car("red")
# print(my_car.wheels)  # 4 

# # ❗ 危险操作：通过实例"修改"类属性
# my_car.wheels = 5  # 实际创建了实例属性！
# print(my_car.wheels)    # 5 (实例属性)
# print(Car.wheels)       # 4 (类属性未变)

# # ✅ 正确修改类属性
# Car.wheels = 6
# new_car = Car("blue")
# print(new_car.wheels)   # 6 (所有新实例生效)
# print(my_car.wheels)    # 5 (旧实例仍访问自己的实例属性)


# 定义类
# class Student:
#     school = "清华大学"  # 类属性

#     def __init__(self, name):
#         self.name = name  # 实例属性

# # 创建实例
# stu1 = Student("张三")
# stu2 = Student("李四")

# # 修改实例属性
# stu1.name = "王五"  
# print(stu1.name)  # 王五
# print(stu2.name)  # 李四 （不受影响）

# # 动态添加实例属性
# stu1.gpa = 3.8    # 仅为stu1添加新属性
# print(stu1.gpa)   # 3.8
# print(stu2.gpa)   # AttributeError



class Student:
    
    school = "学习python大学" #类属性
    
    def __init__(self, name, age):
        self.name = name #实例属性
        self.age = age 
        self.__secret = "考试没及格" #私有属性
        
    def __update_record(self): #私有方法
        print("更新成绩单")

    def study(self, subject):
        print(f"{self.name}正在学习{subject}")
        self.__update_record() #调用私有方法
        
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
        print(f"学校已改为{cls.school}")
        
    @staticmethod
    def get_school_year():
        return "2030年是校庆年"
    
stu1 = Student("老王", 38)
stu2 = Student("冰冰", 17)

stu1.study("学习python架构大课")

Student.change_school("学习python超级大学")

print(Student.get_school_year())