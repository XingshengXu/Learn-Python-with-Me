# if-elif-else statement
is_hot = True
is_cold = False
if is_hot:
    print("It's a hot day!")
elif is_cold:
    print("It's a cold day!")
else:
    print("It's a good day!")

# Comparison Operators
a = 10
b = 20
c = 10

# greater than
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

# less than
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# equal to
if a == c:
    print("a is equal to c")
else:
    print("a is not equal to c")

# not equal to
if a != b:
    print("a is not equal to b")
else:
    print("a is equal to b")

# Logical Operators
a = 10
b = 20
c = 30

# and operator
if a < b and a < c:
    print("a is the smallest")
else:
    print("a is not the smallest")

# or operator
if a < b or a > c:
    print("a is either less than b or greater than c")
else:
    print("a is not less than b and not greater than c")

# not operator
if not (a > b):
    print("a is not greater than b")
else:
    print("a is greater than b")

# Single-line if-else Statement
age = 18
if age > 80:
    is_old = True
else:
    is_old = False

# is_old = True if age > 80 else False
print(is_old)
