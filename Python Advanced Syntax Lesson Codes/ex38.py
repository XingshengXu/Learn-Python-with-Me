# 不使用海象运算符的代码：
input_str = input("请输入一个字符串: ")
while input_str != 'quit':
    print(f"您输入的是: {input_str}")
    input_str = input("请输入一个字符串: ")

# 使用海象运算符的代码：
while (input_str := input("请输入一个字符串: ")) != 'quit':
    print(f"您输入的是: {input_str}")

# 不使用海象运算符的代码：
user_input = input("请输入一个数字: ")
number = int(user_input)
if number > 10:
    print("这个数字大于10。")

# 使用海象运算符的代码：
if (number := int(input("请输入一个数字: "))) > 10:
    print("这个数字大于10。")

# 循环解包中忽略值
students = [('小红', '001', 85), ('小明', '002', 90), ('小李', '003', 95)]
for name, _, score in students:
    print(f"{name} achieved a score of {score}")

# 函数返回值中忽略值


def get_user_info():
    return ("小红", 25)


_, age = get_user_info()
print(f"User age is {age}")

# 一百万
million = 1000000

# 加下划线
million = 1_000_000

# 十亿
billion = 1_000_000_000

# 当然数字也可以带小数点
amount = 123_456.78

# Docstring注释文档


def add_numbers(a, b):
    """
    计算并返回两个数的和。

    参数：
        a (int): 第一个加数。
        b (int): 第二个加数。

    返回：
        int: 两个加数的和。
    """
    return a + b


# 访问并打印函数的Docstring
print(add_numbers.__doc__)

# 传统的if-else语句
age = 20
if age >= 18:
    status = "成年"
else:
    status = "未成年"

# 使用三元条件运算符
status = "成年" if age >= 18 else "未成年"

# 使用链式比较运算符
x = 15
if 10 <= x <= 20:
    print("x 在范围内。")
else:
    print("x 不在范围内。")

# 也可以使用and来连接比较
x = 15
if x >= 10 and x <= 20:
    print("x 在范围内。")
else:
    print("x 不在范围内。")

# 传统方法使用临时变量
a = 5
b = 10
temp = a
a = b
b = temp

# Python的优雅方式
a = 5
b = 10
a, b = b, a

# 循环的else子句
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num < 0:
        print("发现负数")
        break
else:
    print("列表中没有负数")
