import random


def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    print("猜一个 1 到 100 之间的数字：")

    while True:
        try:
            guess = int(input("请输入你的猜测: "))
            attempts += 1

            if guess < number:
                print("太小了，再试一次。")
            elif guess > number:
                print("太大了，再试一次。")
            else:
                print(f"恭喜你！猜对了，数字是 {number}，总共尝试了 {attempts} 次。")
                break
        except ValueError:
            print("请输入一个有效的数字！")


if __name__ == "__main__":
    guess_number()
