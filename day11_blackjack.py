<<<<<<< HEAD
from os import system
import random

# BLACKJACK RULES
# Player turns 2 cards to begin, dealer turns 1. Player can hit or stand until satisfied with their hand.
# Dealer then reveals the second card. If their points are below 17, they must hit until equal or above, then stop.
# If either goes over 21 points, it's a bust. The one with the most points wins.
# Number cards are worth the face value, J/Q/K are worth 10, Ace can be worth 1 or 11 depending on whether it would bust the hand.

def get_card(person):
    """Returns a new random card that was not yet on the table, by suit and value. Removes that card from the deck. Adds points to the given person."""
    while(True):
        suit = random.choice(suits)
        val = random.choice(values)
        
        if(not alreadyPlayed(suit, val)):
            break
    
    if(person.lower() == 'player'):
        # Add to cards
        add_playerpoints(val)
    elif(person.lower() == 'dealer'):
        # Add to cards
        add_dealerpoints(val)
    
    deck[suit].remove(val) 
    return suit + val

def alreadyPlayed(suit, value):
    """Returns TRUE if the card has already been played this round, and FALSE if it hasn't and is still in the deck."""
    if value in deck[suit]:
        return False
    else:
        return True

def add_dealerpoints(value):
    """Interprets the card's value and adds the corresponding points to the dealer."""
    ten_pointers = ['J', 'Q', 'K']
    
    if(value in ten_pointers):
        points = 10
    elif(value == 'A'):
        if(get_dealerpoints() + 11 > 21):
            points = 1
        else:
            points = 11
    else:
        points = int(value)
        
    global dealer_points
    dealer_points += points

def add_playerpoints(value):
    """Interprets the card's value and adds the corresponding points to the player."""
    ten_pointers = ['J', 'Q', 'K']
    
    if(value in ten_pointers):
        points = 10
    elif(value == 'A'):
        if(get_playerpoints() + 11 > 21):
            points = 1
        else:
            points = 11
    else:
        points = int(value)
        
    global player_points
    player_points += points

def get_playerpoints():
    """Returns player points."""
    return player_points

def get_dealerpoints():
    """Returns dealer points."""
    return dealer_points

####################
# GAME START
####################

system("cls")

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♠', '♡', '♣', '♢']

endGame = False

while(not endGame):
    endTurn = False
    bust = False
    dealer_bust = False
    
    deck = {key: values[:] for key in suits}
    
    player_points = 0
    dealer_points = 0
    
    print("---------- BLACKJACK ----------")
    print()
    
    print(f"YOUR cards: {get_card('player')}, {get_card('player')}. You have {get_playerpoints()} points.")
    print(f"DEALER's card: {get_card('dealer')}. They have {get_dealerpoints()} points.")
    print()
    
    print("--- PLAYER TURN ---")
    while(not endTurn):
        choice = input("Do you want to HIT or STAND? ")
        
        if(choice.lower() == 'stand'):
            endTurn = True
        elif(choice.lower() == 'hit'):
            print(f"You got a {get_card('player')}. You have {get_playerpoints()} points.")
        if(get_playerpoints() > 21):
            endTurn = True
            bust = True
        
        print()
    
    if(bust):
        print("BUST! You went over 21 points. Game over...")
    else:
        print("--- DEALER TURN ---")
        print(f"DEALER got a {get_card('dealer')}. They have {get_dealerpoints()} points.")        
        while(get_dealerpoints() < 17):
            print("DEALER must hit again.")
            print(f"DEALER got a {get_card('dealer')}. They have {get_dealerpoints()} points.")
        
        print()
        
        if(get_dealerpoints() > 21):
            print("BUST! The dealer went over 21 points. YOU WIN!")
        elif(get_dealerpoints() > get_playerpoints()):
            print("The dealer won. Game over...")
        elif(get_dealerpoints() == get_playerpoints()):
            print("You tied!")
        else:
            print("YOU WIN!")

    print()
    continue_game = input("Do you want to continue playing? Y/N: ")
    
    if(continue_game.lower() == "n" or continue_game.lower() == "no"):
        print("Thanks for playing!")
        endGame = True
    elif(continue_game.lower() == 'y' or continue_game.lower() == 'yes'):
=======
from os import system
import random

