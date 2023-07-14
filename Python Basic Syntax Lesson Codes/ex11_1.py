# Define A Tuple
my_tuple = tuple([1, 2, 3])
my_tuple = ('apple', 1, True)
my_tuple = 1, 2, 3
print(my_tuple, type(my_tuple))

# Unpacking
num1, num2, num3 = my_tuple
print(num1, num2, num3)

# No Index
my_tuple[0] = 5

# Modify A Tuple
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
my_list.append(4)
my_tuple = tuple(my_list)
print(my_tuple)

new_tuple = (4,)
my_tuple += new_tuple
print(my_tuple)

# del my_tuple
print(my_tuple)

# Count and Index
my_tuple = (1, 2, 2, 3)
print(my_tuple.count(2), my_tuple.index(2))
