# Define A Dictionary
my_dict = dict([('first', 1), ('second', 2), ('third', 3)])
my_dict = dict(first=1, second=2, third=3)
my_dict = {'first': 1, 'second': 2, 'third': 3}
print(my_dict)

child1 = {
    "name": "Emily",
    "year": 2004
}
child2 = {
    "name": "Daniel",
    "year": 2007
}
child3 = {
    "name": "Jack",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)

# No repeat
my_dict = {
    'name': 'HongTu',
    'age': 16,
    'is_new': True
}

# Index and Get Method
print(my_dict['age'])
print(my_dict['birthday'])
print(my_dict.get('age'))

# Modify Dictionary
my_dict['age'] = 18
my_dict['birthday'] = 'Jan-1-2007'
print(my_dict)

# Update
my_dict.update({'name': 'Daniel', 'age': 20, 'birthday': 'Jun-10-2009'})
print(my_dict)

# Dictionary Methods

# items(), keys(), values()
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

# in/not in
print('name' in my_dict)