# BLACKJACK RULES
# Player turns 2 cards to begin, dealer turns 1. Player can hit or stand until satisfied with their hand.
# Dealer then reveals the second card. If their points are below 17, they must hit until equal or above, then stop.
# If either goes over 21 points, it's a bust. The one with the most points wins.
# Number cards are worth the face value, J/Q/K are worth 10, Ace can be worth 1 or 11 depending on whether it would bust the hand.

def get_card(person):
    """Returns a new random card that was not yet on the table, by suit and value. Removes that card from the deck. Adds points to the given person."""
    while(True):
        suit = random.choice(suits)
        val = random.choice(values)
        
        if(not alreadyPlayed(suit, val)):
            break
    
    if(person.lower() == 'player'):
        # Add to cards
        add_playerpoints(val)
    elif(person.lower() == 'dealer'):
        # Add to cards
        add_dealerpoints(val)
    
    deck[suit].remove(val) 
    return suit + val

def alreadyPlayed(suit, value):
    """Returns TRUE if the card has already been played this round, and FALSE if it hasn't and is still in the deck."""
    if value in deck[suit]:
        return False
    else:
        return True

def add_dealerpoints(value):
    """Interprets the card's value and adds the corresponding points to the dealer."""
    ten_pointers = ['J', 'Q', 'K']
    
    if(value in ten_pointers):
        points = 10
    elif(value == 'A'):
        if(get_dealerpoints() + 11 > 21):
            points = 1
        else:
            points = 11
    else:
        points = int(value)
        
    global dealer_points
    dealer_points += points

def add_playerpoints(value):
    """Interprets the card's value and adds the corresponding points to the player."""
    ten_pointers = ['J', 'Q', 'K']
    
    if(value in ten_pointers):
        points = 10
    elif(value == 'A'):
        if(get_playerpoints() + 11 > 21):
            points = 1
        else:
            points = 11
    else:
        points = int(value)
        
    global player_points
    player_points += points

def get_playerpoints():
    """Returns player points."""
    return player_points

def get_dealerpoints():
    """Returns dealer points."""
    return dealer_points

####################
# GAME START
####################

system("cls")

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♠', '♡', '♣', '♢']

endGame = False

while(not endGame):
    endTurn = False
    bust = False
    dealer_bust = False
    
    deck = {key: values[:] for key in suits}
    
    player_points = 0
    dealer_points = 0
    
    print("---------- BLACKJACK ----------")
    print()
    
    print(f"YOUR cards: {get_card('player')}, {get_card('player')}. You have {get_playerpoints()} points.")
    print(f"DEALER's card: {get_card('dealer')}. They have {get_dealerpoints()} points.")
    print()
    
    print("--- PLAYER TURN ---")
    while(not endTurn):
        choice = input("Do you want to HIT or STAND? ")
        
        if(choice.lower() == 'stand'):
            endTurn = True
        elif(choice.lower() == 'hit'):
            print(f"You got a {get_card('player')}. You have {get_playerpoints()} points.")
        if(get_playerpoints() > 21):
            endTurn = True
            bust = True
        
        print()
    
    if(bust):
        print("BUST! You went over 21 points. Game over...")
    else:
        print("--- DEALER TURN ---")
        print(f"DEALER got a {get_card('dealer')}. They have {get_dealerpoints()} points.")        
        while(get_dealerpoints() < 17):
            print(f"DEALER must hit again.")
            print(f"DEALER got a {get_card('dealer')}. They have {get_dealerpoints()} points.")
        
        print()
        
        if(get_dealerpoints() > 21):
            print("BUST! The dealer went over 21 points. YOU WIN!")
        elif(get_dealerpoints() > get_playerpoints()):
            print("The dealer won. Game over...")
        elif(get_dealerpoints() == get_playerpoints()):
            print("You tied!")
        else:
            print("YOU WIN!")

    print()
    continue_game = input("Do you want to continue playing? Y/N: ")
    
    if(continue_game.lower() == "n" or continue_game.lower() == "no"):
        print("Thanks for playing!")
        endGame = True
    elif(continue_game.lower() == 'y' or continue_game.lower() == 'yes'):
>>>>>>> 404d2aba1d8756b0758e3f36ce0fc839045b0ecb
        system("cls")