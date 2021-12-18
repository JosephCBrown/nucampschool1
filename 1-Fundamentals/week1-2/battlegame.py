wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"
exit = "Goodbye!"

wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 1000

wizard_damage = 150
elf_damage = 100
human_damage = 20
orc_damage = 1000

dragon_hp = 300
dragon_damage = 50


while True:
    print("1)  Wizard")
    print("2)  Elf")
    print("3)  Human")
    print("4)  Orc")
    print("5)  Exit")
    character = str(input("Choose your character: ")).lower()
    if character == "1" or character == "wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2" or character == "elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3" or character == "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    elif character == "4" or character == "orc":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
        break
    else:
        print("Unknown character")
print("You have chosen the character: " + character)
print("Health: ", my_hp)
print("Damage: ", my_damage)


while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the dragon!")
    print("The Dragon's hitpoints are now: ", dragon_hp)
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break

    my_hp = my_hp - dragon_damage
    print("The Dragon strikes back at ", character)
    print("The", character, "'s hitpoints are now: ", my_hp)

    if my_hp <= 0:
        print("The", character, "has lost the battle")
        break


"""while True:
    if character != "5" or character != "exit":
        print("Would you like to play again?")
        break"""
