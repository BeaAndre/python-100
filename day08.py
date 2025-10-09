<<<<<<< HEAD
##########
# VARIABLES
##########

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

end = False

##########
# FUNCTIONS
##########

# Prints an error message 
def printError():
    print("Unexpected argument.")

# Encrypts or decrypts the TEXT using the SHIFT and prints the resulting list as a string
def encrypt(text, shift):
    encrypted = []
    
    # If there is a special symbol (non-letter), adds it directly to the encrypted sentence
    # If adding the shift will overflow the list, calculates the number of characters left to the end of it and adds it at the correct place
    # In case none of the above happens, simply shifts the letter and adds it to the encrypted sentence
    for i in text:
        if(not i in alphabet):
            encrypted.append(i)
        elif(alphabet.index(i) + shift > len(alphabet) - 1):
            missing = len(alphabet) - 1 - (alphabet.index(i))
            encrypted.append(alphabet[shift - missing - 1])
        else:
            encrypted.append(alphabet[alphabet.index(i) + shift])
     
    print("".join(encrypted))

##########
# MAIN
##########

while(not end):
    
    print("----- CAESAR CYPHER -----")
    command = input("Do you want to encrypt or decrypt? ")

    # Checks if the user inserted a viable command
    if (command != "encrypt" and command != "decrypt"):
        printError()
        end = True
    else:
        # Asks for user input: sentence and shift
        print(f"Insert the sentence you want to {command}:")
        sentence = input()
        shift = input("Insert the shift: ")
        
        # Checks if user inserted an integer for the shift, if not ends the program
        try:
            shiftInt = int(shift)
        except ValueError:
            printError()
            break
        
        # Processes the encryption or decryption
        if(command == "encrypt"):
            encrypt(sentence, shiftInt)
        elif (command == "decrypt"):
            encrypt(sentence, -shiftInt)
        
        # Checks if the user wants to end the program or run it again    
        askEnd = input("Do you want to continue? Y/N: ")
        if(askEnd == "n" or askEnd == "no"):
            end = True
        elif(askEnd != "y" and askEnd != "yes"):
            printError()
            end = True
        else:
            # Program continues, this print is just to add an empty line
            print()
=======
##########
# VARIABLES
##########

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

end = False

##########
# FUNCTIONS
##########

# Prints an error message 
def printError():
    print("Unexpected argument.")

# Encrypts or decrypts the TEXT using the SHIFT and prints the resulting list as a string
def encrypt(text, shift):
    encrypted = []
    
    # If there is a special symbol (non-letter), adds it directly to the encrypted sentence
    # If adding the shift will overflow the list, calculates the number of characters left to the end of it and adds it at the correct place
    # In case none of the above happens, simply shifts the letter and adds it to the encrypted sentence
    for i in text:
        if(not i in alphabet):
            encrypted.append(i)
        elif(alphabet.index(i) + shift > len(alphabet) - 1):
            missing = len(alphabet) - 1 - (alphabet.index(i))
            encrypted.append(alphabet[shift - missing - 1])
        else:
            encrypted.append(alphabet[alphabet.index(i) + shift])
     
    print("".join(encrypted))

##########
# MAIN
##########

while(not end):
    
    print("----- CAESAR CYPHER -----")
    command = input("Do you want to encrypt or decrypt? ")

    # Checks if the user inserted a viable command
    if (command != "encrypt" and command != "decrypt"):
        printError()
        end = True
    else:
        # Asks for user input: sentence and shift
        print(f"Insert the sentence you want to {command}:")
        sentence = input()
        shift = input("Insert the shift: ")
        
        # Checks if user inserted an integer for the shift, if not ends the program
        try:
            shiftInt = int(shift)
        except ValueError:
            printError()
            break
        
        # Processes the encryption or decryption
        if(command == "encrypt"):
            encrypt(sentence, shiftInt)
        elif (command == "decrypt"):
            encrypt(sentence, -shiftInt)
        
        # Checks if the user wants to end the program or run it again    
        askEnd = input("Do you want to continue? Y/N: ")
        if(askEnd == "n" or askEnd == "no"):
            end = True
        elif(askEnd != "y" and askEnd != "yes"):
            printError()
            end = True
        else:
            # Program continues, this print is just to add an empty line
            print()
>>>>>>> 404d2aba1d8756b0758e3f36ce0fc839045b0ecb
