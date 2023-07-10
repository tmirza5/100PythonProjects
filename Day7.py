### This is the final project for Day 7. Name: Hangman
##Program Start
#Import required modules
import random

#Create word bank
word_bank = ['ardvark', 'baboon', 'camel']

#Choose random word
chosen_word = random.choice(word_bank)

#Print the chosen work (for testing)
print(f"Chosen word is {chosen_word}")

#Convert the word into a list
check = list(chosen_word)

#Create the display skeleton
display = []
for letter in check:
    display.append("_")

#Create list of ASCII art to visualise lives left
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


##Game loop
#Set variable "lives" to 6
lives = 6
#Ask user to guess a letter
#Check if that letter is in the word and if there are duplicates of the letter
#Add correctly guessed letter to display and also prints the correct hangman stage


game = True
while game == True:
    if lives == 0:
        game = False
    else:
        iteration = 0
        guess = input("Guess a letter: ").lower()
        if guess in check:
            display[check.index(guess)] = guess
            for letter in check:
                iteration += 1
                if letter == guess:
                    display[iteration-1] = guess

        else:
            lives -= 1
        print(display)
        print(stages[lives])
print("You win!")### This is the final project for Day 7. Name: Hangman
##Program Start
#Import required modules
import random

#Create word bank
word_bank = ['ardvark', 'baboon', 'camel']

#Choose random word
chosen_word = random.choice(word_bank)

#Print the chosen work (for testing)
print(f"Chosen word is {chosen_word}")

#Convert the word into a list
check = list(chosen_word)

#Create the display skeleton
display = []
for letter in check:
    display.append("_")

##Game loop
#Ask user to guess a letter
#Check if that letter is in the word
#Add correctly guessed letter to display

while display != check:
    guess = input("Guess a letter: ").lower()
    iteration = 0
    for letter in check:
        iteration += 1
        if letter == guess:
            display[iteration-1] = letter
        else:
            continue
    print(display)
print("You win!")
