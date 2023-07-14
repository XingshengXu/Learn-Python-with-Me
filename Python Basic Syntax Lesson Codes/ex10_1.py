# 添加元素
list1 = [1, 2, 3]
list2 = [4, 5]
list1 += list2
print(list1)

# append()
list1 = [1, 2, 3]
list1.append(4)
print(list1)

# insert()
list1 = [1, 2, 4]
list1.insert(2, 3)
print(list1)

# extend()
list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2)
print(list1)

# 去除元素
# remove()
list1 = [1, 2, 3]
list1.remove(3)
print(list1)

# pop()
list1 = [1, 2, 3]
print(list1.pop())
print(list1)

# clear()
list1 = [1, 2, 3]
list1.clear()
print(list1)

# 排序

# reverse()
list1 = [1, 2, 3]
list1.reverse()
print(list1)

# sort()
list1 = [2, 1, 3]
list2 = ['b', 'a', 'c']
list1.sort()
list1.sort(reverse=True)
list2.sort()
list2.sort(reverse=True)
print(list1, list2)

# sorted()
list1 = [2, 1, 3]
list2 = sorted(list1, reverse=True)
print(list1, list2)
