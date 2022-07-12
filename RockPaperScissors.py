import random

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

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
print(symbols[user])

computer = random.randint(0,2)
computer_sign = symbols[computer]
print("Computer chose:")
print(computer_sign)

if(user >= 3 or user < 0):
    print("Wrong number!")
elif(user == computer):
    print("It's a draw! Try again...")
elif(user == 0 and computer == 2):
    print("You win!")
elif(user == 2 and computer == 0):
    print("You lose...")
elif(user > computer):
    print("You win!")
elif(user < computer):
    print("You lose...")
