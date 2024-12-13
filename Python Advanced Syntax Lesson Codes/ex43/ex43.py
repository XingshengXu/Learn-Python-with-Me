import random

# 生成1到10之间的随机整数
random_int = random.randint(1, 10)
print("生成的随机整数:", random_int)

# 生成5到15之间的随机浮点数
random_uniform = random.uniform(5, 15)
print("生成的随机浮点数 (5-15):", random_uniform)

# 随机选择元素
names = ["小红", "小明", "小强", "小花"]
random_name = random.choice(names)
print("随机选择的名字:", random_name)

# 从序列中随机抽样
students = ["小红", "小明", "小强", "小花"]
random_students = random.sample(students, 2)
print("随机抽取的学生:", random_students)

# 加权随机选择
# 设置水果列表和相应的权重
fruits = ['苹果', '橙子', '香蕉']
weights = [1, 2, 3]

# 根据权重随机选择 5 个水果
result = random.choices(fruits, weights=weights, k=5)
print("加权随机选择的结果:", result)

# 随机打乱序列
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
random.shuffle(cards)
print("打乱后的牌:", cards)

# 生成随机数种子
random.seed(42)
print("固定种子的随机数:", random.randint(1, 100))
