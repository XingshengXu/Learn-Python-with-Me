import time
import random


def get_random_sentence():
    sentences = [
        "Python is a powerful programming language.",
        "The quick brown fox jumps over the lazy dog.",
        "Coding is both fun and challenging.",
        "Practice makes perfect in typing speed.",
        "Artificial Intelligence is shaping the future."
    ]
    return random.choice(sentences)


def typing_speed_test():
    sentence = get_random_sentence()
    print("请尽快输入以下文本:")
    print(f"\n{sentence}\n")

    input("按 Enter 开始...")
    start_time = time.time()
    user_input = input("请输入: ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    words = len(user_input.split())
    correct_chars = sum(1 for a, b in zip(user_input, sentence) if a == b)
    accuracy = (correct_chars / len(sentence)) * 100

    print(f"\n你花了 {elapsed_time:.2f} 秒")
    print(f"你的打字速度: {words / (elapsed_time / 60):.2f} WPM")
    print(f"准确率: {accuracy:.2f}%")

    if accuracy > 90:
        print("太棒了！你的打字水平很高！")
    elif accuracy > 75:
        print("不错的成绩，但可以更快！")
    else:
        print("加油，多加练习提高速度和准确度！")


if __name__ == "__main__":
    typing_speed_test()
