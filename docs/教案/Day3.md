### 第三章 AI大模型版-逻辑判断和多种高级循环实战



#### 第1集 Python逻辑判断和比较运算符

**简介：  Python逻辑判断和比较运算符**

* 比较运算符

  | 运算符 |   说明   |       示例       |
  | :----: | :------: | :--------------: |
  |  `==`  |   等于   | `5 == 5 → True`  |
  |  `!=`  |  不等于  | `3 != 5 → True`  |
  |  `>`   |   大于   | `10 > 5 → True`  |
  |  `<`   |   小于   | `3 < 2 → False`  |
  |  `>=`  | 大于等于 | `5 >= 5 → True`  |
  |  `<=`  | 小于等于 | `4 <= 3 → False` |

  * 注意点
    * 避免混淆赋值符：=用于赋值，==用于比较。
    * 链式比较：Python支持链式表达式 1 < x < 5（等价于 x>1 and x<5）

* 逻辑运算符

  * 优先级：not > and > or
    * 可通过括号()明确优先级：
  * 短路求值（Short-Circuiting）
    * 规则
      - `and`：若左侧为假，直接返回假，不计算右侧。
      - `or`：若左侧为真，直接返回真，不计算右侧。

  | 运算符 |        说明        |           示例            |
  | :----: | :----------------: | :-----------------------: |
  | `and`  | 逻辑与（全真为真） | `(5>3) and (2<1) → False` |
  |  `or`  | 逻辑或（一真即真） |  `(5>3) or (2<1) → True`  |
  | `not`  |       逻辑非       |    `not (5>3) → False`    |

* 条件表达式（三元运算符）

  * 语法：结果1 if 条件 else 结果2

  ```
  # 返回两个数中的较大值
  a, b = 5, 10
  max_value = a if a > b else b  # 10
  ```

* 条件语句（if-elif-else）

  * **执行顺序**：从上到下判断条件，满足即执行对应代码块，后续条件不再判断。

  * 基本语法

    ```
    if 条件1:
        代码块1
    elif 条件2:
        代码块2
    else:
        代码块3
    ```

  * 案例代码

    ```
    # 判断成绩等级
    score = 85
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")  # 输出B
    else:
        print("C")
    ```

  

  













#### 第2集 Python常见循环语法和循环控制语句

**简介：  Python常见循环语法和循环控制语句**

* for循环基础

  * 语法

    ```
    for 变量 in 可迭代对象:
        循环体代码
    ```

  * 案例练习

    * 遍历列表

      ```
      teachers = ["哈哈", "张三", "jack"]
      for t in teachers:
          print(f"小明 love  {t}!")
      
      # 输出：
      # 小明 love  哈哈!
      # 小明 love  张三!
      # 小明 love  jack!
      ```

    * 遍历字符串

      ```
      word = "张三"
      for char in word:
          print(char.upper(), end=" ")  # 张三
      ```

    * 遍历字典

      ```
      # 遍历字典
      dict1 = {"Monday": "星期一", "Tuesday": "星期二"}
      for key in dict1.keys():
          print(key)  # 输出字典的键
      ```

    * 结合range函数 生成整数序列

      ```
      for j in range(1, 5):
          print(j)  # 输出1,2,3,4
      ```

      

* while循环基础

  * 语法

    ```
    while 条件表达式:
        循环体代码
    ```

  * 案例练习

    * 计数器

    ```
    count = 0
    while count < 5:
        print(f"Count: {count}")
        count += 1
    
    # 输出：
    # Count: 0
    # Count: 1
    # ...
    # Count: 4
    
    ```

    * 用户输入验证

    ```
    password = ""
    while password != "secret123":
        password = input("Enter password: ")
    print("Access granted!")
    ```

* 循环控制语句

  * break：立即终止循环

  ```
  for num in range(10):
      if num == 5:
          break
      print(num)  # 输出0-4
  ```

  * continue：跳过当前迭代

  ```
  for num in range(10):
      if num % 2 == 0:
          continue
      print(num)  # 输出1,3,5,7,9
  ```

  









#### 第3集 Python高级for循环列表推导式案例实战

