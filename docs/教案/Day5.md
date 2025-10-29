### 第五章 AI大模型版-Python异常处理和OOP编程



#### 第1集 异常处理Try-Except语法案例实战

**简介：  异常处理Try-Except语法案例实战**

* 为什么需要异常处理

  * **避免程序崩溃**：处理运行时错误（如文件不存在、网络中断），提升健壮性。
  * **提供友好提示**：将错误信息转换为用户易懂的内容。
  * **资源清理**：确保文件、网络连接等资源正确释放

* 基本语法

  ```
  try:
      # 可能引发异常的代码
      代码块
  except 异常类型1:
      # 处理异常类型1
      代码块
  except 异常类型2 as e:
      # 处理异常类型2，并获取异常对象e
      代码块
  else:
      # 未发生异常时执行的代码
      代码块
  finally:
      # 无论是否异常，最后都会执行的代码（如资源清理）
      代码块
  
  ```

* 常见异常类型

  |      异常类型       |    触发场景    |       示例代码        |
  | :-----------------: | :------------: | :-------------------: |
  | `ZeroDivisionError` |     除以零     |       `10 / 0`        |
  | `FileNotFoundError` |   文件不存在   | `open("missing.txt")` |
  |    `ValueError`     |  类型转换失败  |     `int("abc")`      |
  |    `IndexError`     |    索引越界    |  `lst = [1]; lst[2]`  |
  |     `KeyError`      |  字典键不存在  | `d = {"a":1}; d["b"]` |
  |     `TypeError`     | 操作类型不匹配 |       `"a" + 1`       |

* 案例实战

  * 基础异常捕获

    ```
    try:
        num = int(input("请输入一个数字："))
        result = 100 / num
        print(result)
    except ValueError:
        print("请输入数字！")
    except ZeroDivisionError:
        print("除数不能为0！")
    except Exception as e:
        print("未知错误：", e)
    else:
        print("没有异常发生！")
    finally:
        print("无论是否发生异常，都会执行！")
    ```

  * 捕获多个异常

    ```
    try:
        with open("data.txt", "r") as f:
            content = f.read()
    except (FileNotFoundError, PermissionError) as e:
        print(f"文件操作失败：{e}")
    ```

* 自定义异常类

  ```
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
  
  ```

  









#### 第2集 Python面向对象编程OOP编程语法

**简介：  Python面向对象编程OOP编程语法**

