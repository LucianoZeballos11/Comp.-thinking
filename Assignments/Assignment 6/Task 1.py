# Assignment 1
file_name = input("Enter a file name: ") # user input 
try:
    file_opened = open(file_name, "r") # define a variable that use the open file on read mode
except :
    print("Error, the file doesn't exist.") # program output if the file don't exist
else: 
    for letter in file_opened: # for loop
        print(letter.upper(), end="") # change all the letters of the file into uppercase letters until the there is no letters
file_opened.close() # function to close the open file