**简介：  Python高级for循环语法和案例实战**

* 什么是推导式

  * 是一种独特的数据处理方式，从一个数据序列构建另一个新的数据序列的结构体。
  * 是一种强大且简洁的语法，适用于生成列表、字典、集合和生成器。
  * 使用推导式时，需要注意可读性，尽量保持表达式简洁，以免影响代码的可读性和可维护性
  * Python支持多种推导式
    - 列表(list)推导式
    - 字典(dict)推导式
    - 集合(set)推导式
    - 元组(tuple)推导式

* 列表推导式（List Comprehensions）

  * 核心作用

    * 快速创建列表，替代传统for循环，具有简洁高效的特点。
    * 用于 从 一个现有的列表 创建 一个新列表 , 使用一行代码 即可 实现 循环 或 条件逻辑 , 生成新的List列表

  * 基础语法 `[expression for item in iterable]`

    * 案例：生成1-10的平方列表

    ```
    squares = [x**2 for x in range(1, 11)]
    print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    ```

  * 条件过滤 语法  `new_list = [expression for item in iterable if condition] `

    * 等价于

      ```
      new_list = []
      for item in iterable:
        if condition:
           expression
      ```

    * 参数说明

      * iterable 参数 : 一个现有的列表 , 可以迭代的对象 , 比如 列表、元组、字符串等 ;
      * condition 参数 : 
        * 可选条件表达式 , 用于过滤 iterable 中的元素 , 
        * iterable 列表中只有满足 该条件的元素 , 才会被作为 item 参与 expression 表达式计算 ;
      * item 参数 :
        * 如果没有 condition 参数 , 那 item 就是 iterable 列表中的每一个元素 ;
        * **如果 有 condition 参数 , 那么 item 就是 iterable 列表中 符合 condition 条件 的元素 **
      * expression 参数 : item 参与计算的 表达式 , 其中有 item 变量 ;

    * 案例：筛选偶数

    ```
    evens = [x for x in range(20) if x % 2 == 0]
    print(evens)  # [0, 2, 4, ..., 18]
    ```

    

  * 条件表达式语法 `[expression1 if condition else expression2 for item in iterable]` 结合三目运算符

    * 案例：数值转换

    ```
    nums = [12, -5, 8, -3, 0]
    abs_nums = [x if x >= 0 else -x for x in nums]
    print(abs_nums)  # [12, 5, 8, 3, 0]
    ```

  

* 作业案例

  * 考试成绩转换，转换为等级制（80分以上为A，其他为B）

  ```
  # 原始成绩列表
  scores = [78, 92, 65, 88, 54]
  
  # 转换为等级制（80分以上为A，其他为B）
  grades = ['A' if score >=80 else 'B' for score in scores]
  print(grades)  # 输出：['B', 'A', 'B', 'A', 'B']
  ```

  









#### 第4集 Python高级推导式字典-元组-集合

**简介：  Python高级推导式字典-元组-集合**

* 字典推导

  * 语法结构详解 `{ 键表达式: 值表达式 for 循环变量 in 可迭代对象 [if 条件] }`

  * 注意

    - 键必须唯一且不可变
    - 值可以是任意类型

  * 案例

    * **键值转换**

    ```
    # 反转字典的键值对
    original = {'a': 1, 'b': 2, 'c': 3}
    reversed_dict = {v: k for k, v in original.items()}
    print(reversed_dict)  # {1: 'a', 2: 'b', 3: 'c'}
    ```

    * **复杂数据重组**

    ```
    students = [
        {'name': 'Alice', 'math': 85, 'english': 90},
        {'name': 'Bob', 'math': 78, 'english': 82},
        {'name': 'Charlie', 'math': 92, 'english': 88}
    ]
    
    # 创建学科分数字典
    math_scores = {stu['name']: stu['math'] for stu in students}
    print(math_scores)  # {'Alice':85, 'Bob':78, 'Charlie':92}
    ```

