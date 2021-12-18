
class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name
        print("Your username has been changed to", self.name)

    def change_pin(self, pin):
        self.pin = pin
        print("Your username has been changed to", self.pin)

    def change_password(self, password):
        self.password = password
        print("Your username has been changed to", self.password)


""" Driver Code for Task 1 :

account = User("Bob", "1234", "password")
print(account.name, account.pin, account.password)"""

"""Driver Code for Task 2:

account = User(name="Bob", pin="1234", password="password")
print(account.name, account.pin, account.password)
account.change_name(input("Enter your updated name: "))
account.change_pin(input("Enter your new pin: "))
account.change_password(input("Enter your updated password: "))
print(account.name, account.pin, account.password) """


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, "has an account balance of: ", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.name, "has an account balance of: ", self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(self.name, "has an account balance of: ", self.balance)

    def transfer_money(self, receipent_account, amount):
        print("You are transferring $"+str(amount),
              " To ", receipent_account.name + ".")
        print("Authentication Required")
        correct_pin = input("Enter your PIN: ")
        if self.pin == correct_pin:
            print("Tansfer is Authorized")
            print("Transferring $"+str(amount),
                  " To ", receipent_account.name + ".")
            self.balance = self.balance - amount
            receipent_account.balance = receipent_account.balance + amount
            return True
        else:
            print("Invalid Pin: Transaction Canceled.")
            return False

    def request_money(self, receipent_account, amount):
        print("You are requesting $"+str(amount),
              " from ", receipent_account.name + ".")
        print("Authentication Required")
        correct_pin = input("Enter your PIN: ")
        if self.pin == correct_pin:
            password = input("Enter your password: ")
            if password == self.password:
                print("Request is Authorized")
                print(receipent_account.name, "sent $" + str(amount) + ".")
                self.balance = self.balance + amount
                receipent_account.balance = receipent_account.balance - amount
                return True
            else:
                print("Invalid Pin: Transaction Canceled.")
                return False
        else:
            print("Invalid Pin. Transaction cancelled")
            return False

        # self.receipent_account = receipent_account # Do not need this it seems keeping just in case.


current_user = BankUser(name="Bob", pin="1234", password="password")
my_account = BankUser(name="Joe", pin="3210", password="newpassword")


""" Driver Code for Task 3: 

bank_user = BankUser(name="Bob", pin="1234", password="password")
print(bank_user.name, bank_user.pin, bank_user.password, bank_user.balance)"""

""" Driver Code for Task 4

current_user.show_balance()

current_user.deposit(1000)
# current_user.show_balance()

current_user.withdraw(500)
# current_user.show_balance()"""

""" Driver Code for Task 5 """
current_user.show_balance()
my_account.show_balance()

current_user.deposit(2000)

current_user.transfer_money(my_account, 200)

my_account.show_balance()

current_user.show_balance()

current_user.request_money(my_account, 100)

my_account.show_balance()

current_user.show_balance()
