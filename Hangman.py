import random

print('''
888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"   
''')

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#Step 4
end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
chosen_word = list(chosen_word)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

lives = 6
stage = -1

#Create blanks
display = []
for _ in range(len(chosen_word)):
     display.append("_")

print(stages[stage])
while display != chosen_word:
     guess = input("Guess a letter: ").lower()

     if guess not in chosen_word:
          lives -= 1
          stage -=1
          print(stages[stage])
          
          if lives == 0:
               print("You lose...")
               exit()

     for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
            display[position] = letter

         

          #TODO-2: - If guess is not a letter in the chosen_word,
          #Then reduce 'lives' by 1. 
          #If lives goes down to 0 then the game should stop and it should print "You lose."

     print(display)
     
     if(display == chosen_word):
          print("You win!")