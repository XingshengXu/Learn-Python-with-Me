# 装饰器

def outer(original_function):  # 装饰器
    def inner():
        print(f"Call someone's name before {original_function.__name__}.")
        return original_function()
    return inner


# def say_hi():
#     print("Hello!")


# display = outer(say_hi)
# display()

# 使用@这个前缀来定义装饰器
# @outer
# def say_hi():
#     print("Hello!")


# say_hi()

# 函数需要输入参数
# def outer(original_function):
#     def inner(*args, **kwargs):
#         print(f"Call someone's name before {original_function.__name__}.")
#         return original_function(*args, **kwargs)
#     return inner


# @outer
# def say_hello(name):
#     print(f"Hello, {name}!")


# say_hello('HongTu')
# say_hello(name='HongTu')

# 用类来定义装饰器
# class Outer:
#     def __init__(self, original_function):
#         self.original_function = original_function

#     def __call__(self, *args, **kwargs):
#         print(f"Call someone's name before {self.original_function.__name__}.")
#         return self.original_function(*args, **kwargs)


# @Outer
# def say_hello(name):
#     print(f"Hello, {name}!")


# say_hello('HongTu')
