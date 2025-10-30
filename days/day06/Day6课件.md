### 第六章 AI大模型版-文件处理和常用模块实战



#### 第1集 Python文件IO操作案例最佳实践

**简介：  Python文件IO操作案例实战**

* 文件操作步骤

  * **打开文件**：建立程序与文件的连接。
  * **读写操作**：读取内容或写入数据。
  * **关闭文件**：释放系统资源。

* 文件打开模式

  | 模式 |            说明            | 文件存在 | 文件不存在 |
  | :--: | :------------------------: | :------: | :--------: |
  | `r`  |   只读（文本模式，默认）   | 正常打开 |    报错    |
  | `w`  |    写入（覆盖原有内容）    | 清空内容 | 创建新文件 |
  | `a`  |   追加（在文件末尾添加）   | 正常打开 | 创建新文件 |
  | `r+` |   读写（文件指针在开头）   | 正常打开 |    报错    |
  | `b`  | 二进制模式（配合其他模式） |    -     |            |

* 文件操作语法与案例

  * 常规操作文件打开读取

    ```
    # 不推荐（可能忘记关闭文件）
    file = open("test.txt", "r")
    try:
        content = file.read()
    finally:
        file.close()  # 必须手动关闭
    
    
    # 推荐始终使用with语句：自动处理文件关闭，避免资源泄漏。
    with open("test.txt") as f:
        content = f.read()
    ```

  * with open语法结构

    * `file_path`（必需）
      要操作的文件路径（字符串类型），可以是绝对路径或相对路径。
      示例：`"data.txt"`、`"/home/user/docs/file.csv"`
    * `mode`（可选，默认为 `'r'`）
      指定文件的打开模式，常用模式如下

    ```
    with open(file_path, mode='r', encoding=None, ...) as file_object:
        # 在此代码块内操作文件
        # 文件会自动关闭（无论是否发生异常）
    ```

    

  * 基础文件读写  (**明确指定文件编码**：避免中文乱码，优先使用`utf-8`。)

    ```
    # 写入文件（覆盖模式）
    with open("test.txt", "w", encoding="utf-8") as f:
        f.write("Hello, World!\n")
        f.write("第二行内容")
    
    # 读取文件（全部内容）
    with open("test.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(content)
    # 输出：
    # Hello, World!
    # 第二行内容
    ```

    

  * 逐行读取和写入

    ```
    # 写入多行
    lines = ["Python\n", "Java\n", "C++\n"]
    with open("languages.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)
    
    # 逐行读取（推荐方式）
    with open("languages.txt", "r", encoding="utf-8") as f:
        for line in f:          # 自动处理大文件，内存友好
            print(line.strip())  # 移除换行符
    # 输出：
    # Python
    # Java
    # C++
    
    ```

  * 追加内容

    ```
    with open("test.txt", "a", encoding="utf-8") as f:
        f.write("\n追加的内容")
    
    ```

  * 读取特定行数

    ```
    with open("test.txt", "r", encoding="utf-8") as f:
        first_line = f.readline()    # 读取第一行
        next_lines = f.readlines()   # 读取剩余所有行（返回列表）
    ```

  * 二进制文件操作（图片复制）

    ```
    with open("input.jpg", "rb") as src, open("output.jpg", "wb") as dst:
        dst.write(src.read())  # 复制图片
    ```

    













#### 第2集 Python的pip模块安装和管理实战

**简介：  Python的pip模块安装和管理实战**

