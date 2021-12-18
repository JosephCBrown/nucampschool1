
class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


""" Driver Code for Task 1 
account = User("Bob", "1234", "password")
print(account.name, account.pin, account.password)"""
"""Driver Code for Task 2
account = User("Bob", "1234", "password")
print(account.name, account.pin, account.password)"""
