# 可迭代对象 Iterable
nums = [1, 2, 3]
for num in nums:
    print(num)

print(dir(nums))

# 迭代器 Iterator
# my_list = [1, 2, 3]
# iterator = iter(my_list)
# # print(dir(iterator))

# try:
#     while True:
#         num = next(iterator)
#         print(num)
# except StopIteration:
#     pass

# 生成器 Generator
# def generator():
#     for i in range(5):
#         yield i

# for num in generator:
#     print(num)

# 生成器表达式（Generator Expression）
# generator = (x for x in range(5))

# for num in generator:
#     print(num)

# 生成器和列表的区别
# import sys

# # 创建一个包含大量元素的列表
# large_list = [i for i in range(1000000)]
# print(f"Size of large_list: {sys.getsizeof(large_list)} bytes")

# # 创建一个生成器用于生成大量元素
# large_generator = (i for i in range(1000000))
# print(f"Size of large_generator: {sys.getsizeof(large_generator)} bytes")
