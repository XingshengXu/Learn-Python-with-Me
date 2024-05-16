import cProfile
import pstats

# ex2 复杂函数分析


def calculate_sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def large_prime(limit):
    primes = []
    num = 2
    while len(primes) < limit:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes[-1]


def main():
    large_prime(10000)
    fibonacci(30)
    calculate_sum_of_squares(1000000)


cProfile.run('main()')

# 读取性能分析文件并排序
# cProfile.run('main()', 'profile_stats')
# p = pstats.Stats('profile_stats')
# p.sort_stats('cumulative').print_stats(10)

# tuna进行可视化
# cProfile.run('main()', 'main.prof')

# def fibonacci(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         return n
#     memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
#     return memo[n]
