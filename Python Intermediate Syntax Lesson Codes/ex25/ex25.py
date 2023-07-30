# 定义文件路径和文件名
import os


dir_path = 'E:\\Your File Path'
file_name = 'test.txt'

file_path = os.path.join(dir_path, file_name)

# 打开/关闭文件
# f = open(file_path, 'r')  # 可以是'r', 'w', 'a', 'r+'等不同的文件模式，默认是'r'
# print(f.name)
# print(f.mode)
# f.close()

# 使用文件管理器处理文件

# with open(file_path, 'r') as f:
#     content = f.read()  # 生成全文
#     # content = f.readlines()  # 生成一个列表
#     # content = f.readline()  # 生成一行内容
# print(content)

# 逐行生成文件
# with open(file_path, 'r') as f:
#     for line in f:
#         print(line, end='')

# 读取前100个字符
# with open(file_path, 'r') as f:
#     read_size = 100
#     content = f.read(read_size)
#     while len(content) > 0:
#         print(content, end='*')  # 为了显示读取过程，使用end=’*’来标记每一处断点
#         content = f.read(read_size)

# 添加文件内容
# with open(file_path, 'a') as f:
#     f.write('This is the end of file.')

# 编写文件
# with open('test2.txt', 'w') as f:
#     f.write('Test')

# with open('test2.txt', 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('R')

# Quiz
# 方法一
# with open(file_path, 'r') as rf:
#     with open('test2.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# 方法二
# with open(file_path, 'r') as rf:
#     with open('test2.txt', 'w') as wf:
#         read_size = 10
#         content = rf.read(read_size)
#         while len(content) > 0:
#             wf.write(content)
#             content = rf.read(read_size)

# 复制图片
# with open('dog.png', 'rb') as rf:
#     with open('dog2.png', 'wb') as wf:
#         for line in rf:
#             wf.write(line)
