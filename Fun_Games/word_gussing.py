import random
from wordlist import words

MAX_ATTEMPTS = 6


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    secret_word = random.choice(words)
    hint = ["_"] * len(secret_word)
    wrong_guesses = 0
    guessed_letters = set()

    print("欢迎来到猜单词游戏!\n")

    while True:
        display_hint(hint)
        print(f"已猜过的字母: {', '.join(sorted(guessed_letters)) or '—'}")
        print(f"剩余尝试次数: {MAX_ATTEMPTS - wrong_guesses}\n")

        guess = input("请输入一个字母: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("请输入一个字母(a-z)。")
            continue

        if guess in guessed_letters:
            print(f"字母 '{guess}' 已经猜过了。")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            for i, ch in enumerate(secret_word):
                if ch == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print(f"字母 '{guess}' 不在单词中。\n")

        if "_" not in hint:
            display_answer(secret_word)
            print("你赢了！🎉")
            break

        if wrong_guesses >= MAX_ATTEMPTS:
            display_answer(secret_word)
            print("你输了！😢")
            break


if __name__ == "__main__":
    main()
