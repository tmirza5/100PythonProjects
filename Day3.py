#Greeting

print('Welcome to the Tresure Island.\nYour mission is to find the tresure island')

#Option 1

op1 = input("You're at a crossroads. Do you wish to go left or right?")

play = True

while play == True:
    if op1 == "right":

        print("Game Over!")

        play == False
    elif op1 == "left":

        op2 = input("You come to a lake. There is an island in the middle of the lake. Type 'Wait' if you wish to wait for a boat. Type 'Swim' if you with to swim")

        if op2 == "Swim":

            print("Game Over") 

            play = False
        elif op2 == "Wait":
            op3 = input("You make it to the tresure island unharmed. There is 3 doors, one Yellow, one red, one blue. Which one do you go in?")

            if op3 == "red": 

                print("Game Over!")

                play = False
            
            elif op3 == "blue":
                print("Game Over!")
                
            elif op3 == "yellow":
                print("You get the treasue and enjoy a life filled with prosperity!")
                break
