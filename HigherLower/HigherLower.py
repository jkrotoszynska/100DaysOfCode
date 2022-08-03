from pydoc import describe
import art
from game_data import data
import random

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

account_a = random.choice(data)
account_b = random.choice(data)
while account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A:{printable_format(account_a)}")
print(art.vs)
print(f"Compare B:{printable_format(account_b)}")

score = 0
guess = input("Who has more followers? Type 'A' or 'B': ").lower()

a_followers_count = account_a['follower_count']
b_followers_count = account_b['follower_count']

is_correct = check_answer(guess, a_followers_count, b_followers_count)

if is_correct:
    score += 1
    print(f"You're right! Current score: {score}")
else:
    print(f"You lose... Final score: {score}")

# Make the game repeatable
# Making account at posiotn B become the next account at position A
# Clear the screen between rounds
