# class Animal:  # 基类/父类
#     def __init__(self, name):
#         self.name = name
        
#     def speak(self):
#         raise NotImplementedError("子类必须实现此方法")

# class Dog(Animal):  # 派生类/子类
#     def speak(self):  # 方法重写
#         print("老王不是狗,但是叫 wang")
#         return "汪汪！"

# class Cat(Animal):
#     def speak(self):
#         print("老王不是猫，但是叫 miao")
#         return "喵～"
    
    
# dog = Dog("旺财")
# dog.speak()

# cat = Cat("小花")
# cat.speak()

# class Vehicle:
#     def run(self):
#         print("交通工具运行中...")

# class Car(Vehicle):
#     def run(self):  # 完全重写
#         print("汽车在公路上行驶")

# v = Vehicle()
# v.run()  # 交通工具运行中...
# c = Car()
# c.run()  # 汽车在公路上行驶


# class Phone:
#     def __init__(self, brand):
#         self.brand = brand
        
#     def call(self, number):
#         print(f"{self.brand}手机拨打：{number}")

# class SmartPhone(Phone):
#     def __init__(self, brand, os):
#         super().__init__(brand)  # 调用父类构造
#         self.os = os
        
#     def call(self, number):
#         super().call(number)  # 重用父类方法
#         print("正在使用网络通话功能")

# sp = SmartPhone("华为", "HarmonyOS")
# sp.call("13800138000")


from abc import ABC, abstractmethod

#Shape是一个抽象基类，area是一个抽象方法。因为Shape继承了ABC，
#且area方法使用了@abstractmethod装饰器，所以Shape不能被实例化，子类必须实现area方法

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

# 尝试实例化抽象类会报错
# s = Shape()  # TypeError
c = Circle(5)
print(c.area())  # 78.5