* 什么是pip

  * 是 Python 包管理工具，该工具提供了对 Python 包的查找、下载、安装、卸载的功能，类似Maven, Npm
  * Python 2.7.9 + 或 Python 3.4+ 以上版本都自带 pip 工具
  * 管理超过40万个PyPI软件包
  * 在 VS Code中，有一个免费扩展(Extension）：PIP Manager ，可以很方便查看和调整相关的软件依赖模块

* 核心操作

  * 安装与管理包

    ```
    # 安装最新版本
    pip install requests
    
    # 安装指定版本
    pip install numpy==1.21.0
    
    # 升级包版本
    pip install --upgrade requests
    
    # 卸载包
    pip uninstall pandas
    
    #更新pip版本
    python -m pip install --upgrade pip
    ```

  * 环境检查

    ```
    # 查看已安装包列表
    pip list
    
    # 检查过期包
    pip list --outdated
    
    # 显示包详细信息
    pip show flask
    ```

  * 导出当前 Python 环境的配置

    * 一个项目里面会有很多依赖包，可以通过pip freeze查看和导出
    * 包括网上下载的Python项目，可以通过这个命令安装对应的环境

    ```
    # 导出环境依赖
    pip freeze > requirements.txt
    
    # 从文件安装依赖
    pip install -r requirements.txt
    
    ```

    

* 镜像源配置加速

  ```
  # 临时使用镜像源安装依赖包
  pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
  
  # 永久配置镜像源
  pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
  
  #很多源
  清华 https://pypi.tuna.tsinghua.edu.cn/simple
  腾讯 http://mirrors.cloud.tencent.com/pypi/simple
  阿里 https://mirrors.aliyun.com/pypi/simple/
  
  # 更换阿里源
  pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
  
  # 更换清华源
  pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
  
  # 更换腾讯源
  pip config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple
  
  # 更换中科大源
  pip config set global.index-url https://pypi.mirrors.ustc.edu.cn/simple
  
  #恢复默认源
  pip config set global.index-url https://pypi.org/simple
  ```

  * 配置文件管理

  ```
  配置文件路径：
  Windows: %APPDATA%\pip\pip.ini
  macOS/Linux: ~/.config/pip/pip.conf
  ```

  * 查看系统配置的镜像源操作

  ```
  pip config list
  ```

  











#### 第3集 Python常用内置模块案例实战

**简介：  Python常用内置模块案例实战**

* 讲解Python自带高频模块使用

|   模块   |        典型应用场景        |
| :------: | :------------------------: |
|   `os`   |     文件管理、路径操作     |
|  `json`  | API数据交换、配置文件读写  |
|  `sys`   | 脚本参数处理、程序退出控制 |
| `random` |   生成随机数据、游戏开发   |
|  `math`  |     科学计算、几何问题     |

* os模块：操作系统交互

  * **核心功能**：文件/目录操作、路径管理、环境变量。
  * 常用函数与案例

  ```
  import os
  
  # 1.1 获取当前工作目录
  current_dir = os.getcwd()
  print("当前目录:", current_dir)  # 输出：/Users/yourname/projects
  
  # 1.2 遍历目录下的文件
  files = os.listdir(".")  # 当前目录所有文件和子目录
  print("文件列表:", files)
  
  # 1.3 路径拼接（跨平台安全）
  file_path = os.path.join("data", "test.txt")  # data/test.txt（Windows自动转反斜杠）
  
  # 1.4 创建目录（如果不存在）
  if not os.path.exists("backup"):
      os.makedirs("backup")  # 创建多级目录
  
  # 1.5 删除文件
  os.remove("temp.txt")  # 文件不存在会报错
  ```

* json模块：JSON数据处理

  * **核心功能**：序列化（Python对象→JSON字符串）、反序列化（JSON→Python对象）。
  * 常用函数与案例

  ```
  import json
  
  # 2.1 字典转JSON字符串
  data = {"name": "小明", "age": 18, "is_student": True}
  json_str = json.dumps(data, ensure_ascii=False)  # 禁用ASCII转码
  print("JSON字符串:", json_str)  # {"name": "小明", "age": 18, "is_student": true}
  
  # 2.2 JSON字符串转字典
  data_restored = json.loads(json_str)
  print("恢复的字典:", data_restored["name"])  # 小明
  
  # 2.3 读写JSON文件
  # 写入
  with open("user.json", "w", encoding="utf-8") as f:
      json.dump(data, f, indent=4)  # 缩进美化
  
  # 读取
  with open("user.json", "r", encoding="utf-8") as f:
      loaded_data = json.load(f)
      print("文件内容:", loaded_data)
  
  ```

* sys模块：系统相关操作

  * **核心功能**：命令行参数、程序退出、系统路径。
  * 常用函数与案例

  ```
  import sys
  
  # 3.1 获取命令行参数
  # 运行命令：python script.py arg1 arg2
  print("脚本名:", sys.argv[0])     # script.py
  print("第一个参数:", sys.argv[1])  # arg1
  
  # 3.2 强制退出程序（带状态码）
  if len(sys.argv) < 2:
      print("缺少参数！")
      sys.exit(1)  # 非0表示异常退出
  
  # 3.3 添加自定义模块搜索路径
  sys.path.append("/my_modules")  # 临时添加
  
  ```

* random模块：随机数生成

  * **核心功能**：生成伪随机数、随机选择元素。
  * 常用函数与案例

  ```
  import random
  
  # 4.1 生成随机整数（包含两端）
  num = random.randint(1, 10)  # 1~10之间的整数
  print("随机数:", num)
  
  # 4.2 随机选择元素
  fruits = ["苹果", "香蕉", "橘子"]
  choice = random.choice(fruits)  # 随机选一个
  print("随机水果:", choice)  # e.g. 橘子
  
  # 4.3 打乱列表顺序（原地修改）
  cards = ["A", "2", "3", "J", "Q", "K"]
  random.shuffle(cards)
  print("洗牌后:", cards)  # e.g. ['Q', 'A', '3', ...]
  
  # 4.4 生成随机验证码（6位字母+数字）
  import string
  chars = string.ascii_letters + string.digits  # 所有字母和数字
  code = ''.join(random.choices(chars, k=6))    # 生成6位
  print("验证码:", code)  # e.g. aB3dE7
  
  ```

* math模块：数学运算

  * **核心功能**：数学函数、常数。
  * 常用函数与案例

  ```
  import math
  
  # 5.1 计算平方根和幂
  a = math.sqrt(25)     # 5.0
  b = math.pow(2, 3)    # 8.0
  print(f"平方根: {a}, 幂: {b}")
  
  # 5.2 向上/向下取整
  c = math.ceil(3.2)    # 4
  d = math.floor(3.8)   # 3
  print(f"向上取整: {c}, 向下取整: {d}")
  
  # 5.3 常数π和弧度转换
  radius = 5
  area = math.pi * radius ** 2  # 圆面积公式
  degrees = math.degrees(math.pi)  # 180.0
  print(f"圆面积: {area:.2f}, 弧度转角度: {degrees}")
  
  # 5.4 对数运算
  log_value = math.log(100, 10)  # 以10为底的log(100) → 2.0
  print("对数结果:", log_value)
  
  ```

  

