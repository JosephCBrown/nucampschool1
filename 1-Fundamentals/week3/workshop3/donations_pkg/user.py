def login(database, username, password):

    if username in database:
        if password == database[username].lower():
            print("\nWelcome Back, ", username + "!")
            return username
        print("\nPassword does not match for", username + ".")
        return ""

    print("NO ACCOUNT FOUND, PLEASE REGISTER")
    return ""


def register(database, username):
    if username.lower() in database:
        print("Username already registered")
        return ""

    print("\nUsername " + username, "registered succesfully!")
    return username
