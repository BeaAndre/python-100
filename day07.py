<<<<<<< HEAD
import random

##########
# VARIABLES
##########

wordList = [ "apple", "banana", "cat", "dog", "elephant", "flower", "grape", "house", "island", "jungle", "kitten", "lemon", "mountain", "notebook", "orange", "pencil", "queen", "river", "sunflower", "tree", "umbrella", "violin", "window", "xylophone", "yogurt", "zebra", "angry", "brave", "calm", "delightful", "eager", "famous", "gentle", "happy", "intelligent", "joyful", "kind", "lively", "mysterious", "nice", "optimistic", "patient", "quiet", "radiant", "strong", "talented", "unique", "vibrant", "wonderful", "youthful", "zany", "adventure", "backpack", "castle", "dragon", "eagle", "forest", "garden", "horizon", "iceberg", "journal", "kangaroo", "library", "moon", "nebula", "ocean", "panda", "quasar", "rainbow", "star", "turtle", "unicorn", "valley", "waterfall", "xenon", "yawn", "zephyr", "affectionate", "bitter", "curious", "dreary", "elegant", "funky", "graceful", "hopeful", "imaginative", "jazzy", "keen", "lavish", "melancholy", "nostalgic", "ornate", "peaceful", "quirky", "romantic", "silly", "tranquil", "unusual", "vivid", "whimsical" ]

# Chooses a random word from the list at runtime
word = wordList[random.randint(0, len(wordList) - 1)]

hidden = []
used = []

lives = 5

won = False
lost = False

##########
# FUNCTIONS
##########

# Hides the word using underscores for each letter, puts it in a list   
def getWordHidden():
    for i in word:
        hidden.append('_ ')

# Removes one life
def loseLife():
    global lives, lost
    if(lives > 1):
        lives -= 1
        print(f"You lost a life. You have {lives} left.")  
    else:
        lost = True
        print("You have no lives left. GAME OVER." + f"\nYour word was {word}.")

# Checks if the given character belongs to the word
def isInWord(char):
    found = False
    
    for i, element in enumerate(word):
        if(element == char):
            hidden[i] = char
            found = True
            
    if(not found):
        loseLife()          

# Returns the currently discovered word as a string
def hiddenString():
    return "".join(hidden)

##########
# MAIN
##########

print("Welcome to HANGMAN. Guess the following word:")
getWordHidden()

while(not lost and ('_' in hiddenString())):
    print("\n" + hiddenString())
    guess = input("Guess a letter > ")
    
    if(guess in used):
        print("You already tried that letter.")
    else:
        used.append(guess)
        isInWord(guess)
        if(not '_' in hiddenString()):
            print(f"You WON! The word was {word}.")
=======
import random

##########
# VARIABLES
##########

wordList = [ "apple", "banana", "cat", "dog", "elephant", "flower", "grape", "house", "island", "jungle", "kitten", "lemon", "mountain", "notebook", "orange", "pencil", "queen", "river", "sunflower", "tree", "umbrella", "violin", "window", "xylophone", "yogurt", "zebra", "angry", "brave", "calm", "delightful", "eager", "famous", "gentle", "happy", "intelligent", "joyful", "kind", "lively", "mysterious", "nice", "optimistic", "patient", "quiet", "radiant", "strong", "talented", "unique", "vibrant", "wonderful", "youthful", "zany", "adventure", "backpack", "castle", "dragon", "eagle", "forest", "garden", "horizon", "iceberg", "journal", "kangaroo", "library", "moon", "nebula", "ocean", "panda", "quasar", "rainbow", "star", "turtle", "unicorn", "valley", "waterfall", "xenon", "yawn", "zephyr", "affectionate", "bitter", "curious", "dreary", "elegant", "funky", "graceful", "hopeful", "imaginative", "jazzy", "keen", "lavish", "melancholy", "nostalgic", "ornate", "peaceful", "quirky", "romantic", "silly", "tranquil", "unusual", "vivid", "whimsical" ]

# Chooses a random word from the list at runtime
word = wordList[random.randint(0, len(wordList) - 1)]

hidden = []
used = []

lives = 5

won = False
lost = False

##########
# FUNCTIONS
##########

# Hides the word using underscores for each letter, puts it in a list   
def getWordHidden():
    for i in word:
        hidden.append('_ ')

# Removes one life
def loseLife():
    global lives, lost
    if(lives > 1):
        lives -= 1
        print(f"You lost a life. You have {lives} left.")  
    else:
        lost = True
        print("You have no lives left. GAME OVER." + f"\nYour word was {word}.")

# Checks if the given character belongs to the word
def isInWord(char):
    found = False
    
    for i, element in enumerate(word):
        if(element == char):
            hidden[i] = char
            found = True
            
    if(not found):
        loseLife()          

# Returns the currently discovered word as a string
def hiddenString():
    return "".join(hidden)

##########
# MAIN
##########

print("Welcome to HANGMAN. Guess the following word:")
getWordHidden()

while(not lost and ('_' in hiddenString())):
    print("\n" + hiddenString())
    guess = input("Guess a letter > ")
    
    if(guess in used):
        print("You already tried that letter.")
    else:
        used.append(guess)
        isInWord(guess)
        if(not '_' in hiddenString()):
            print(f"You WON! The word was {word}.")
>>>>>>> 404d2aba1d8756b0758e3f36ce0fc839045b0ecb
