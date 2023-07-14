# Quiz
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

# Set Comprehension
numbers = [1, 1, 2, 2, 2, 2, 3, 3, 4, 4]
squared_set = {number ** 2 for number in numbers}
print(squared_set)

# Dictionary Comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_dict = {number: number ** 2 for number in numbers}
print(squared_dict)
