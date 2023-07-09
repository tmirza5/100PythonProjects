### This is the final project for Day 2. Name: Tip Calculator
##Program Start
#Import required modules
import random

#Create the character lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Greeting
print("Welcome to the PyPassword Generator!")

#Ask the user how many characters they would like in their password.
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Generate the password
#Create an empty string
password = ''

#Get the random set of letters
for _ in range(0, nr_letters+1):
    letter = random.choice(letters)
    password += letter

#Get the random set of symbols
for _ in range(0, nr_symbols+1):
    symbol = random.choice(symbols)
    password += symbol

#Get the random set of numbers
for _ in range(0, nr_numbers+1):
    number = random.choice(numbers)
    password += number

#Shuffle the password
password = list(password)
random.shuffle(password)
shuffled_password = ''
for char in password:
    shuffled_password += char

#Output the password
print(f"Here is your password: {shuffled_password}")