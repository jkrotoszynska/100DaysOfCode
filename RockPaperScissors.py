import random

from matplotlib.pyplot import sci
symbol = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n")

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
''' 

symbols = [rock, paper, scissors]

print(symbols[int(symbol)])

computer = random.choice(symbols)
print(computer)

