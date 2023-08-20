import builtins
# Local and Global Variables
x = 'global x'


def test():
    # global x
    # x = 'now, it is global x'
    x = 'local x'
    print(x)


test()
print(x)

# Built-in Variables
# print(dir(builtins))

# Example
# list_length = len(['apple', 'orange', 'banana'])
# print(list_length)

# Re-define Built-in Function


# def len():
#     pass


# len(['apple', 'orange', 'banana'])

# Enclosing Variables


# def outer():
#     x = 'outer x'

#     def inner():
#         # nonlocal x
#         x = 'inner x'
#         print(x)

#     inner()
#     print(x)


# outer()
