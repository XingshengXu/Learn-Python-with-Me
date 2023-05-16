# Define A Function
def my_function():
  print('Hello from a function')


my_function()

# Positional Arguments
def my_function(fname, lname):
  print(fname + ' ' + lname)


my_function('Emily', 'Smith')

# Arbitrary Arguments
def my_function(*kids):
  'Arbitrary Arguments'
  print('The youngest child is ' + kids[-1])


my_function('Emily', 'Daniel', 'John')

# Keyword Arguments
def my_function(child3, child2, child1):
  print('The youngest child is ' + child3)


my_function(child1='Emily', child2='Daniel', child3='John')

# Arbitrary Keyword Arguments
def my_function(**name):
  print('His last name is ' + name['lname'])


my_function(fname='Emily', lname='Smith')

# Default Arguments
def my_function(country="Norway"):
  print("I am from " + country)


my_function()
my_function("Japan")
my_function("India")
my_function("Brazil")

# Return A Value from Function
def add(a, b):
  print('Calculating...')
  return a + b


result = add(1, 2)
print(f'The result is {result}.')

# Quiz
def mul_table(row, col):
  for multiplier in range(1, row + 1):
    for multiplicand in range(1, col + 1):
      print(multiplier * multiplicand, end='\t')
    print()


mul_table(9, 9)
