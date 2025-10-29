# teachers = ["python", "java", "c++"]
# for t in teachers:
#     print(f"小明 love 学习 {t}!")

# 输出：
# 小明 love 学习 python!
# 小明 love 学习 java!
# 小明 love 学习 c++!


# word = "学习python"

# for c in  word:
#     print(c)

# 遍历字典
# dict1 = {"Monday": "星期一", "Tuesday": "星期二"}
# for key in dict1.keys():
#     print(key)  # 输出字典的键


# for j in range(1,5):
#     print(j)

# count = 0
# while count < 5:
#     print(f"Count: {count}")
#     count += 1


# password = ""

# while password != "123456":
#     password = input("请输入密码：")
#     print("密码错误，请重新输入")

# print("登录成功")


# for num in range(10):
#     if num == 5:
#         break;
#     print(num)

for num in range(10):
    if num % 2 == 0:
        continue;
    print(num)