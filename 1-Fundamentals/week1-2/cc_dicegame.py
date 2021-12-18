import random

high_score = 0


def dice_game():
    while True:
        global high_score
        print("Current High Score:", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")

        selection = str(input("Enter your choice: ")).lower()
        dice = range(1, 7, 1)

        if selection == 1 or selection == "1" or selection == "Roll Dice":
            roll_1 = random.choice(dice)
            roll_2 = random.choice(dice)
            print("\nYou roll a....", roll_1)
            print("You roll a....", roll_2, "\n")
            score_total = roll_1 + roll_2
            print("You have rolled a total of: ", score_total, "\n")
            if score_total > high_score:
                print("New high score!\n")
                high_score = score_total
            else:
                print("Better luck next time.... Play Again?\n")

        if selection == 2 or selection == "2" or selection == "Leave Game":
            print("Goodbye!")
            exit = True
            break

dice_game()
