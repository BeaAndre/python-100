<<<<<<< HEAD
import random

matrix = [['A' + str(i) for i in range(1,6)],
          ['B' + str(i) for i in range(1,6)],
          ['C' + str(i) for i in range(1,6)]]

##########
# FUNCTIONS
##########

# Returns the end position of the given array/list
def end_of(array):
    return len(array) - 1

# Puts the whole matrix into an organized string ready to be printed
def map_print():
    map_print = ""
    for i in matrix:
        for j in i:
            map_print += str(j) + " "
            if(i.index(j) == end_of(i)):
                map_print += "\n"
    return map_print

# Checks if the given string appears on the matrix, ignoring case
def put_inMatrix(pos):
    for i in matrix:
        for j in i:
            if (pos.lower() == str(j).lower()):
                matrix[matrix.index(i)][i.index(j)] = "##"
                return
    raise Exception("Not a valid position.")

##########
# MAIN
#########

print("This is the map:")
print(map_print())

start = input("Where you do want to start? ")
try:
    put_inMatrix(start)
except Exception as error:
    print(error)
    
print(map_print())
=======
import random

matrix = [['A' + str(i) for i in range(1,6)],
          ['B' + str(i) for i in range(1,6)],
          ['C' + str(i) for i in range(1,6)]]

##########
# FUNCTIONS
##########

# Returns the end position of the given array/list
def end_of(array):
    return len(array) - 1

# Puts the whole matrix into an organized string ready to be printed
def map_print():
    map_print = ""
    for i in matrix:
        for j in i:
            map_print += str(j) + " "
            if(i.index(j) == end_of(i)):
                map_print += "\n"
    return map_print

# Checks if the given string appears on the matrix, ignoring case
def put_inMatrix(pos):
    for i in matrix:
        for j in i:
            if (pos.lower() == str(j).lower()):
                matrix[matrix.index(i)][i.index(j)] = "##"
                return
    raise Exception("Not a valid position.")

##########
# MAIN
#########

print("This is the map:")
print(map_print())

start = input("Where you do want to start? ")
try:
    put_inMatrix(start)
except Exception as error:
    print(error)
    
print(map_print())
>>>>>>> 404d2aba1d8756b0758e3f36ce0fc839045b0ecb
