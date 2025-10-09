<<<<<<< HEAD
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '?', '+']
numbers = [i for i in range(0, 10)]

print("Welcome to the PyPassword Generator!")
in_letters = int(input("How many letters? "))
in_symbols = int(input("How many symbols? "))
in_nums = int(input("How many numbers? "))

password = []

# Randomize letters
for i in range(0, in_letters):
    letter_pos = random.randint(0, len(letters) - 1)
    password.append(str(letters[letter_pos]))
    
# Randomize symbols
for i in range(0, in_symbols):
    symbol_pos = random.randint(0, len(symbols) - 1)
    password.append(str(symbols[symbol_pos]))

# Randomize numbers
for i in range(0, in_nums):
    num_pos = random.randint(0, len(numbers) - 1)
    password.append(str(numbers[num_pos]))

# Shuffle the password, then save the characters into a new single string to be shown to the user
random.shuffle(password)
finalpass = ""

for i in password:
    finalpass = finalpass + i

print(f"Your new password is: {finalpass}")
=======
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '?', '+']
numbers = [i for i in range(0, 10)]

print("Welcome to the PyPassword Generator!")
in_letters = int(input("How many letters? "))
in_symbols = int(input("How many symbols? "))
in_nums = int(input("How many numbers? "))

password = []

# Randomize letters
for i in range(0, in_letters):
    letter_pos = random.randint(0, len(letters) - 1)
    password.append(str(letters[letter_pos]))
    
# Randomize symbols
for i in range(0, in_symbols):
    symbol_pos = random.randint(0, len(symbols) - 1)
    password.append(str(symbols[symbol_pos]))

# Randomize numbers
for i in range(0, in_nums):
    num_pos = random.randint(0, len(numbers) - 1)
    password.append(str(numbers[num_pos]))

# Shuffle the password, then save the characters into a single string to be shown to the user
random.shuffle(password)
finalpass = ""

for i in password:
    finalpass = finalpass + i

print(f"Your new password is: {finalpass}")
>>>>>>> 404d2aba1d8756b0758e3f36ce0fc839045b0ecb
