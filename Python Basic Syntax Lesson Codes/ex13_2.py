# Immutable Data
a = 123
b = a
print(f'address_a: {id(a)}, address_b: {id(b)}', a is b)

b += 1
print(f'address_a: {id(a)}, address_b: {id(b)}', a is b)

a = '123'
b = a
print(f'address_a: {id(a)}, address_b: {id(b)}', a is b)
b += '4'
print(f'address_a: {id(a)}, address_b: {id(b)}', a is b)

# Mutable Data
a = [1, 2, 3]
b = a
print(f'address_a: {id(a)}, address_b: {id(b)}', a is b)
b.append(4)
print(f'address_a: {id(a)}, address_b: {id(b)}', a is b)

a = {1, 2, 3}
b = a
print(f'address_a: {id(a)}, address_b: {id(b)}', a is b)
b.add(4)
print(f'address_a: {id(a)}, address_b: {id(b)}', a is b)
