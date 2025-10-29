### 第四章 AI大模型版-高级函数和Lambda实战

#### 第1集 Python的函数语法规范和返回值语法

**简介：  Python的函数语法规范和返回值语法**

* 函数语法格式

  * 函数是一段可重复使用的代码块，通过名称调用执行， 使用 def 关键字

  * 格式如下

    ```
    def 函数名(参数):
        """文档字符串（可选）"""
        代码块
        return 返回值  # 可选
    ```

  * 案例：计算两个数的和

    ```
    def add(a, b):
        """返回a + b的结果"""
        result = a + b
        return result
    
    sum_result = add(3, 5)
    print(sum_result)  # 8
    ```

* 参数传递

  * **不可变对象**（如整数、字符串、元组）：函数内修改会创建新对象，不影响原数据。

    ```
    def modify_num(n):
        n += 10
        print("函数内n:", n)  # 20
    
    num = 10
    modify_num(num)
    print("函数外num:", num)  # 10（未改变）
    ```

  * **可变对象**（如列表、字典）：函数内修改直接影响原对象。

    ```
    def modify_list(lst):
        lst.append(4)
        print("函数内lst:", lst)  # [1,2,3,4]
    
    my_list = [1,2,3]
    modify_list(my_list)
    print("函数外my_list:", my_list)  # [1,2,3,4]（原列表被修改）
    
    ```

* 参数返回值

  * `return` 语句用于退出函数，选择性地向调用方返回一个表达式, 

  * 不带参数值的 return 语句返回 None：

  * 返回单个值

    ```
    def square(n):
        return n ** 2
    
    print(square(4))  # 16
    ```

  * 返回多个值（元组解包）

    ```
    def calculate(a, b):
        return a + b, a - b, a * b
    
    sum_result, sub_result, mul_result = calculate(5, 3)
    print(sum_result)  # 8
    ```

  * 无返回值（隐式返回None）

    ```
    def greet(name):
        print(f"Hello, {name}!")
    
    result = greet("Alice")  # Hello, Alice!
    print(result)            # None
    ```

  * 拓展 None类型

    * **唯一标识符**：`None` 是Python中的一个特殊常量，表示「空值」或「不存在的值」

    * **数据类型的终点**：任何变量被赋值为 `None` 时，其类型变为 `NoneType`

      ```
      a = None
      print(type(a))  # <class 'NoneType'>
      ```

      |    类型     |          特性          |          示例           |
      | :---------: | :--------------------: | :---------------------: |
      |   `None`    | 绝对空值，不可被实例化 |       `x = None`        |
      |   `False`   |   布尔类型，逻辑假值   |       `if not x:`       |
      | `0` / `""`  | 数值型/字符串的空状态  | `count = 0` / `s = ""`  |
      | `[]` / `{}` |    数据结构的空容器    | `lst = []` / `dct = {}` |

    * 必须显式赋值

      ```
      # 错误示范：不能直接声明未初始化的变量
      x =  # SyntaxError
      
      # 正确方式必须给初始值（可以是None）
      x = None
      y = [None] * 5  # 创建包含5个None的列表
      ```

    * 作为默认参数

      ```
      def greet(name=None):
          print(f"Hello, {name or 'Guest'}!")
      
      greet()  # 输出：Hello, Guest!
      ```

* 案例实战

  * 学生成绩分析器，接收成绩列表，返回最高分、平均分

  ```
  def analyze_scores(scores):
      """接收成绩列表，返回最高分、平均分"""
      max_score = max(scores)
      avg_score = sum(scores) / len(scores)
      return max_score, avg_score
  
  scores = [85, 92, 78, 90]
  max_val, avg_val = analyze_scores(scores)
  print(f"最高分：{max_val}, 平均分：{avg_val:.1f}")
  ```

  



















#### 第2集 Python参数类型高阶语法特性讲解

**简介：  Python参数类型高阶语法特性讲解**

