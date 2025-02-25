import itertools

# ex1
counter = itertools.count()
# for num in counter:
#     print(num)  # 会无限循环慎用！

print(next(counter))
print(next(counter))
print(next(counter))

# ex2
counter = itertools.count(start=5, step=5)
print(next(counter))
print(next(counter))
print(next(counter))

# ex3
colors = itertools.cycle(["红", "绿", "蓝"])
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))

# ex4
repeat_2 = itertools.repeat(2, times=3)
print(list(repeat_2))

# ex5
squares = map(pow, range(10), itertools.repeat(2))
print(list(squares))

# ex6
letters = ["A", "B", "C", "D"]
result = itertools.combinations(letters, 2)
print(list(result))

# ex7
result = itertools.combinations_with_replacement(letters, 2)
print(list(result))

# ex8
letters = ["A", "B", "C", "D"]
result = itertools.permutations(letters, 2)
print(list(result))

# ex9
result = itertools.product(letters, repeat=2)
print(list(result))

# ex10
a = [1, 2, 3]
b = ['a', 'b']
print(list(zip(a, b)))

result = itertools.zip_longest(a, b)
print(list(result))

# ex11
result = itertools.zip_longest(a, b, fillvalue="空")
print(list(result))

# ex12
list1 = ["A", "B", "C"]
list2 = [1, 2, 3]

result = itertools.chain(list1, list2)
print(list(result))

# ex13
numbers = range(10)

result = itertools.islice(numbers, 2, 8, 2)
print(list(result))

# ex14
people = [
    {"name": "小明", "city": "北京"},
    {"name": "小红", "city": "北京"},
    {"name": "张伟", "city": "上海"},
    {"name": "李强", "city": "上海"},
    {"name": "王芳", "city": "北京"},
]

# 按 "city" 进行分组
people.sort(key=lambda x: x["city"])  # 必须先排序
grouped = itertools.groupby(people, key=lambda x: x["city"])

for key, group in grouped:
    print(key, list(group))
