from pydoc import describe
import art
from game_data import data
import random

def printable_format(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return(f" {name}, a {description}, from {country}")

print(art.logo)

account_a = random.choice(data)
account_b = random.choice(data)
while account_a == account_b:
    account_b = random.choice(data)

# Format the account data into printable format

print(f"Compare A:{printable_format(account_a)}")
print(art.vs)
print(f"Compare B:{printable_format(account_b)}")

# Ask user for a guess
decision = input("Who has more followers? Type 'A' or 'B': ")

# Check if user is correct
#   Get follower count of each account
#   Use if statment to check if user is correct
# Give user feedback on theri guess
# Score keeping
# Make the game repeatable
# Making account at posiotn B become the next account at position A
# Clear the screen between rounds
