def fizzbuzz(num):
    for num in range(1, 51):
        if num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0 and num % 5 == 0:
            print("Fizzbuzz")
        else:
            print(num)
    return num


fizzbuzz(50)