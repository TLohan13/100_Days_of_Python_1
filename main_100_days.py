import random
import my_module

# DAY 1

# 1) Creat Greeting
print("Welcome to the band name generator!")
# 2) Ask for city that user grew up in - made variable name to store data
city = input("Which city did you grow up in?\n")
# 3) Ask for pet name of pet they've had
pet = input("What is the name of your pet?\n")
# 4) Add City Name and Pet Name
print("Your band name is " + city + " " + pet + "!")


# Day 2

# Welcome Message
print("Welcome to the tip calculator!")
# Input for bill received. Converted to float because bills usually have cents.
bill = float(input("What was the current bill? $"))
# Do not want customers to add "%" to input statement.
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people are you splitting the bill with? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")

# Day 3

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

# Day 4


# random_integer = random.randint(1, 10)
# print(random_integer)

print(my_module.pi)