* Python的面向对象OOP

  * 基本结构

  ```
  class 类名:
      """类文档字符串"""
      
      #定义基本属性， 类属性 = 初始值 ，所有实例共享，类似java的static静态变量
      name = "张三的电脑"
  
      #定义私有属性,私有属性在类外部无法直接进行访问，采用 __ 进行表示, 如果方法开头是__ 表示私有方法
      __weight = 0
      
      def __init__(self, 参数1, 参数2):  # 构造方法
          self.实例属性1 = 参数1
          self.实例属性2 = 参数2
      
      def 实例方法(self):
          """方法文档字符串"""
          return self.实例属性1
      
      #类方法，由哪一个类调用的方法，方法内的cls就是哪一个类的引用
      @classmethod
      def 类方法(cls):
          return cls.类属性
      
      #静态方法，参数随意，没有“self”和“cls”参数，但是方法体中不能使用实例的任何属性和方法
      @staticmethod
      def 静态方法():
          return "与类和实例无关"
  
  ```

  * 类有一个名为 `__init__(self)` 的特殊方法（和Java的构造函数类似）

    * 该方法在类实例化时会自动调用，默认是无参构造函数
    * 可以有参数，参数通过 `__init__(self,param1,param2)`  传递到类的实例化

  * `self` 代表类的实例，而非类,和Java中的 this类似 

    * 当定义一个类，并在类中定义方法时，第一个参数通常被命名为 self，尽管可以使用其他名称
    * 方法中需要传递self才可以使用成员变量
    * 它是一个指向实例的引用，使得类的方法能够访问和操作实例的属性。

  * 属性区别（类属性、实例属性）

    * 案例代码

    ```
    class Dog:
        # 类属性（所有实例共享）
        species = "Canis familiaris"
    
        def __init__(self, name, age):
            # 实例属性（每个对象独立）
            self.name = name
            self.age = age
    ```

    * 核心对比

    |   **特征**   |         **类属性**         |          **实例属性**          |
    | :----------: | :------------------------: | :----------------------------: |
    | **存储位置** |   类内部定义，类自身维护   | `__init__`中定义，实例独立存储 |
    |  **共享性**  |    所有实例共享同一份值    |      每个实例拥有独立副本      |
    | **修改影响** | 修改后，所有实例访问到新值 |       修改仅影响当前实例       |
    | **内存占用** |      全类共用1份内存       |      每个实例单独占用内存      |
    | **典型用途** |   常量、计数器、全局配置   |         对象个性化数据         |

    * 类属性操作

    ```
    # 定义类
    class Car:
        wheels = 4  # 类属性
    
        def __init__(self, color):
            self.color = color  # 实例属性
    
    # ✅ 正确访问
    print(Car.wheels)  # 4 (通过类访问)
    
    # ✅ 通过实例访问（返回类属性值）
    my_car = Car("red")
    print(my_car.wheels)  # 4 
    
    # ❗ 危险操作：通过实例"修改"类属性
    my_car.wheels = 5  # 实际创建了实例属性！
    print(my_car.wheels)    # 5 (实例属性)
    print(Car.wheels)       # 4 (类属性未变)
    
    # ✅ 正确修改类属性
    Car.wheels = 6
    new_car = Car("blue")
    print(new_car.wheels)   # 6 (所有新实例生效)
    print(my_car.wheels)    # 5 (旧实例仍访问自己的实例属性)
    ```

    * 实例属性操作

    ```
    # 定义类
    class Student:
        school = "清华大学"  # 类属性
    
        def __init__(self, name):
            self.name = name  # 实例属性
    
    # 创建实例
    stu1 = Student("张三")
    stu2 = Student("李四")
    
    # 修改实例属性
    stu1.name = "王五"  
    print(stu1.name)  # 王五
    print(stu2.name)  # 李四 （不受影响）
    
    # 动态添加实例属性
    stu1.gpa = 3.8    # 仅为stu1添加新属性
    print(stu1.gpa)   # 3.8
    print(stu2.gpa)   # AttributeError
    ```

    

  * 完整案例：学生类

  ```
  class Student:
      school = "清华大学"  # 类属性，所有实例属性共享
      
      def __init__(self, name, age):
          self.name = name  # 实例属性
          self.age = age
          self.__secret = "考试没及格"  # 私有属性
          
      def study(self, subject):
          print(f"{self.name}正在学习{subject}")
          self.__update_record()  # 调用私有方法
          
      def __update_record(self):  # 私有方法
          print("学习记录已更新")
          
      @classmethod
      def change_school(cls, new_school):
          cls.school = new_school
          print(f"学校已变更为{new_school}")
          
      @staticmethod
      def get_school_year():
          return "2023-2024学年"
  
  # 使用示例
  stu1 = Student("张三", 20)
  stu1.study("Python")  # 张三正在学习Python → 学习记录已更新
  Student.change_school("北京大学")  # 修改类属性
  print(Student.get_school_year())  # 2023-2024学年
  ```

  









#### 第3集 OOP编程进阶和综合案例实战

**简介：  OOP编程进阶和综合案例实战**

* 多个方法对比

  | 方法类型 |    装饰器     | 第一个参数 |       访问权限       |       典型应用场景       |
  | :------: | :-----------: | :--------: | :------------------: | :----------------------: |
  | 实例方法 |      无       |    self    |   实例属性和类属性   |    对象的具体行为实现    |
  |  类方法  | @classmethod  |    cls     |    只能访问类属性    |   工厂方法、操作类属性   |
  | 静态方法 | @staticmethod |     无     | 不能访问实例和类属性 | 工具函数、与类相关的计算 |

* 类方法深度案例

  ```
  class Date:
      def __init__(self, year, month, day):
          self.year = year
          self.month = month
          self.day = day
      
      @classmethod
      def from_string(cls, date_str):
          """工厂方法：从'YYYY-MM-DD'字符串创建实例"""
          year, month, day = map(int, date_str.split('-'))
          return cls(year, month, day)
      
      @classmethod
      def get_current_date(cls):
          """获取当前日期（演示类方法访问类属性）"""
          import datetime
          now = datetime.datetime.now()
          return cls(now.year, now.month, now.day)
  
  d1 = Date.from_string('2023-09-15')
  d2 = Date.get_current_date()
  print(f"{d2.year}-{d2.month}-{d2.day}")  # 输出当前日期
  
  ```

