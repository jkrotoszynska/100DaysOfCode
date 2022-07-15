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

#Step 3 
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
chosen_word = list(chosen_word)

#Create blanks
display = []
for _ in range(len(chosen_word)):
     display.append("_")

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while display != chosen_word:
     guess = input("Guess a letter: ").lower()

     #Check guessed letter
     for position in range(len(chosen_word)):
          if chosen_word[position] == guess:
               index = position
               display[index] = guess

     print(display)
     
     if(display == chosen_word):
          print("You win!")