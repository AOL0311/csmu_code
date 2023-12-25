import random

begin_num = 1
end_num = 100

random_number = random.randint(begin_num, end_num)
guess_times = 0

while True:
    guess_times += 1
    print("Guess number")
    guess_number = int(input(f"{guess_times}. {begin_num}-{end_num} =>"))
    if guess_number == random_number:
        print(f"Bingo! You Spend {guess_times} times.")
        break
    elif guess_number < random_number:
        begin_num = guess_number
        print("Too Small!")
        print("-----------------------------------------")
    else:
        end_num = guess_number
        print("Too Big!")
        print("-----------------------------------------")