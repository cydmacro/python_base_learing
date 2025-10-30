# Day 6 测评 - 文件操作与异常处理

**时间**: 30分钟 | **总分**: 100分

## 一、选择题(40分)

**1. 读取文本文件的正确方式是?(4分)**
A. `f = open('data.txt','r')`
B. `f = read('data.txt')`
C. `f = file('data.txt')`
D. `f = load('data.txt')`
**答案**: A

**2. with语句的作用是?(4分)**
A. 自动关闭文件
B. 加快读取速度
C. 防止报错
D. 格式化输出
**答案**: A

**3. JSON文件的读取用?(4分)**
A. `json.read()`
B. `json.load(f)`
C. `json.open()`
D. `json.get()`
**答案**: B

**4. 异常捕获的正确语法是?(4分)**
A. `try: ... catch: ...`
B. `try: ... except: ...`
C. `catch: ... except: ...`
D. `error: ... handle: ...`
**答案**: B

**5. 写入文件用什么模式?(4分)**
A. 'r'
B. 'w'
C. 'a'
D. 'x'
**答案**: B

**6. `f.readlines()`返回什么?(4分)**
A. 字符串
B. 列表
C. 字典
D. 元组
**答案**: B

**7. 追加模式是?(4分)**
A. 'r'
B. 'w'
C. 'a'
D. 'r+'
**答案**: C

**8. 捕获所有异常用?(4分)**
A. `except:`
B. `except Exception:`
C. `except Error:`
D. A和B都对
**答案**: D

**9. 文件操作的步骤有?(多选,8分)**
A. 打开文件
B. 读写文件
C. 关闭文件
D. 删除文件
**答案**: ABC

**10. try-except的组成部分?(多选,8分)**
A. try
B. except
C. else
D. finally
**答案**: ABCD

## 二、实操题(60分)

**实操题1(20分): 配置文件读取**
编写程序:
1. 创建config.txt,包含:`name=张三\nage=20\ncity=北京`
2. 读取文件
3. 解析为字典格式
4. 输出配置信息

**实操题2(40分): 数据处理日志系统**
编写程序:
1. 读取student_scores.txt(自己创建测试数据)
2. 计算平均分
3. 将结果写入report.txt
4. 添加异常处理(文件不存在/数据格式错误)
5. 在日志文件log.txt中记录处理过程