* 函数参数类型

  |      参数类型      |         说明         |          示例代码          |
  | :----------------: | :------------------: | :------------------------: |
  |    **位置参数**    |  按参数位置顺序传递  |        `add(3, 5)`         |
  |   **关键字参数**   |   按参数名指定传递   |      `add(b=5, a=3)`       |
  |    **默认参数**    | 参数定义时设置默认值 | `def greet(name="Guest"):` |
  |    **可变参数**    |   接收任意数量参数   |  `*args`（元组形式接收）   |
  | **关键字可变参数** | 接收任意数量的键值对 | `**kwargs`（字典形式接收） |

  * 位置参数（Positional Arguments）

    * 定义：按参数定义顺序传递，数量必须匹配。

    ```
    def greet(name, message):
        print(f"{message}, {name}!")
    
    greet("Alice", "Hello")  # Hello, Alice!
    ```

  * 关键字参数（Keyword Arguments）

    * 定义：按参数名指定，顺序可打乱

    ```
    greet(message="Hi", name="Bob")  # Hi, Bob!
    
    ```

  * 默认参数（Default Arguments）

    * **定义**：参数定义时指定默认值，调用时可省略。

    ```
    def register(name, age=18, city="北京"):
        print(f"姓名：{name}, 年龄：{age}, 城市：{city}")
    
    register("小明")              # 年龄和城市使用默认值
    register("小红", 20, "上海")   # 覆盖默认值
    ```

  * 可变位置参数（args）

    * **定义**：接收任意数量的位置参数，打包为元组。

    ```
    def sum_numbers(*args):
        return sum(args)
    
    print(sum_numbers(1,2,3))    # 6
    print(sum_numbers(4,5))      # 9
    ```

  * 可变关键字参数（kwargs）

    * **定义**：接收任意数量的关键字参数，打包为字典。

    ```
    def print_info(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    
    print_info(name="Alice", age=25)
    # 输出：
    # name: Alice
    # age: 25
    
    ```

  * 参数顺序规则

    * **标准顺序**：`位置参数 → 默认参数 → *args → **kwargs`

    ```
    def add(a, b, c):
        return a + b + c
    
    numbers = [1, 2, 3]
    print(add(*numbers))  # 6（等价于 add(1,2,3)）
    
    ```

* 参数解包（Unpacking）

  * 列表/元组解包为位置参数（*）

    ```
    def add(a, b, c):
        return a + b + c
    
    numbers = [1, 2, 3]
    print(add(*numbers))  # 6（等价于 add(1,2,3)）
    ```

  * 字典解包为关键字参数（ ** ）

    ```
    def greet(name, message):
        print(f"{message}, {name}!")
    
    params = {"name": "Alice", "message": "Hello"}
    greet(**params)  # Hello, Alice!
    
    ```

* 常见错误

  * 参数顺序错误

    ```
    # 错误：位置参数在关键字参数后
    func(a=1, 2)  # SyntaxError
    
    # 正确：位置参数在前
    func(2, a=1)
    
    ```

    

* 综合案例

  * 混合参数类型

    ```
    def complex_func(a, b, c=0, *args, **kwargs):
        print("a:", a)
        print("b:", b)
        print("c:", c)
        print("args:", args)
        print("kwargs:", kwargs)
    
    complex_func(1, 2, 3, 4, 5, name="Alice", age=25)
    # 输出：
    # a: 1
    # b: 2
    # c: 3
    # args: (4,5)
    # kwargs: {'name': 'Alice', 'age':25}
    
    ```

  * 动态生成SQL查询

    ```
    def build_sql(table, **conditions):
        query = f"SELECT * FROM {table}"
        if conditions:
            where_clause = " AND ".join([f"{key} = '{value}'" for key, value in conditions.items()])
            query += f" WHERE {where_clause}"
        return query
    
    print(build_sql("users", name="Alice", age=25))
    # SELECT * FROM users WHERE name = 'Alice' AND age = '25'
    
    ```

    











#### 第3集 匿名函数Lambda讲解和案例实战

**简介：  匿名函数Lambda讲解和案例实战**

* 什么是Lambda函数

  * **定义**：Lambda函数是匿名的小型函数，用于简化简单函数的定义。
  * 语法：`lambda 参数: 表达式`
    - **无名称**：无需`def`关键字定义。
    - **单行表达式**：只能包含一个表达式，不能有代码块或复杂逻辑； 可以设置多个参数，参数使用逗号 **,** 隔开

  ```
  # 示例1：加法函数
  add = lambda a, b: a + b
  print(add(3, 5))  # 8
  
  # 示例2：平方函数
  square = lambda x: x**2
  print(square(4))  # 16
  
  #作为函数参数传递
  def operate(func, a, b):
      return func(a, b)
  
  result = operate(lambda x, y: x * y, 3, 4)
  print(result)  # 12
  ```

* Lambda与普通函数的对比

  |   **特性**   |      **Lambda函数**      |     **普通函数（def）**      |
  | :----------: | :----------------------: | :--------------------------: |
  |   **名称**   |           匿名           |            需命名            |
  |  **代码量**  |           单行           |            可多行            |
  | **适用场景** | 简单逻辑（如表达式计算） | 复杂逻辑（如循环、条件嵌套） |
  |  **返回值**  |    自动返回表达式结果    |        需显式`return`        |

* Lambda与列表推导式对比

  |       **场景**       |  **Lambda + map/filter**   | **列表推导式** |
  | :------------------: | :------------------------: | :------------: |
  |  **简单转换/过滤**   |         可读性较低         |   更简洁直观   |
  | **函数作为参数传递** |       必须使用Lambda       |  无法直接替代  |
  |       **性能**       | 相近（但生成器更节省内存） |      相近      |

  ```
  # 示例：筛选偶数并平方
  numbers = [1, 2, 3, 4, 5]
  
  # Lambda + map/filter
  result1 = list(map(lambda x: x**2, filter(lambda x: x%2==0, numbers)))
  
  # 列表推导式
  result2 = [x**2 for x in numbers if x%2 ==0]
  
  print(result1, result2)  # [4, 16] [4, 16]
  ```

  

