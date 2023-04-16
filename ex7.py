# String Methods
course = 'Learn Python With Me'
print(dir(course))

# format()
name = "HongTu"
age = 16
print("My name is {} and I am {} years old.".format(name, age))

# upper()
print(course.upper())

# lower()
print(course.lower())

# find()
print(course.find('L'))

# replace()
print(course.replace('Python', 'Fun Python'))

# count()
print(course.count('n'))

# in and not in
print('P' in course)
print('P' not in course)
