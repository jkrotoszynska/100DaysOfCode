from pydoc import describe
import art
from game_data import data
import random

print(art.logo)

account_a = random.choice(data)
account_b = random.choice(data)
while account_a == account_b:
    account_b = random.choice(data)

# Format the account data into printable format
name = account_a["name"]
description = account_a["description"]
country = account_a["country"]
print(f"Compare A: {name}, {description}, from {country}")

print(art.vs)

name = account_b["name"]
description = account_b["description"]
country = account_b["country"]
print(f"Compare B: {name}, a {description}, from {country}")

# Ask user for a guess
print("Who has more followers? Type 'A' or 'B': ")

# Check if user is correct
#   Get follower count of each account
#   Use if statment to check if user is correct
# Give user feedback on theri guess
# Score keeping
# Make the game repeatable
# Making account at posiotn B become the next account at position A
# Clear the screen between rounds
