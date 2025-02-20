gameover = "Wrong choice, game over."

print("Welcome to Treasure Island. Your mission is to find the treasure.")
choice1 = input("You're at a crossroad. Would you like to go left or right? ")

if(choice1 == "right"):
    print(gameover)
elif(choice1 == "left"):
    choice2 = input("There is a river. Would you like to swim across or wait for a boat? ")
    if(choice2 == "swim"):
        print(gameover)
    elif(choice2 == "wait"):
        choice3 = input("You face three doors. Would you like to open the red, blue or yellow door? ")
        if(choice3 == "red" or choice3 == "blue"):
            print(gameover)
        elif(choice3 == "yellow"):
            print("Congratulations, you won!")
        else:
            print("Unexpected argument.")
    else:
        print("Unexpected argument.")
else:
    print("Unexpected argument.")
