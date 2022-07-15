import random
import Hangman_art
import Hangman_words

print(Hangman_art.hangman)

end_of_game = False
word_list = Hangman_words.word_list
chosen_word = random.choice(word_list)
chosen_word = list(chosen_word)
word_length = len(chosen_word)

lives = 6

display = []
for _ in range(len(chosen_word)):
     display.append("_")

while display != chosen_word:
     guess = input("Guess a letter: ").lower()

     if guess in display:
          print("The letter has been guessed")
          continue

     if guess not in chosen_word:
          lives -= 1
          print(Hangman_art.stages[lives])
          print(f"Letter {guess} is not in the word")
          
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