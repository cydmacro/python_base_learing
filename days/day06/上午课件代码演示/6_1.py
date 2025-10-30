#AI⼤模型版-⽂件处理和常⽤模块实战


# file = open("my_file.txt", "w")
# try:
#     file.write("Hello, World!")
# finally:
#     file.close()


# with open("test.txt", "r") as file:
#     #file.write("Hello, World!")
#     content = file.read()
#     print(content)

# 写入多行
# lines = ["Python\n", "Java\n", "C++\n"]
# with open("languages.txt", "w", encoding="utf-8") as f:
#     f.writelines(lines)

# with open("languages.txt", "r", encoding="utf-8") as f:
#     for line in f:          # 自动处理大文件，内存友好
#         print(line.strip())  # 移除换行符


# with open("test.txt", "a", encoding="utf-8") as f:
#     f.write("\n追加的内容")


# with open("test.txt", "r", encoding="utf-8") as f:
#     first_line = f.readline()    # 读取第一行
#     next_lines = f.readlines()   # 读取剩余所有行（返回列表）
#     print(first_line)

with open("1.png", "rb") as src, open("output.png", "wb") as dst:
    dst.write(src.read())  # 复制图片