# a = 10      # int
# print(type(a))
a = "Hello" # 类型动态改变（实际是绑定到新对象）
print(type(a))


# 名称="老王"
# print(名称)


a = 10          # 十进制
b = 0b1010      # 二进制 → 10
c = 1_000_000   # 分隔符增强可读性（Python3.6+）

print(a, b, c)


x = 3.14
y = 2.5e-3      # 0.0025
print(x, y)


is_active = True
print(is_active)
print(int(is_active))  # 1