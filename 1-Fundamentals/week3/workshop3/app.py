from donations_pkg import homepage, user

database = {"admin": "password123"}
donations = []
authorized_user = ""


while True:
    homepage.show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as: ", authorized_user)
    option = input("Choose an option: ").lower()
    if option == "1" or option == "login":
        username = input("Enter your username: ").lower()
        password = input("Enter your password: ")
        authorized_user = user.login(database, username, password)
    elif option == "2" or option == "register":
        username = input("Enter your username: ").lower()
        password = input("Enter your password: ")
        authorized_user = user.register(database, username)
        if authorized_user != "":
            database[username] = password
    elif option == "3" or option == "donate":
        if authorized_user == "":
            print("You are not logged in")
            continue
        donation = homepage.donate(authorized_user)
        if donation != []:
            donations.append(donation)
    elif option == "4" or option == "show donations":
        homepage.show_donations(donations)
    elif option == "5" or option == "exit":
        print("\nYou are now leaving DonateMe...")
        print("\nThank you, goodbye!\n")
        break
    else:
        print("\nInvalid Selection!")
