# Define A Set
my_set = set([1, 2, 3])
my_set = {1, 2, 3}
my_set = {}
print(my_set, type(my_set))

# No Order
my_set = {1, 2, 3}
my_set[0]
print(my_set)

# No Repeat
my_set = {1, 2, 2, 2, 3}
print(my_set)

# in/not in
my_set = {1, 2, 3}
print(1 in my_set)

# Set Methods
set_a = {1, 2, 3}
set_b = {2, 4, 5}

# intersection or &
print(set_a.intersection(set_b))
print(set_a & set_b)

# difference or -
print(set_a.difference(set_b))
print(set_a - set_b)

# union or |
print(set_a.union(set_b))
print(set_a | set_b)
