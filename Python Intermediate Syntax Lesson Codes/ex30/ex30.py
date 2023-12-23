# 闭包
def outer():
    count = 0

    def inner():  # 闭包函数
        nonlocal count
        count += 1
        return count
    return inner


# 创建一个计数器
# my_counter = outer()

# 使用计数器
# print(my_counter())
# print(my_counter())
# print(my_counter())

# 简便的闭包


# def outer(count):
#     def inner(): # 闭包函数
#         nonlocal count  # count is an enclosing variable
#         count += 1
#         return count
#     return inner


# # 创建一个计数器
# my_counter = outer(0)

# # 使用计数器
# print(my_counter())
# print(my_counter())
# print(my_counter())

# 另一个例子
# def make_multiplier(x):
#     def multiplier(n):  # 闭包函数
#         nonlocal x
#         return n * x
#     return multiplier


# times_three = make_multiplier(3)
# print(times_three(5))
