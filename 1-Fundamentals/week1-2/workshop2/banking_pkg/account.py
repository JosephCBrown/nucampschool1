# task 4
def show_balance(balance):
    print("Current Balance: ", "$" + str(float(balance)))


def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    d_balance = balance + amount
    return float(d_balance)


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    new_balance = balance - amount
    return float(new_balance)


def logout(name):
    print("Goodbye " + name + "!")
    exit = True
