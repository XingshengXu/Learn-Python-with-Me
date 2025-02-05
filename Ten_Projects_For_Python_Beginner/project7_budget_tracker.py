records = []


def show_menu():
    print("\n个人记账本")
    print("1. 添加收入/支出")
    print("2. 查看记录")
    print("3. 计算总余额")
    print("4. 退出")


def add_record():
    try:
        item = input("请输入项目名称 (例如: 午餐、工资): ")
        amount = float(input("请输入金额 (收入填正数，支出填负数): "))
        records.append((item, amount))
        print(f"记录成功: {item} - {amount} 元")
    except ValueError:
        print("错误：请输入正确的金额！")


def view_records():
    if records:
        print("\n当前记录:")
        for index, (item, amount) in enumerate(records, 1):
            print(f"{index}. {item}: {amount} 元")
    else:
        print("\n暂无记录。")


def calculate_total():
    total = sum(amount for _, amount in records)
    print(f"\n总余额: {total} 元")


while True:
    show_menu()
    choice = input("请选择操作: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        view_records()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        print("退出记账本。")
        break
    else:
        print("无效选择，请重新输入。")
