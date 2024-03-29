#Import library
import random

stages = [
    '''
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
'''
]

#List of words
word_list = ["aardvark", "baboon", "camel"]

#Random word choice
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
lives = 6
win = False

#Fill up the display list
for i in range(len(chosen_word)):
    display += "_"

#Check the process
while not win:
    #User input
    guess = input("Gues a letter: ").lower()

    #Check if the letter is in any place of the word
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess
        print("Nailed it!")
    else:
        lives -= 1
        print(f"Whoops, incorrect!\nYou have {lives} lives left.")

    print(stages[lives])

    #If there are not blank spaces, it means the user has won
    if "_" not in display:
        print(f"You won!\nThe word was {chosen_word}.")
        win = True

    #Check for lives
    if lives <= 0:
        print(f"Game Over!\nThe word was {chosen_word}.")
        break
