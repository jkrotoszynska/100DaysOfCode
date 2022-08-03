from pydoc import describe
import art
from game_data import data
import random
import os

def printable_format(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return(f" {name}, a {description}, from {country}")

def check_answer(guess, acc_a, acc_b):
    if acc_a > acc_b:
        return guess == "a"
    elif acc_a < acc_b:
        return guess == "b"

print(art.logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A:{printable_format(account_a)}")
    print(art.vs)
    print(f"Compare B:{printable_format(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers_count = account_a['follower_count']
    b_followers_count = account_b['follower_count']

    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
        game_should_continue = True
        os.system('cls')
    else:
        print(f"You lose... Final score: {score}")
        game_should_continue = False
