import time
# import logging

# 计算函数执行时间


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__}'s running time: {end_time - start_time} second.")
        return result
    return wrapper

# 使用装饰器


# @timer_decorator
# def my_function(n):
#     sum = 0
#     for i in range(n):
#         sum += i
#     return sum


# 调用函数
# my_function(1000000)

# 日志记录
# def logging_decorator(func):
#     def wrapper(*args, **kwargs):
#         logging.info(f"loading function: {func.__name__}")
#         logging.info(f"loading arguments: args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} return result: {result}")
#         return result
#     return wrapper


# logging.basicConfig(level=logging.INFO)

# 使用装饰器


# @logging_decorator
# def add(a, b):
#     return a + b


# @logging_decorator
# def multiply(a, b):
#     return a * b


# 调用函数
# add(3, 4)
# multiply(3, 4)
