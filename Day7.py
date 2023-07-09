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
print(display)

#Ask user to guess a letter
guess = input("Guess a letter: ").lower()

#Check if that letter is in the word
iteration = 0
for letter in check:
    iteration += 1
    if letter == guess:
        display[iteration-1] = letter
    else:
        continue

print(display)