* 集合推导式

  * 语法结构详解 `{ 表达式 for 循环变量 in 可迭代对象 [if 条件] }`

  * 注意

    * 自动去重
    * 元素无序
    * 元素必须可哈希

  * 案例

    * **交集和并集案例**

    ```
    A = {1, 2, 3}
    B = {3, 4, 5}
    
    # 并集
    union = {x for x in A | B}  # {1,2,3,4,5}
    
    # 交集
    intersection = {x for x in A if x in B}  # {3}
    
    ```

    * **数据去重**

    ```
    words = ['apple', 'banana', 'apple', 'orange', 'banana']
    unique_words = {word.upper() for word in words}
    print(unique_words)  # {'APPLE', 'BANANA', 'ORANGE'}
    ```

    * **特征提取**

    ```
    text = "The quick brown fox jumps over the lazy dog"
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # 提取文本中的唯一元音字母
    found_vowels = {char.lower() for char in text if char.lower() in vowels}
    print(found_vowels)  # {'a', 'e', 'i', 'o', 'u'}
    ```

* 元组表达式

  * 语法结构详解 `( 表达式 for 循环变量 in 可迭代对象 [if 条件] )`

  * 元组推导式和列表推导式的用法相同，只是元组推导式是用 **()** 圆括号将各部分括起来，列表推导式用的是中括号 [ ]

  * 元组推导式返回的结果是一个生成器对象， 所以“元组推导式"实际上是生成器表达式

  * 注意

    * 惰性求值（按需生成）
    * 内存效率高
    * 只能迭代一次

  * 案例

    * 生成一个包含数字 1~9 的元组

    ```
    a = (x for x in range(1,10)) # 返回的a是生成器对象
    
    tuple(a)       # 使用 tuple()函数，将生成器对象转换成元组
    (1, 2, 3, 4, 5, 6, 7, 8, 9)
    ```

    













#### 第5集 Python迭代器介绍和常见方法讲解

**简介：  Python迭代器介绍和常见方法讲解**

* 什么迭代器

  * 访问集合元素的一种方式，可以记住遍历的位置的对象，和Java里面的集合的迭代器Iterator一样

  * 核心是通过某种方式（通常使用循环）访问集合元素的过程

  * 作用

    * 在处理大数据集时，迭代器可以节省内存。
    * 迭代器提供了一种统一的遍历方式，适用于各种数据结构。

  * 迭代器对象和可迭代对象

    * 可迭代对象：实现了`__iter__()`方法的对象
    * 迭代器对象：实现了`__iter__()`和`__next__()`方法的对象称为迭代器对象
    * 通过定义可以知道，**迭代器对象一定是可迭代对象**。
    * 简单解释两个方法：
      *  `__iter__()`要返回一个迭代器对象，可以使用iter() 函数触发
      *  `__next__()`用于从迭代器中返回下一个值，如果没有可返回值，抛出 `StopIteration`异常，用next() 函数来触发它。
    * 常见可迭代对象：列表、元组、字符串、字典、集合、文件对象、生成器

    ```
    # 验证可迭代对象  
    from collections.abc import Iterable
    
    print(isinstance([1,2,3], Iterable))  # True
    print(isinstance("hello", Iterable))  # True
    print(isinstance(123, Iterable))      # False
    
    # isinstance(object, classinfo) 判断一个对象是否为指定类型或指定类型的子类
    # 使用元组传递多个类型，如果对象是其中任意一个类型的实例，则返回 `True`。
    print(isinstance(10, (int, str)))  # 输出：True
    ```

  * 迭代器对象遍历 ( 记录当前迭代位置, 只能向前不能后退)

    * 使用常规for语句进行遍历

    ```
    list=[1,2,3,4]
    it = iter(list)    # 创建迭代器对象
    for x in it:
        print (x, end=" ")
    ```

    * `iter()` 函数
      * 用于将可迭代对象（如列表、元组等）转换为迭代器。
    * 使用 next() 函数
      * `next()` 函数用于从迭代器中获取下一个元素。

    ```
    # 手动使用迭代器
    numbers = [1, 2, 3]
    iterator = iter(numbers)
    
    print(next(iterator))  # 1
    print(next(iterator))  # 2
    print(next(iterator))  # 3
    print(next(iterator))  # 抛出StopIteration异常
    ```

