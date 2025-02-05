import random

idioms = ["一心一意", "意气风发", "发扬光大", "大公无私", "私心杂念", "念念不忘", "忘恩负义", "义无反顾"]
used_idioms = set()


def idiom_chain():
    print("欢迎来到成语接龙游戏！输入'退出'结束游戏。")

    current_idiom = random.choice(idioms)
    used_idioms.add(current_idiom)
    print(f"游戏开始！第一个成语是: {current_idiom}")

    while True:
        user_input = input("请输入一个成语: ")

        if user_input == "退出":
            print("游戏结束！")
            break

        if user_input in used_idioms:
            print("这个成语已经用过了，请换一个！")
            continue

        if user_input in idioms and user_input[0] == current_idiom[-1]:
            print(f"正确！你接的成语是：{user_input}")
            used_idioms.add(user_input)
            current_idiom = user_input
        else:
            print("成语错误，接龙失败！")
            break


if __name__ == "__main__":
    idiom_chain()
