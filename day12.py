<<<<<<< HEAD
from os import system
import random

# NUMBER GUESSING GAME

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def set_difficulty(difficulty):
    """Takes the chosen difficulty and returns the corresponding number of attempts."""
    
    if(difficulty == "easy"):
        return EASY_ATTEMPTS
    elif(difficulty == "hard"):
        return HARD_ATTEMPTS
    else:
        return 0
    
def decrease_attempts():
    """Decreases the number of attempts by one."""
    
    return attempts - 1

def process_guess(guess, answer):
    """Compares the user's guess with the real answer and determines which clue to give them (higher/lower)."""
    
    if(guess > answer):
        print("Lower...")
    elif (guess < answer):
        print("Higher...")

# MAIN

print("----- NUMBER GUESSING -----")

print("Choose your difficulty: easy / hard")
diff_choice = input().casefold()
attempts = set_difficulty(diff_choice)

print("I'm thinking of a number between 1 and 100...")
answer = random.randint(1, 100)

endGame = False

if(attempts == 0):
    endGame = True

while(not endGame):
    print(f"You have {attempts} attempts remaining.")
    guess = int(input("Your guess: "))
    attempts = decrease_attempts()
    
    if(guess == answer):
        endGame = True
        print(f"CORRECT! The number was {answer}.")
    else:
        if(attempts > 0):
            process_guess(guess, answer)
        else:
            print(f"You lost! The number was {answer}.")
=======
from os import system
import random

# NUMBER GUESSING GAME

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def set_difficulty(difficulty):
    """Takes the chosen difficulty and returns the corresponding number of attempts."""
    
    if(difficulty == "easy"):
        return EASY_ATTEMPTS
    elif(difficulty == "hard"):
        return HARD_ATTEMPTS
    else:
        return 0
    
def decrease_attempts():
    """Decreases the number of attempts by one."""
    
    return attempts - 1

def process_guess(guess, answer):
    """Compares the user's guess with the real answer and determines which clue to give them (higher/lower)."""
    
    if(guess > answer):
        print("Lower...")
    elif (guess < answer):
        print("Higher...")

# MAIN

print("----- NUMBER GUESSING -----")

print("Choose your difficulty: easy / hard")
diff_choice = input().casefold()
attempts = set_difficulty(diff_choice)

print("I'm thinking of a number between 1 and 100...")
answer = random.randint(1, 100)

endGame = False

while(not endGame):
    print(f"You have {attempts} attempts remaining.")
    guess = int(input("Your guess: "))
    attempts = decrease_attempts()
    
    if(guess == answer):
        endGame = True
        print(f"CORRECT! The number was {answer}.")
    else:
        if(attempts > 0):
            process_guess(guess, answer)
        else:
            print(f"You lost! The number was {answer}.")
>>>>>>> 404d2aba1d8756b0758e3f36ce0fc839045b0ecb
            endGame = True