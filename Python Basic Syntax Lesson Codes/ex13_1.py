# Converting between numeric types
x = 5
y = float(x)
print(y)

x = 5.6
y = int(x)
print(y)

# Converting between string and numeric types
x = "123"
y = int(x)
print(y)

x = 123
y = str(x)
print(y)

# Converting between lists and tuples
x = [1, 2, 3]
y = tuple(x)
print(y)

x = (1, 2, 3)
y = list(x)
print(y)

# Converting between lists and strings
x = "hello"
y = list(x)
print(y)

x = ['h', 'e', 'l', 'l', 'o']
y = "".join(x)
print(y)

# Converting between dictionaries and lists of tuples
x = {'a': 1, 'b': 2, 'c': 3}
y = list(x.items())
print(y)

x = [('a', 1), ('b', 2), ('c', 3)]
y = dict(x)
print(y)

# Converting between sets and lists
x = [1, 2, 3, 1, 2, 3]
y = set(x)
print(y)

x = {1, 2, 3}
y = list(x)
print(y)
