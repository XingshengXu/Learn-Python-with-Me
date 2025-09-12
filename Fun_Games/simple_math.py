import operator
import random
import time

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}

# 调整算术难度
MIN_OPERAND = 2
MAX_OPERAND = 20
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    op_symbol = random.choice(list(OPERATORS.keys()))
    op_func = OPERATORS[op_symbol]

    expr = f"{left} {op_symbol} {right}"
    answer = op_func(left, right)
    return expr, answer


wrong = 0
input("请按回车键开始!")
print("----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("问题#" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print("好样的🎉总共完成时间", total_time, f"秒! 一共答错{wrong}次!")
