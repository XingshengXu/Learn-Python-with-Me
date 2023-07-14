# List Unpacking
fruits = ['apple', 'banana', 'orange']

# fruit_1 = fruits[0]
# fruit_2 = fruits[1]
# fruit_3 = fruits[2]

fruit_1, fruit_2, fruit_3 = fruits
print(fruit_1, fruit_2, fruit_3)

# Multiple Variables Unpacking
fruits = ['apple', 'banana', 'orange', 'pear', 'cherry']
fruit_1, fruit_2, *other_fruits = fruits
fruit_1, *other_fruits, fruit_2 = fruits
print(fruit_1, fruit_2, other_fruits)

# Quiz
a = 1
b = 2
print(a, b)
c = a
a = b
b = c
print(a, b)

# Quiz Using Unpacking
a = 1
b = 2
a, b = b, a
print(a, b)
