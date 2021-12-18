import donations_pkg


def show_homepage():
    print("\n    === DonateMe Homepage ===     ")
    print("---------------------------------------")
    print("|   1. Login    | 2.   Register       |")
    print("---------------------------------------")
    print("|   3. Donate   | 4.  Show Donations  |")
    print("---------------------------------------")
    print("|           5.   Exit                 |")
    print("---------------------------------------")


def donate(username):
    donation_amt = float(input("\nEnter amount to donate: "))
    donation = str(username) + " donated $" + str(donation_amt)
    print("Thank you for your donation!")
    return donation


def show_donations(donations):
    print("\n--- All Donations ---")
    if donations == []:
        print("Currently, there are no donations.")
        return ""
    for donation in donations:
        print(str(donation))
