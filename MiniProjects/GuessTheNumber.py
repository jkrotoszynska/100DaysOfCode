import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_number(guessing_number, number,attempts):
    if (guessing_number > number):
        print("Too high. \n Guess again.")
        return attempts - 1
    elif (guessing_number < number):
        print("Too low. \n Guess again.")
        return attempts - 1
    else:
        print("You got it!")

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if(level == "easy"):
        return EASY_LEVEL_TURNS
    elif(level == "hard"):
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1,100)
    print("I'm thinking of a number betweem 1 and 100.")

    attempts = difficulty()

    guessing_number = 0
    while guessing_number != number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessing_number = int(input("Make a guess:"))
        attempts = check_number(guessing_number, number, attempts)

        if attempts == 0:
            print("You've run out of guesses. You lose...")
            return
        elif(guessing_number != number):
            print("Guess again...")        

game()