# Define a List
my_list = [1, 2, 3, 4, 5]
my_list = list('HongTu')
print(my_list)

my_list = ['abc', 10, 3.14, [10], True]
print(my_list)

# List Length
print(len(my_list))

# Index of List
print(my_list[0])
print(my_list[-1])

# Slicing
print(my_list[0:3])
print(my_list[1:])
print(my_list[:5])
print(my_list[:])

# Modify List using Slicing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Delete a List
del thislist
print(thislist)

# 2D List
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m = len(matrix)
n = len(matrix[0])
print(matrix)
print(matrix[0][1])
print(m, n)