* 静态方法深度案例

  ```
  class MathUtils:
      
      @staticmethod
      def is_prime(num):
          """判断质数（工具方法）"""
          if num < 2:
              return False
          for i in range(2, int(num**0.5)+1):
              if num % i == 0:
                  return False
          return True
  
  
  print(MathUtils.is_prime(17))  # True
  ```

* cls方法拓展

  * python中cls代表的是类的本身，相对应的self则是类的一个实例对象。
  * cls等同于类本身，类方法中可以通过使用cls来实例化一个对象。

  ```
  class Person(object):
      def __init__(self, name, age):
          self.name = name
          self.age = age
          print('self:', self)
  
      # 定义build方法，返回一个person实例对象，这个方法等价于Person()。
      @classmethod
      def build(cls):
          # cls()等于Person()
          p = cls("老王八", 18)
          print('cls:', cls)
          return p
  
  person = Person.build()
  print(person, person.name, person.age)
  ```

  

* 综合案例：学生管理系统

  ```
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
  
  ```

  



















#### 第4集 OOP编程的继承和抽象方法-重写实战

**简介：  OOP编程的继承和方法重写案例实战**

* Python面向对象编程里面的继承

  * **代码复用**：子类自动获得父类非私有属性和方法
  * **扩展性**：子类可以添加新属性和方法
  * **多态基础**：不同子类对同一方法的不同实现
  * 语法特点

  ```
  class ParentClass: 
      # 父类定义
      pass
  
  class ChildClass(ParentClass):  # 继承语法
      # 子类定义
      pass
  ```

  

  <img src="./%E7%AC%AC%E4%BA%94%E7%AB%A0.assets/image-20250226192931778.png" alt="image-20250226192931778" style="zoom:50%;" />

  ```
  class Animal:  # 基类/父类
      def __init__(self, name):
          self.name = name
          
      def speak(self):
          raise NotImplementedError("子类必须实现此方法")
  
  class Dog(Animal):  # 派生类/子类
      def speak(self):  # 方法重写
          return "汪汪！"
  
  class Cat(Animal):
      def speak(self):
          return "喵～"
  ```

* 方法重写

  * 完全重写案例

  ```
  class Vehicle:
      def run(self):
          print("交通工具运行中...")
  
  class Car(Vehicle):
      def run(self):  # 完全重写
          print("汽车在公路上行驶")
  
  v = Vehicle()
  v.run()  # 交通工具运行中...
  c = Car()
  c.run()  # 汽车在公路上行驶
  ```

  * 扩展式重写（使用super()）

  ```
  class Phone:
      def __init__(self, brand):
          self.brand = brand
          
      def call(self, number):
          print(f"{self.brand}手机拨打：{number}")
  
  class SmartPhone(Phone):
      def __init__(self, brand, os):
          super().__init__(brand)  # 调用父类构造
          self.os = os
          
      def call(self, number):
          super().call(number)  # 重用父类方法
          print("正在使用网络通话功能")
  
  sp = SmartPhone("华为", "HarmonyOS")
  sp.call("13800138000")
  # 输出：
  # 华为手机拨打：13800138000
  # 正在使用网络通话功能
  ```

* super()工作原理

  ```
  class Base:
      def __init__(self):
          print("Base初始化")
  
  class A(Base):
      def __init__(self):
          super().__init__()
          print("A初始化")
  
  class B(Base):
      def __init__(self):
          super().__init__()
          print("B初始化")
  
  class C(A, B):
      def __init__(self):
          super().__init__()
          print("C初始化")
  
  c = C()
  # 输出顺序：
  # Base初始化
  # B初始化
  # A初始化
  # C初始化
  
  ```

* 抽象类和抽象方法

  * 抽象基类
    * Abstract Base Class，简称 ABC， 抽象基类是一种不能被实例化的类，主要作用是为其他子类定义一个公共的接口
  * 抽象方法
    * 抽象方法是定义在抽象基类中的方法，它只有方法签名，没有具体的实现。
    * 子类必须重写抽象方法并提供具体的实现

  ```
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
  
  ```

  

