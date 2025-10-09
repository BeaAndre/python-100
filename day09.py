from os import system

####################
# VARIABLES
####################

end = False
sayWelcome = True

bidders = {}

####################
# FUNCTIONS
####################

# Adds a bidder to the dictionary with key NAME and value BID
def addBidder(name, bid):
    bidders[name] = bid

# Returns the name of the bidder with the highest value on the dictionary
def getWinner():
    winner = max(bidders, key = bidders.get)
    return winner

# Prints an error in case the user gives an unexpected input
def printError():
    print("Unexpected argument.")

####################
# MAIN
####################

while(not end):
    # Clears the screen
    system("cls")
    
    # Ensure the program only says welcome to the first user
    if(sayWelcome):
        print("Welcome to the Secret Auction program.")
        sayWelcome = False
    
    name = input("What's your name? ")
    bid = input("What's your bid? $")
    
    # Check if the bid is an integer, stop the program if not
    try:
        checkNumber = int(bid)
    except ValueError:
        printError()
        break  
    
    addBidder(name, int(bid))
    
    moreBidders = input("Are there more bidders? Y/N: ")

    if(moreBidders == "no" or moreBidders == "n"):
        winner = getWinner()
        print(f"The winner is {winner} with a bid of ${bidders[winner]}!")
        end = True
    elif(moreBidders != "yes" and moreBidders != "y"):
        printError()
        break