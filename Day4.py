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

#Write your code below this line 👇
print("Welcome, prepare to be defeated in this game of rock, paper scissors")

user = (input("Please type rock, paper or scisors")

choices = [rock, paper, scissors]
game = random.choice(choices)

if game == scissors:
    if user == "scisors":
