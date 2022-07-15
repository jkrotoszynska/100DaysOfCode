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
=========
''', '''
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


end_of_game = False
word_list = ["aardvark", "baboon", "camel", "cow", "apple", "watermelon", "bathtube", "happy", "unicorn", "button", "pillow"]
chosen_word = random.choice(word_list)
chosen_word = list(chosen_word)
word_length = len(chosen_word)

lives = 6

display = []
for _ in range(len(chosen_word)):
     display.append("_")

while display != chosen_word:
     guess = input("Guess a letter: ").lower()

     if guess not in chosen_word:
          lives -= 1
          print(stages[lives])
          
          if lives == 0:
               print("You lose...")
               print(f"The word was: {''.join(chosen_word)}")
               exit()

     for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
            display[position] = letter

     print(''.join(display))
     
     if(display == chosen_word):
          print("You win!")