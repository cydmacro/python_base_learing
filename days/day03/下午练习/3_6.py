# def lifecycle_gen():
#     print("Stage 1")
#     yield "A"
#     print("Stage 2")
#     yield "B"
#     print("Stage 3")
#     yield "C"
#     print("End of generator")

# gen = lifecycle_gen()

# try:
#     print(next(gen))  # Stage1 -> A
#     print(next(gen))  # Stage2 -> B
#     print(next(gen))  # Stage3 -> C
#     print(next(gen))  # End -> StopIteration
# except StopIteration:
#     print("Generator exhausted")


def natural_numbers():
    num = 1
    while True:
        yield num
        num += 1

# 使用生成器
numbers = natural_numbers()
for _ in range(50):
    print(next(numbers))  # 输出 1, 2, 3, 4, 5