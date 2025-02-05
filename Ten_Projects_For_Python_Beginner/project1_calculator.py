def calculator():
    print("欢迎使用简单计算器！")
    print("可用运算符：+、-、*、/、%（取余）、**（幂）")

    while True:
        try:
            num1 = float(input("请输入第一个数字: "))
            operator = input("请输入运算符 (+, -, *, /, %, **): ")
            num2 = float(input("请输入第二个数字: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("错误：不能除以 0")
                    continue
                result = num1 / num2
            elif operator == '%':
                result = num1 % num2
            elif operator == '**':
                result = num1 ** num2
            else:
                print("无效的运算符，请重新输入。")
                continue

            print(f"计算结果: {num1} {operator} {num2} = {result}")

        except ValueError:
            print("错误：请输入有效的数字！")

        choice = input("是否继续计算？(y/n): ").lower()
        if choice != 'y':
            print("退出计算器。")
            break


if __name__ == "__main__":
    calculator()