* for 循环的底层原理

  * `for` 循环实际上是通过调用 `iter()` 和 `next()` 来实现的。

  ```
  for item in my_list:
      print(item)
      
  # 等价于：
  
  my_iter = iter(my_list)
  while True:
      try:
          item = next(my_iter)
          print(item)
      except StopIteration:
          break
  ```

  







#### 第6集 如何自定义迭代器和生成器案例实战

**简介：  自定义迭代器和生成器案例实战**

* 如何自定义迭代器？

  * 定义一个类，并实现 `__iter__()` 和 `__next__()` 方法。
  * `__iter__()` 返回迭代器对象本身。
  * `__next__()` 返回下一个元素，如果没有更多元素，则抛出 StopIteration 异常。
  * 示例：自定义一个范围迭代器

  ```
  # __xxx__ 形式的方法被称为魔术方法或特殊方法，有特殊的名称和用途，通常用于实现某些内置操作， 例如，__init__ 用于对象初始化
  # self是一个具有特殊意义的参数，是一个约定俗成的名称，代表类的实例本身。当定义一个类的方法（成员函数）时，按照惯例，第一个参数通常被命名为self
  # 在Python中，self是一个显式传递的参数，而在Java中，this是一个隐式的引用
  class RangeIterator:
      def __init__(self, start, end):
          self.current = start
          self.end = end
  
      def __iter__(self):
          return self
  
      def __next__(self):
          if self.current >= self.end:
              raise StopIteration
          else:
              self.current += 1
              return self.current - 1
  
  # 使用自定义迭代器
  range_iter = RangeIterator(1, 4)
  for num in range_iter:
      print(num)  # 输出 1, 2, 3
  ```

* 生成器

  * 使用了 yield 的函数被称为生成器（generator），是一种特殊的迭代器，使用 `yield` 关键字来返回值。
  * yield 是一个关键字，用于定义生成器函数，是一种特殊的函数，在迭代过程中逐步产生值，而不是一次性返回所有结果
  * 生成器函数在每次调用 `next()` 时执行，直到遇到 `yield` 语句。
  * 作用
    * 生成器可以节省内存，因为它不会一次性生成所有数据, 代码更简洁。
    * 状态保持：每次yield后保持当前执行状态
  * 案例一：调用链路, 生成器生命周期
    * 生成器函数中使用 **yield** 语句时，函数的执行将会暂停，并将 **yield** 后面的表达式作为当前迭代的值返回。
    * 每调用生成器的 **next()** 方法进行迭代时，函数会从上次暂停的地方继续执行，直到再次遇到 **yield** 语句。
    * 生成器函数可以逐步产生值，而不需要一次性计算并返回所有结果

  ```
  def lifecycle_gen():
      print("Stage 1")
      yield "A"
      print("Stage 2")
      yield "B"
      print("Stage 3")
      yield "C"
      print("End of generator")
  
  gen = lifecycle_gen()
  
  try:
      print(next(gen))  # Stage1 -> A
      print(next(gen))  # Stage2 -> B
      print(next(gen))  # Stage3 -> C
      print(next(gen))  # End -> StopIteration
  except StopIteration:
      print("Generator exhausted")
  ```

  * 案例二： 使用生成器实现无限序列，例如自然数序列

  ```
  def natural_numbers():
      num = 1
      while True:
          yield num
          num += 1
  
  # 使用生成器
  numbers = natural_numbers()
  for _ in range(5):
      print(next(numbers))  # 输出 1, 2, 3, 4, 5
  ```

  

* yield vs return

|   特性   |   yield    | return |
| :------: | :--------: | :----: |
| 函数状态 |    保持    |  清除  |
| 执行次数 |    多次    |  一次  |
|  返回值  | 生成器对象 | 单个值 |

* 迭代器 vs 生成器

|    特性    |    迭代器    |      生成器       |
| :--------: | :----------: | :---------------: |
|  实现方式  | 类+协议方法  |    函数+yield     |
|  内存占用  |      低      |       极低        |
| 代码复杂度 |     较高     |       较低        |
|  状态保持  |   显式管理   |     自动管理      |
|  适用场景  | 复杂迭代逻辑 | 简单/中等迭代需求 |



