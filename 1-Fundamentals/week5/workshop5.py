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

# ---driver code test task 1----
# guess_random_number(5, 0, 11)


def guess_random_number_linear(tries, start, stop):
    r1 = random.randint(start, stop)
    c_guess = random.randrange(start, stop)
    print(f"The number for the program to guess is: {r1}")

    while tries > 0:
        for i in [c_guess]:
            print(f"Number of tries remaining: {tries}")
            print(f"The program is guessing... {i}")
            if i == r1:
                return print(f"The program guessed the correct number!")
        tries -= 1
        if tries == 0:
            print(
                f"The program has failed to guess the correct number of: {r1}")
            return -1
    return

# ---driver code test task 2----
#guess_random_number_linear(5, 0, 11)


def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found


def guess_random_num_binary(tries, start, stop):
    r1 = random.randint(start, stop)
    c_guess = [x for x in range(listlength)]
    print(f"Random number to find: {r1}")
    while tries > 0:
        if (binarySearch(c_guess, findnum)) == r1:
            print("Found it! %d" % r1)
        if (binarySearch(c_guess, findnum)) > r1:
            print(f"Guessing lower!")
        if (binarySearch(c_guess, findnum)) < r1:
            print(f"Guessing higher!")
        tries -= 1
        if tries == 0:
            print(
                f"The program has failed to guess the correct number of: {r1}")
    return c_guess


listlength = 101
findnum = random.randrange(0, listlength)
guess_random_num_binary(5, 0, 101)
