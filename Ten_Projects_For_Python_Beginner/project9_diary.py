def show_menu():
    print("\n日记本")
    print("1. 记录新日记")
    print("2. 查看所有日记")
    print("3. 退出")


def write_diary():
    date = input("请输入日期 (如 2024-02-03): ")
    entry = input("输入你的日记内容:\n")
    with open("diary.txt", "a", encoding="utf-8") as file:
        file.write(f"{date}: {entry}\n")
    print("日记已保存。")


def read_diary():
    try:
        with open("diary.txt", "r", encoding="utf-8") as file:
            print("\n你的日记:")
            print(file.read())
    except FileNotFoundError:
        print("暂无日记记录。")


while True:
    show_menu()
    choice = input("请选择操作: ")

    if choice == "1":
        write_diary()
    elif choice == "2":
        read_diary()
    elif choice == "3":
        print("退出日记本。")
        break
    else:
        print("无效选择，请重新输入。")
