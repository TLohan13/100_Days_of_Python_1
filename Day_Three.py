# Introduction
print("Welcome to Treasure Island! ~ THE GAME  ~")
print("Can you find the Treasure?")

# First option. Made it more user-friendly by converting input to lower.
choice1 = input(
    'You\'re at a crossroads. Your phone has died. No more google maps. Type "left" or "right".').lower()

# Left is the correct answer.
if choice1 == "left":

    # Choice 2 input. Had to add "\" and single quotes to allow double quotes around options.
    choice2 = input(
        'You\'ve arrived at a lake with an island in the middle. Type "wait" to wait for a boat. Type "swim" to swim to the island.').lower()

    # Waiting is the correct choice.
    if choice2 == "wait":

        # Choice 3 input. Had to add "\" and single quotes to allow double quotes around options.
        choice3 = input(
            "You made it to the island. There is a house with 3 doors - One red, one yellow and one blue. Which color are you going to choose? ").lower()

        # Yellow is best option!
        if choice3 == "red":
            print("You were attacked by ghosts. Game over!")
        elif choice3 == "yellow":
            print("Congrats! You found the Treasure!")
        elif choice3 == "blue":
            print("You vanished. Game over!")

        # User entered an option that doesn't exist.
        else:
            print("You chose a door that doesn't exist.. Game Over!")

    else:
        print("You got eaten by a giant goldfish!")
else:
    print("You fell into a snake pit. Game over!")
