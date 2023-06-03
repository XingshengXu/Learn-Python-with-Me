""Python Coding Style: PEP 8""
1. "每个缩进级别使用4个空格"


def greet(name):
    if name:
        print("Hello, " + name + "!")
    else:
        print("Hello, stranger!")


greet("Alice")

2. "最大行长最多79个字符"
"限制所需的编辑器窗口宽度可以并排打开两个文件"
"并且在使用在相邻列中显示两个版本的代码审查工具时效果最好。"

3. "换行应该在运算符之前"
# Wrong:
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

# Correct:
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

4. "import 模块格式"
# Wrong:
import os
import sys
# Correct:
import os
import sys
# Correct:
from subprocess import Popen, PIPE

5. "字符串引号"
print("This is Daniel's house.")

6. "空格"
"在以下情况下避免多余的空格："

a. "紧接在圆括号、方括号或大括号内："
# Correct:
spam(ham[1], {eggs: 2})
# Wrong:
spam(ham[1], {eggs: 2})

b. "在尾随逗号和紧随其后的右括号之间："
# Correct:
my_tuple = (0,)
# Wrong:
my_tuple = (0, )

c. "紧接在逗号、分号或冒号之前："
# Correct:
if x == 4:
    print(x, y)
    x, y = y, x
# Wrong:
if x == 4:
    print(x, y)
    x, y = y, x

d. "在切片中，两个冒号必须应用相同的间距。例外：省略切片参数时，省略空格："
# Correct:
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower + offset: upper + offset]
ham[: upper_fn(x): step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset: upper + offset]
# Wrong:
ham[1: 9], ham[1:9], ham[1:9: 3]
ham[lower:: step]
ham[: upper]

e. "紧接在开始函数调用的参数列表的左括号之前："
# Correct:
spam(1)
# Wrong:
spam(1)

f. "在开始索引或切片的左括号之前："
# Correct:
dct['key'] = lst[index]
# Wrong:
dct['key'] = lst[index]

g. "赋值或运算符："
# Correct:
i = i + 1
submitted += 1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
# Wrong:
i = i + 1
submitted += 1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

7. "注释"
total_energy = potential_energy + kinetic_energy

# Wrong: Add two energy together and store result in the total energy
# Correct: Calculate the total energy of the object

8. "文档字符串"
"PEP 257描述了良好的文档字符串约定"

9. "命名约定"
def my_function()


my_module.py
def MyClass(self)


MY_CONSTANT

10. "使用空的数据结构（字符串、列表、元组等）作为if-else的条件语句"
# Correct:
if not my_list:
if my_list:

    # Wrong:
if len(my_list):
if not len(my_list):

11. "布尔值作为if-else条件语句"
# Correct:
if greeting:
    # Wrong:
if greeting == True:
    # Worst:
if greeting is True:

12. "函数参数"
# Correct:


def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# Wrong:


def complex(real=0.0, imag=0.0):
    return magic(r=real, i=imag)


13. "一致性"
"遵循风格指南的一致性很重要，但是在你的项目中的一致性更重要!"
