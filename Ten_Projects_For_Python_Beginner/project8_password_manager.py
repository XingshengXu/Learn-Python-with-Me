passwords = {}


def show_menu():
    print("\n密码管理器")
    print("1. 添加账号密码")
    print("2. 查找账号密码")
    print("3. 删除账号密码")
    print("4. 显示所有账号")
    print("5. 退出")


def add_password():
    account = input("请输入账号名称: ")
    password = input("请输入密码: ")
    passwords[account] = password
    print(f"账号 {account} 的密码已存储。")


def find_password():
    account = input("请输入要查找的账号: ")
    if account in passwords:
        print(f"{account} 的密码是: {passwords[account]}")
    else:
        print("该账号不存在。")


def delete_password():
    account = input("请输入要删除的账号: ")
    if account in passwords:
        del passwords[account]
        print(f"账号 {account} 已删除。")
    else:
        print("该账号不存在。")


def view_accounts():
    if passwords:
        print("\n已存储的账号:")
        for account in passwords.keys():
            print(account)
    else:
        print("暂无存储的账号。")


while True:
    show_menu()
    choice = input("请选择操作: ")

    if choice == "1":
        add_password()
    elif choice == "2":
        find_password()
    elif choice == "3":
        delete_password()
    elif choice == "4":
        view_accounts()
    elif choice == "5":
        print("退出密码管理器。")
        break
    else:
        print("无效选择，请重新输入。")
