import random

print("Rock, paper or scissors?")
choice = input()

# [0] Rock
# [1] Paper
# [2] Scissors

match choice:
    case "rock":
        player = 0
    case "paper":
        player = 1
    case "scissors":
        player = 2
        
cpu = random.randint(0, 2)

if player > cpu or (player == 0 and cpu == 2):
    win = "YOU WON!"
elif player == cpu:
    win = "YOU TIED!"
else:
    win = "YOU LOST!"
    
moves = ["rock", "paper", "scissors"]
print(f"You played {choice} and the computer played {moves[cpu]}.")
print(win)