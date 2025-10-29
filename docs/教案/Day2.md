### 第二章 AI大模型版-Python核心数据类型讲解



#### 第1集 Python的字符串和常见方法操作

**简介：  Python的字符串和常见方法操作**

* 字符串基础

  * **定义方式**

    * 字符串一旦创建，内容不可修改（修改会创建新对象）

    ```
    s1 = '单引号字符串'
    s2 = "双引号字符串"
    s3 = '''三引号支持
            多行字符串'''
    s4 = r"原始字符串\n不转义"  # 输出：r Row String代表原始字符串，转义符失效 原始字符串\n不转义
    ```

  * 转义字符

    |    转义符    |   说明   |          示例           |
    | :----------: | :------: | :---------------------: |
    |     `\\`     |  反斜杠  | `print("C:\\")` → `C:\` |
    |     `\n`     |   换行   |    `"Hello\nWorld"`     |
    |     `\t`     |  制表符  |    `"Name:\tAlice"`     |
    | `\'` 或 `\"` | 保留引号 |      `'It\'s OK'`       |

  * 索引与切片

    ```
    s = "Python"
    print(s[0])     # P（正向索引，从0开始）
    print(s[-1])    # n（反向索引，从-1开始）
    print(s[2:5])   # tho（切片：[起始, 结束)）
    print(s[::2])   # Pto（步长为2）
    
    ```

* 字符串常用方法

  * 大小写转换

    ```
    s = "Hello, Python"
    print(s.upper())       # HELLO, PYTHON
    print(s.lower())       # hello, python
    print(s.title())       # Hello, Python（每个单词首字母大写）
    print(s.swapcase())    # hELLO, pYTHON（大小写互换）
    ```

  * 查找和替换

    ```
    s = "Hello World"
    # 查找子串位置
    print(s.find("World"))     # 6（返回首次出现的索引，找不到返回-1）
    print(s.index("lo"))       # 3（类似find，但找不到会报错）
    
    # 统计出现次数
    print(s.count("l"))        # 3
    
    # 替换内容
    print(s.replace("World", "Python"))  # Hello Python
    ```

  * 字符串分割与连接

    ```
    # 分割为列表
    s = "apple,banana,orange"
    print(s.split(","))        # ['apple', 'banana', 'orange']
    
    # 按行分割（适用于多行文本）
    text = "Line1\nLine2\nLine3"
    print(text.splitlines())   # ['Line1', 'Line2', 'Line3']
    
    # 连接列表为字符串
    lst = ["2023", "10", "01"]
    print("-".join(lst))       # 2030-10-01
    ```

  * 去除空白与填充

    ```
    s = "   Python   "
    print(s.strip())       # "Python"（去除两侧空白）
    print(s.lstrip())      # "Python   "（去左空白）
    print(s.rstrip())      # "   Python"（去右空白）
    
    # 填充对齐
    print(s.center(20, "*"))   # ****Python****（居中填充）
    print(s.zfill(10))         # 0000Python（左侧补零）
    
    ```

* 字符串格式化

  * 旧式格式化（%）

    ```
    name = "Alice"
    age = 25
    print("Name: %s, Age: %d" % (name, age))  # Name: Alice, Age: 25
    ```

  * str.format()

    ```
    print("{} + {} = {}".format(3, 5, 8))         # 3 + 5 = 8（按顺序）
    print("{name}喜欢{language}".format(name="小明", language="Python"))  # 关键字参数
    ```

  * f-string（Python 3.6+）

    ```
    price = 19.99
    print(f"价格：{price:.2f}元")   # 价格：19.99元（保留两位小数）
    ```

* **字符串方法速查表**

  |     方法名     |       功能说明       |                  示例                  |
  | :------------: | :------------------: | :------------------------------------: |
  |   `split()`    |  按分隔符分割字符串  |  `"a,b,c".split(",") → ['a','b','c']`  |
  |   `strip()`    |     去除两侧空白     |        `" hi ".strip() → "hi"`         |
  |  `replace()`   |       替换子串       | `"Hello".replace("e", "a") → "Hallo"`  |
  | `startswith()` | 判断是否以某子串开头 | `"file.txt".startswith("file") → True` |
  |  `endswith()`  | 判断是否以某子串结尾 | `"image.jpg".endswith(".jpg") → True`  |

















#### 第2集 Python常用自带初级函数讲解

**简介：  Python常用自带初级函数讲解**

* Python很多函数，没法一个个记住，掌握高频的使用的即可

  

* 基础操作类函数

  * `print()`

    * **功能**：输出内容到控制台
    * **参数**：`*values`（多个值）、`sep`（分隔符）、`end`（结束符）

    ```
    print("Hello", "World", sep=", ", end="!")  # Hello, World!
    ```

  * `input()`

    * **功能**：获取用户输入（返回字符串）
    * **参数**：`prompt`（提示信息）
    * **案例**：

    ```
    name = input("请输入姓名：")  
    print(f"你好，{name}！")
    ```

* 数据类型转换

  * `int()` / `float()` / `str()` / `bool()`

    * **功能**：强制类型转换
    * **案例**

    ```
    num = int("123")        # 字符串→整数 → 123  
    price = float("9.9")    # 字符串→浮点数 → 9.9  
    text = str(100)         # 整数→字符串 → "100"
    ```

  * `list()` / `tuple()` / `dict()` / `set()`

    * **功能**：创建或转换容器类型
    * **案例**：

    ```
    # 1. 字符串转列表（按字符拆分）
    chars = list("Python")
    print(chars)  # 输出：['P', 'y', 't', 'h', 'o', 'n']
    
    # 2. 元组转列表
    tup = (1, 2, 3)
    lst = list(tup)
    print(lst)    # 输出：[1, 2, 3]
    
    #创建空列表（等效于 []）
    empty = list()
    print(empty)   # 输出：[]
    
    #=================================
    # 1. 列表转元组
    lst = [10, 20, 30]
    tup = tuple(lst)
    print(tup)    # 输出：(10, 20, 30)
    
    # 2. 字典转元组（仅保留键）
    dct = {'a': 1, 'b': 2}
    keys = tuple(dct)
    print(keys)   # 输出：('a', 'b')
    
    #创建空元组（等效于 ()）
    empty = tuple()
    print(empty)   # 输出：()
    
    #=================================
    # 1. 键值对列表转字典
    pairs = [('a', 1), ('b', 2)]
    dct = dict(pairs)
    print(dct)    # 输出：{'a': 1, 'b': 2}
    
    # 2. 关键字参数创建
    dct = dict(name='Alice', age=25)
    print(dct)    # 输出：{'name': 'Alice', 'age': 25}
    
    #创建空字典（等效于 {}）
    empty = dict()
    print(empty)  # 输出：{}
    #=================================
    
    # 1. 列表去重
    nums = [1, 2, 2, 3, 3]
    unique = set(nums)
    print(unique)  # 输出：{1, 2, 3}
    
    # 2. 字符串转字符集合
    chars = set("apple")
    print(chars)   # 输出：{'a', 'p', 'l', 'e'}
    
    #创建空集合（注意不能用 {}）
    empty = set()
    print(empty)   # 输出：set()
    ```

* 数学与序列操作

  * `range()`

    * **功能**：生成整数序列（常用于循环）
    * **参数**：`start`, `stop`, `step`
    * **案例**

    ```
    range(stop)            # 生成 [0, stop) 的整数序列，步长=1
    range(start, stop)     # 生成 [start, stop) 的整数序列，步长=1
    range(start, stop, step)  # 生成 [start, stop) 的整数序列，步长=step
    
    # 生成 0-4
    r1 = range(5)
    print(list(r1))  # 输出 [0, 1, 2, 3, 4]
    
    # 生成 2-5（不包含5）
    r2 = range(2, 5)
    print(list(r2))  # 输出 [2, 3, 4]
    
    for i in range(2, 10, 2):  
        print(i)  # 输出 2 4 6 8
    ```

  * `len()`

    * **功能**：获取容器长度（字符串、列表、字典等）
    * **案例**

    ```
    text = "Python"  
    print(len(text))  # 6
    ```

  * `sum()` / `max()` / `min()`

    * **功能**：计算总和、最大值、最小值
    * **案例**

    ```
    nums = [1, 2, 3]  
    print(sum(nums))   # 6  
    print(max(nums))   # 3
    ```

* 时间处理（time模块）

  * `time.time()`

    * **功能**：获取当前时间戳（单位：秒）从1970年到现在的秒数
    * **案例**：

    ```
    import time  
    start = time.time()  
    time.sleep(2)  # 暂停2秒  
    end = time.time()  
    print(f"耗时：{end - start:.2f}秒")  # 耗时：2.00秒
    
    ```

  * `time.strftime()`

    * **功能**：格式化时间
    * **案例**：

    ```
    import time  
    now = time.strftime("%Y-%m-%d %H:%M:%S")  
    print(now)  # 2030-10-01 14:30:00
    ```

    

















#### 第3集 Python的列表List和常见方法操作

**简介：  Python的列表List和常见方法操作**

* 列表List

  * 定义方式

    ```
    list1 = [1, 2, 3]                # 直接定义
    list2 = list("abc")              # 通过可迭代对象转换 → ['a', 'b', 'c']
    list3 = []                       # 空列表
    list4 = [1, "hello", True, [2, 3]]  # 可混合多种类型
    ```

  * 核心特性

    - **有序**：元素按插入顺序存储。
    - **可变**：支持增删改操作（内存地址不变）。
    - **可重复**：允许包含相同元素。

  * 索引与切片

    ```
    lst = ["a", "b", "c", "d", "e"]
    # 索引
    print(lst[0])    # a（正向索引，从0开始）
    print(lst[-1])   # e（反向索引，从-1开始）
    
    # 切片（返回新列表）
    print(lst[1:3])  # ['b', 'c']（左闭右开）
    print(lst[::2])  # ['a', 'c', 'e']（步长2）
    ```

* 列表常用方法

  * 增删元素

  |         方法         |                功能说明                |               示例代码               |
  | :------------------: | :------------------------------------: | :----------------------------------: |
  |    `append(obj)`     |             在末尾添加元素             |     `lst.append(4) → [1,2,3,4]`      |
  | `insert(index, obj)` |           在指定索引插入元素           | `lst.insert(1, "x") → [1, 'x', 2,3]` |
  |  `extend(iterable)`  |        合并可迭代对象到列表末尾        |  `lst.extend([4,5]) → [1,2,3,4,5]`   |
  |    `remove(obj)`     |    删除第一个匹配的元素（无返回值）    |       `lst.remove(2) → [1,3]`        |
  |   `pop(index=-1)`    | 删除并返回指定索引元素（默认最后一个） |       `lst.pop(1) → 2 → [1,3]`       |
  |      `clear()`       |                清空列表                |          `lst.clear() → []`          |

  * 查询与统计

  |     方法     |               功能说明               |       示例代码       |
  | :----------: | :----------------------------------: | :------------------: |
  | `index(obj)` | 返回元素首次出现的索引（找不到报错） | `lst.index("b") → 1` |
  | `count(obj)` |           统计元素出现次数           |  `lst.count(2) → 2`  |
  |  `len(lst)`  |             获取列表长度             |  `len([1,2,3]) → 3`  |

  * 排序与反转

  |              方法               |           功能说明           |            示例代码             |
  | :-----------------------------: | :--------------------------: | :-----------------------------: |
  | `sort(key=None, reverse=False)` |     原地排序（无返回值）     | `lst.sort(reverse=True) → 降序` |
  |       `sorted(iterable)`        | 返回新排序列表（原列表不变） |     `sorted(lst) → 新列表`      |
  |           `reverse()`           |       原地反转列表顺序       |    `lst.reverse() → [3,2,1]`    |













#### 第4集 Python的字典Dict和常见方法操作

**简介：  Python的字典Dict和常见方法操作**

* 字典Dict

  * 字典是键值对（`key-value`）的集合，键唯一且不可变（如字符串、数字、元组），值可以是任意类型。

  ```
  # 创建字典的多种方式
  dict1 = {}                      # 空字典
  dict2 = {"name": "Alice", "age": 25}
  dict3 = dict(name="Bob", age=30)  # 关键字参数创建
  dict4 = dict([("id", 1001), ("city", "Beijing")])  # 可迭代对象
  ```

  * 特性：
    * 无序性（Python 3.7之前无序，之后有序但不应依赖顺序）。
    * 动态可变：可随时增删改键值对。
    * 高效查找：通过键直接访问值，时间复杂度为O(1)。
  * 键的限制
    * **键必须是不可变类型**，如`int`、`str`、`tuple`（不含可变元素的元组）。
    * **键不可重复**，重复赋值会覆盖旧值。

* 字典常用操作

  * 增删改查

  ```
  student = {"name": "Alice", "age": 20}
  
  # 查：通过键访问
  print(student["name"])          # Alice（键不存在会报KeyError）
  print(student.get("age", 18))   # 20（键不存在返回默认值18）
  
  # 增/改
  student["gender"] = "Female"    # 添加新键值对
  student["age"] = 21             # 修改已有键的值
  
  # 删
  del student["gender"]           # 删除指定键值对
  age = student.pop("age")        # 删除并返回值 → 21
  student.clear()                 # 清空字典 → {}
  ```

  * 常用方法

  |           方法名           |                功能说明                |                        示例                         |
  | :------------------------: | :------------------------------------: | :-------------------------------------------------: |
  |          `keys()`          |          返回所有键的视图对象          |       `student.keys() → dict_keys(['name'])`        |
  |         `values()`         |          返回所有值的视图对象          |     `student.values() → dict_values(['Alice'])`     |
  |         `items()`          |        返回所有键值对的视图对象        | `student.items() → dict_items([('name', 'Alice')])` |
  |      `update(dict2)`       |         合并字典（覆盖重复键）         |  `student.update({"age": 22, "city": "Shanghai"})`  |
  | `setdefault(key, default)` | 若键存在返回其值，否则插入键并设默认值 |    `student.setdefault("name", "Bob") → "Alice"`    |
  |        `popitem()`         |   删除并返回最后插入的键值对（LIFO）   |     `student.popitem() → ('city', 'Shanghai')`      |

* 注意事项

  * 键不可变：列表、字典等可变类型不能作为键。

  ```
  # 错误示例：列表作为键
  invalid_dict = {["id"]: 1001}  # TypeError: unhashable type: 'list'
  ```

  

* 作业练习

  * 统计单词频率

  ```
  text = "apple banana apple orange banana apple"
  words = text.split()
  word_count = {}
  for word in words:
      word_count[word] = word_count.get(word, 0) + 1
  print(word_count)  # {'apple':3, 'banana':2, 'orange':1}
  ```

  















#### 第5集 Python的元组Tulple和常见方法操作

**简介：  Python的元组Tulple和常见方法操作**

* 元组Tulple

  * 定义：元组是一个不可变的序列类型，可以包含任意类型的元素
  * 语法：使用圆括号 `()`，元素用逗号分隔（**单元素元组必须加逗号**）
  * 元组比列表更轻量，适用于只读场景。

  ```
  t1 = ()                 # 空元组
  t2 = (1,)               # 单元素元组 → (1,)
  t3 = (1, "a", True)     # 混合类型
  t4 = 4, 5, 6            # 括号可省略 → (4,5,6)
  ```

  * 核心特性：

    * 不可变性：元组一旦创建，元素不能增删改（但可包含可变元素，如列表,可以修改这个里面的内容）

    ```
    t = (1, 2, 3)
    t[0] = 100  # 报错：TypeError（不可修改元素）
    
    
    t = ([1,23,4,5], 2, 3)
    t[0].append(1111) #可以修改
    print(t[0]) 
    ```

    * 有序性：元素按插入顺序存储。
    * 可重复：允许包含相同元素。

  * 注意事项

    * **单元素元组的逗号**：单元素必须加逗号，否则视为普通变量

    ```
    t = (1,)   # 正确 → 元组
    t = (1)    # 错误 → 整数1
    ```

    * 元组真的完全不可变吗？元组本身的引用不可变，但若包含可变元素（如列表），其内部可修改

    ```
    t = (1, [2, 3])
    t[1].append(4)  # 合法 → (1, [2,3,4])
    ```

    

* 元组常用操作

  * 元组常见方法

    * count(obj)  统计元素出现的次数

    ```
    t = (1, 2, 2, 3, 2)
    print(t.count(2))  # 3
    ```

    * index(obj) 返回元素首次出现的索引（找不到时报错）

    ```
    t = ("a", "b", "c", "b")
    print(t.index("b"))  # 1
    ```

  * 索引与切片

  ```
  t = (10, 20, 30, 40, 50)
  
  # 索引
  print(t[0])     # 10（正向索引，从0开始）
  print(t[-1])    # 50（反向索引，从-1开始）
  
  # 切片（返回新元组）
  print(t[1:3])   # (20,30)（左闭右开）
  print(t[::2])   # (10,30,50)（步长2）
  ```

  * 元组拼接与重复

  ```
  t1 = (1, 2)
  t2 = (3, 4)
  
  # 拼接（生成新元组）
  t3 = t1 + t2    # (1,2,3,4)
  
  # 重复
  t4 = t1 * 3     # (1,2,1,2,1,2)
  
  ```

  * 元组普通解包（Unpacking）

  ```
  a, b, c = (10, 20, 30)
  print(a, b, c)  # 10 20 30
  ```

* 案例练习

  * 学生信息存储与解包

  ```
  student = ("张三", 20, "Computer Science")
  name, age, major = student
  print(f"{name}主修{major}")  # 主修Computer Science
  ```

  













#### 第6集 Python的集合Set和常见方法操作

**简介：  Python的集合Set和常见方法操作**

* 集合Set

  * 集合是一个**无序、不重复元素**的容器，元素必须是不可变类型（如数字、字符串、元组）
  * 集合与字典的关系, 字典的键集合类似集合，但字典存储键值对，集合仅存储键。

  ```
  # 创建集合
  s1 = {1, 2, 3}              # 直接定义
  s2 = set([1, 2, 2, 3])      # 通过可迭代对象 → {1, 2, 3}
  empty_set = set()           # 空集合（不能使用 {}，因为这是空字典）
  ```

  * 核心特性

    * 元素唯一性：自动去重，重复元素仅保留一个。
    * 无序性：元素存储顺序与添加顺序无关。
    * 高效成员检测：查找元素的时间复杂度为O(1)。

  * 不可变集合（frozenset）

    * 不可变版本的集合，不可增删元素，可哈希（可作为字典的键）

    ```
    fs = frozenset([1, 2, 3])
    ```

  * 注意事项

    * 集合元素无顺序，无法通过索引访问

    ```
    s = {3, 1, 2}
    print(list(s))  # 输出顺序不确定（如 [1,2,3] 或 [3,1,2]）
    ```

    * 如何创建空集合？

    ```
    s = set()   # 正确（空集合）
    s = {}      # 错误（创建的是空字典）
    ```

    

* 集合常用方法

  * 增删元素

  |        方法        |                功能说明                |            示例代码             |
  | :----------------: | :------------------------------------: | :-----------------------------: |
  |   `add(element)`   |              添加单个元素              |     `s.add(4) → {1,2,3,4}`      |
  | `update(iterable)` |         合并可迭代对象中的元素         | `s.update([4,5]) → {1,2,3,4,5}` |
  | `remove(element)`  |    删除指定元素（元素不存在时报错）    |      `s.remove(3) → {1,2}`      |
  | `discard(element)` |   删除指定元素（元素不存在时不报错）   |     `s.discard(3) → {1,2}`      |
  |      `pop()`       | 随机删除并返回一个元素（集合为空报错） |          `s.pop() → 1`          |
  |     `clear()`      |                清空集合                |       `s.clear() → set()`       |

  * 集合运算

  |            方法            |          运算符           |               功能说明               |                 示例代码                 |
  | :------------------------: | :-----------------------: | :----------------------------------: | :--------------------------------------: |
  |        `union(s2)`         | `    |                  ` |       返回并集（不修改原集合）       |                                          |
  |     `intersection(s2)`     |            `&`            |               返回交集               |   `s1 & s2` → 同时存在于s1和s2中的元素   |
  |      `difference(s2)`      |            `-`            |    返回差集（s1有但s2没有的元素）    |      `s1 - s2` → s1中不在s2中的元素      |
  | `symmetric_difference(s2)` |            `^`            | 返回对称差集（仅在一个集合中的元素） | `s1 ^ s2` → 在s1或s2中但不同时存在的元素 |

  * 集合关系判断

  |       方法       |          功能说明          |             示例代码             |
  | :--------------: | :------------------------: | :------------------------------: |
  |  `issubset(s2)`  | 判断当前集合是否为s2的子集 |  `s1.issubset(s2) → True/False`  |
  | `issuperset(s2)` |   判断当前集合是否包含s2   | `s1.issuperset(s2) → True/False` |
  | `isdisjoint(s2)` |   判断两个集合是否无交集   | `s1.isdisjoint(s2) → True/False` |

* 集合操作案例

  * 去重

  ```
  lst = [1, 2, 2, 3, 3, 3]
  unique = set(lst)        # {1, 2, 3}
  new_lst = list(unique)  # [1, 2, 3]（但顺序可能丢失）
  ```

  * 集合运算应用

  ```
  # 统计两个列表的共同元素
  list1 = [1, 2, 3]
  list2 = [2, 3, 4]
  common = set(list1) & set(list2)  # {2, 3}
  ```

  * 权限管理系统

  ```
  # 用户权限集合
  user_permissions = {"read", "write"}
  required_permissions = {"write", "execute"}
  
  # 检查用户是否具备所有必需权限
  if required_permissions.issubset(user_permissions):
      print("权限足够")
  else:
      print("缺少权限：", required_permissions - user_permissions)
      # 输出：缺少权限：{'execute'}
  ```

  

