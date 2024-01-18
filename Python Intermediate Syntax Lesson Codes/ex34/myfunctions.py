def add(x, y):
    """加法函数"""
    return x + y


def subtract(x, y):
    """减法函数"""
    return x - y


def multiply(x, y):
    """乘法函数"""
    return x * y


def divide(x, y):
    """除法函数"""
    if y == 0:
        raise ValueError("除数不能为0")
    return x / y
