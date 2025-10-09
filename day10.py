from os import system

####################
# VARIABLES

end = False
reuseNumber = False

####################
# FUNCTIONS

def add(first, second):
    """Takes two numbers. Returns their sum."""
    return first + second

def sub(first, second):
    """Takes two numbers. Returns their subtraction."""
    return first - second

def mult(first, second):
    """Takes two numbers. Returns their multiplication."""
    return first * second

def div(first, second):
    """Takes two numbers. Returns their division."""
    return first / second

def operation(first, op, second, result):
    """Takes two numbers, an operator and the respective result. Returns a string with the entire operation."""
    return f"{first} {op} {second} = {result}"

def errorCode():
    """Returns an error code to use anytime the user inputs an argument which is not expected.."""
    return "Unexpected argument. Exiting..."

####################
# MAIN

while(not end):

    if(not reuseNumber):
        first = input("First number: " )
    else:
        print(f"Your first number is: {result}")
        first = result
    
    print("+ - * /")
    op = input("Pick an operation: ")
    
    second = input("Second number: ")
    
    # Check if what the user inserted are numbers, return an error if not
    try:
        int(first)
        int(second)
    except ValueError:
        end = True
        print(errorCode())
        break
        
    # Convert the inserted numbers to integers
    num1 = int(first)
    num2 = int(second)
    
    # Perform the calculation or return an error if the user didn't insert a valid operation 
    if(op == "+"):
        result = add(num1, num2)
    elif(op == "-"):
        result = sub(num1, num2)
    elif(op == "*"):
        result = mult(num1, num2)
    elif(op == "/"):
        result = div(num1, num2)
    else:
        end = True
        print(errorCode())
        break
    
    # Print the entire operation to the screen
    print(operation(num1, op, num2, result))
    
    print(f"Press Y to continue with your last value: {result}.")
    print("Press N to continue with a new value.")
    print("Press Q to quit.")
    
    choice = input().upper()
    
    if(choice == "Q"):
        print("Exiting...")
        break
    elif(choice == "Y"):
        reuseNumber = True
        system("cls")
    elif(choice == "N"):
        reuseNumber = False
        system("cls")
    else:
        end = True
        print(errorCode())
        break