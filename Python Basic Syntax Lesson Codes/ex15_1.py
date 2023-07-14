# Guessing Game
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You Win!')
        break
else:
    print('You Lose!')


# Continue Statement
num = 0
while num <= 5:
    num += 1
    if num == 3:
        print('Found!')
        continue
    print(num)
