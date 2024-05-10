# LBYL写法
import os


def read_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read()
    else:
        return "File not found."


print(read_file('exists.txt'))
print(read_file('does_not_exist.txt'))

# EAFP写法


# def read_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             return file.read()
#     except FileNotFoundError:
#         return "File not found."


# print(read_file('exists.txt'))
# print(read_file('does_not_exist.txt'))
