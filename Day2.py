### This is the final project for Day 2. Name: Tip Calculator
##Program Start
#Program Greeting
print("Welcome to the tip calculator!")

#Take in total_bill
total_bill = float(input("What was the total bill? $"))

#Take in Tip percentage
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

#Take in amount of people
people = int(input("How many people to spit the bill? "))

#Do the calculations
split_bill = round((total_bill + (total_bill * (percent/100 + 1))) / people, 2)

#Output the results
print(f"Each person should pay ${split_bill}")