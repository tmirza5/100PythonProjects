### This is the first project for Day 7. Name: Hangman
##Program Start
#Import required modules
import random

#Create word bank
word_bank = ['ardvark', 'baboon', 'camel']

#Choose random word
chosen_word = random.choice(word_bank)

#Ask user to guess a letter
guess = input("Guess a letter: ")

#Check if that letter is in the word
check = list(chosen_word)
for letter in check:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")