from random import randint

EAZY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer is {answer}!")


def set_difficulty():
    level = input("Choose difficulty. Type the 'easy' 'hard': ")
    if level == "easy":
        return EAZY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():

    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Psst, the correct answer is {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Guess a number: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You ran out of guesses. You lose!")
            return
        elif guess != answer:
            print("Guess Again!")


game()
