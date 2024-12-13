import re

# 匹配字符串
result = re.match(r"hello", "hello world")
if result:
    print("匹配成功:", result.group())
else:
    print("匹配失败")

# 搜索字符串
result = re.search(r"world", "hello world")
if result:
    print("匹配成功:", result.group())
else:
    print("匹配失败")

# 查找所有匹配项
numbers = re.findall(r"\d+", "我的电话号码是123456789，邮编是100010")
print("找到的所有数字:", numbers)

# 替换字符串
text = "我的电话号码是123456789"
result = re.sub(r"\d", "*", text)
print("替换后的字符串:", result)

# 分割字符串
text = "苹果,橙子 香蕉;西瓜"
result = re.split(r"[ ,;]", text)
print("分割后的列表:", result)

# 编译正则表达式
pattern = re.compile(r"\d+")
text = "123 hello 456"
matches = pattern.findall(text)
print("找到的数字:", matches)
