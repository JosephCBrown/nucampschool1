import random


def guess_random_number(tries, start, stop):
    r1 = random.randint(start, stop)
    while tries > 0:
        print(f"Number of tries remaining: {tries}")
        guess = int(input(f"Guess a number between 0 and 10: "))
        if guess == r1:
            print(f"You guessed the correct number!")
            return
        if guess < r1:
            print(f"Guess higher!")
        if guess > r1:
            print(f"Guess lower!")
        tries -= 1
        if tries == 0:
            print(f"You have failed to guess the number: {r1}")
            return

guess_random_number(5, 0, 11)
