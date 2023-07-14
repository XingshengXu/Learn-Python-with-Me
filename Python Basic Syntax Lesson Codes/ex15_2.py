# For Loop Examples
for letter in 'Python':
    print(letter)

fruits = [1, 2, 3]
for fruit in fruits:
    print(fruit)

# Range Function
for num in range(5):
    print(num)

for num in range(1, 5, 2):
    print(num)

for num in range(4, -1, -1):
    print(num)

# Quiz
bill = {
    'apple': 15,
    'orange': 20,
    'banana': 10
}

fruit_type = []
total_price = 0
for fruit, price in bill.items():
    fruit_type.append(fruit)
    total_price += price
print(f'The toal price of {fruit_type} is {total_price}.')
