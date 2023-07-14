# Quiz
a = [1, 2, 3]
b = a
b.append(4)
print(a, b)

# copy()
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a, b)

# count and in/not in
my_list = [1, 2, 2, 2, 3]
print(my_list.count(2))
print(2 in my_list)
