import random

random_number = random.randint(1, 100)
guess_times = 0

while True:
    guess_times += 1
    print("Guess number")
    guess_number = int(input(f"{guess_times}. 1-100 =>"))
    if guess_number == random_number:
        print(f"Bingo! You Spend {guess_times} times.")
        break
    elif guess_number < random_number:
        print("Too Small!")
    else:
        print("Too Big!")