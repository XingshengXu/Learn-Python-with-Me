from collections import Counter, deque, defaultdict
from collections import OrderedDict, namedtuple

# 1. 创建 Counter 对象
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(data)
print("统计结果:", counter)

# 获取出现频率最高的元素
print("最常见的元素:", counter.most_common(2))

# 更新计数器
counter.update(['banana', 'banana', 'grape'])
print("更新后的统计:", counter)

# 删除计数器中的元素
del counter['apple']
print("删除后的计数器:", counter)

# 计算交集和并集
counter1 = Counter(a=3, b=1)
counter2 = Counter(a=1, b=2, c=3)
print("交集:", counter1 & counter2)
print("并集:", counter1 | counter2)

# 2. 创建deque队列
dq = deque(['a', 'b', 'c'])
print("初始队列:", dq)

# 在两端插入和删除
dq.append('d')  # 右端插入
dq.appendleft('z')  # 左端插入
print("插入后的队列:", dq)

dq.pop()  # 右端删除
dq.popleft()  # 左端删除
print("删除后的队列:", dq)

# 旋转队列
dq.extend(['e', 'f'])
dq.rotate(2)  # 向右旋转两步
print("旋转后的队列:", dq)

# 限制队列长度
dq_limited = deque(maxlen=3)
dq_limited.extend([1, 2, 3])
dq_limited.append(4)  # 超过最大长度时，左端元素会被自动移除
print("有限长度队列:", dq_limited)

# 3. 创建带默认值的defaultdict字典
dd = defaultdict(int)
data = ['apple', 'banana', 'apple']
for item in data:
    dd[item] += 1

print("统计结果:", dd)

# 默认值为列表
dd_list = defaultdict(list)
dd_list['key'].append('value')
print("列表默认值:", dd_list)

# 4. 创建有序OrderedDict字典
od = OrderedDict()
od['a'] = 3
od['c'] = 2
od['b'] = 1
print("有序字典:", od)

# 根据键排序
od_sorted = OrderedDict(sorted(od.items(), key=lambda x: x[0]))
print("按键排序后的字典:", od_sorted)

# 根据值排序
od_sorted_by_value = OrderedDict(sorted(od.items(), key=lambda x: x[1]))
print("按值排序后的字典:", od_sorted_by_value)

# 5. 创建命名元组namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print("坐标:", p)
print("x 坐标:", p.x)
print("y 坐标:", p.y)

# 转换为字典
print("转换为字典:", p._asdict())

# 替换字段值
p_new = p._replace(x=100)
print("替换后的命名元组:", p_new)
