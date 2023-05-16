# Lambda Function
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler(10))
mytripler = myfunc(3)
print(mytripler(10))

# Quiz


def sort_by_last_letter(words):
    return sorted(words, key=lambda word: word[-1])


words = ['apple', 'banana', 'cherry', 'melon']
print(sort_by_last_letter(words))

# Map() Function
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# Filter Function
A = [1, 2, 3, 4, 5]
B = [2, 4]
A = list(filter(lambda x: x not in B, A))
print(A)