* 注意

  * 仅限单个表达式，无法包含复杂逻辑（如循环、多条件分支）

    ```
    # 错误示例：Lambda中不能包含if-else代码块
    invalid = lambda x: if x > 0: x else -x  # SyntaxError
    
    # 正确做法：使用条件表达式
    valid = lambda x: x if x > 0 else -x
    print(valid(-5))  # 5
    ```

  * 可读性较低, 过度使用会降低代码可读性，尤其是嵌套Lambda

    ```
    # 复杂Lambda示例（不推荐）
    complex_lambda = lambda x: (lambda y: x + y)(10)
    print(complex_lambda(5))  # 15
    
    ```

    























#### 第4集 数据处理领域Python高阶函数实战

**简介：  数据处理领域Python高阶函数实战**

* 什么是高阶函数

  * 满足以下任一条件的函数
    * 接收函数作为参数
    * 返回函数作为结果
  * 优势
    * 代码简洁：通过组合函数减少重复代码。
    * 功能灵活：动态指定处理逻辑
  * 组合应用
    * lambda 函数通常与内置高阶函数如 map()、filter() 和 reduce() 一起使用，在集合上执行操作

* 常用高阶函数详解

  * `map(func, iterable)`

    * 功能：对可迭代对象的每个元素应用func，返回迭代器。
    * 示例：将列表元素平方

    ```
    numbers = [1, 2, 3, 4]
    squared = map(lambda x: x**2, numbers)
    print(list(squared))  # [1, 4, 9, 16]
    ```

    * 对比列表推导式

    ```
    squared = [x**2 for x in numbers]  # 结果相同，但立即生成列表
    ```

  * `filter(func, iterable)`

    * 功能：筛选满足func条件为True的元素，返回迭代器。
    * 示例：过滤偶数

    ```
    even = filter(lambda x: x % 2 == 0, numbers)
    print(list(even))  # [2, 4]
    ```

    * 对比生成器表达式：

    ```
    even = (x for x in numbers if x % 2 == 0)  # 惰性计算，节省内存
    ```

  * `reduce(func, iterable[, initial])`

    * 功能：对元素累积应用func，返回单一结果。
    * 导入：`from functools import reduce`
    * 应用场景：累积计算（求和、求积、合并字典等）。
    * 示例：计算乘积

    ```
    from functools import reduce
    product = reduce(lambda a, b: a * b, [1, 2, 3, 4])
    print(product)  # 24（计算过程：((1*2)*3)*4）
    ```

  * `sorted(iterable, key=None, reverse=False)`

    * 功能：排序可迭代对象，key指定排序规则。
    * 示例：按字符串长度排序

    ```
    words = ["apple", "banana", "cherry", "date"]
    sorted_words = sorted(words, key=lambda x: len(x))
    print(sorted_words)  # ['date', 'apple', 'banana', 'cherry']
    ```

* 高阶函数综合应用案例

  * 数据清洗管道

  ```
  data = [5, 12, 8, "10", 3.5, "7"]
  
  # 步骤1：过滤非整数
  filtered = filter(lambda x: isinstance(x, int), data)
  # 步骤2：转换为绝对值
  processed = map(abs, filtered)
  print(list(processed))  # [5, 12, 8, 3]
  
  ```

  * 字典合并（使用reduce）

  ```
  from functools import reduce
  
  dicts = [{"a": 1}, {"b": 2}, {"a": 3, "c": 4}]
  merged = reduce(lambda d1, d2: {**d1, **d2}, dicts)
  print(merged)  # {'a':3, 'b':2, 'c':4}
  
  ```

* 注意事项

  * 惰性求值与内存管理

    * map、filter返回迭代器，适合处理大数据（逐项处理，不一次性加载到内存）

    ```
    large_data = range(1_000_000)
    squared_iter = map(lambda x: x**2, large_data)  # 内存友好
    ```

  * 可读性与简洁的平衡

    * **避免过度嵌套**：复杂的`lambda`或链式调用可能降低代码可读性。

    ```
    # 不推荐：难以理解的嵌套
    result = map(lambda x: x*2, filter(lambda x: x>5, data))
    
    # 推荐：分步或使用生成器表达式
    filtered = (x for x in data if x > 5)
    result = (x*2 for x in filtered)
    
    ```

  * 性能考量

    * 列表推导式 vs map/filter：性能相近，选择更易读的方式。
    * reduce的替代方案：显式循环有时更直观

