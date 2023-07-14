# example
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_of_evens = []
for n in nums:
    if n % 2 == 0:
        squares_of_evens.append(n**2)
print(squares_of_evens)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares_of_evens = [n**2 for n in nums if n % 2 == 0]
# print(squares_of_evens)

# If-else Condition
fruits = ["apple", "banana", "cherry", "orange", "mango"]
newlist = [x for x in fruits if "a" in x]

newlist = [x for x in range(10) if x < 5]
print(newlist)

# Expression
fruits = ["Apple", "Banana", "Cherry", "Orange", "Mango"]
newlist = [x.upper() for x in fruits if x == 'Orange']

newlist = [x.upper() if "e" in x else x.lower() for x in fruits]
print(newlist)

# Map Function
nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
num_list = list(map(abs, nums))
# num_list = [abs(num) for num in nums]
print(num_list)

# Filter Function
items = ['hello', 'world', '3', '5']
filtered_items = list(filter(str.isdigit, items))
# filtered_items = [item for item in items if item.isdigit()]
print(filtered_items)

# Nested List Comprehension
a = [[1, 2], [3, 4]]
new_list = [num for row in a for num in row]
print(new_list)
