import cProfile

# ex1 单个函数分析


def calculate_sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

# def calculate_sum_of_squares(n):
#     return sum([i**2 for i in range(1, n+1)])


# 生成分析结果文件
cProfile.run('calculate_sum_of_squares(1000000)')
