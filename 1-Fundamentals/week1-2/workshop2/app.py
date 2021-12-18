from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


#Task 2#
print("          === Automated Teller Machine ===          ")
name = input("Enter name to register: ").lower()
pin = input("Enter Pin ")
balance = 0
print(name, "has been registered with a starting balance of", "$" + str(balance))

#Task 3#
print("          === Automated Teller Machine ===          ")
while True:
    print("LOGIN")
    if name is not None and pin is not None:
        name_i = input("Enter name: ").lower()
        pin_i = input("Enter pin: ")
        if name == name_i and pin == pin_i:
            print("Login Succesful!")
            break
        else:
            print("Invalid Credentials!")


while True:
    atm_menu(name)
    option = input("Choose an option: ").lower()
    if option == "1" or option == "balance":
        account.show_balance(balance)
    elif option == "2" or option == "deposit":
        balance = account.deposit(balance)
        print("Current Balance: ", "$" + str(balance))
    elif option == "3" or option == "withdraw":
        balance = account.withdraw(balance)
        print("Current Balance: ", "$" + str(balance))
    elif option == "4" or option == "logout":
        account.logout(name)
        break
    else:
        print("Invalid Selection!")
