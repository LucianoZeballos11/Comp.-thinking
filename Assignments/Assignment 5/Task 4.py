# Assignment 4
while True: # infinite loop
    inp_str = input("Please enter string:\n> ") # user input
    if inp_str == "done": # user input to break the loop
        print("Bye !") # program output after user breaker input
        break # break infinite loop
    chr_removed = [',', '.', ':', '!', '?'] # define special characters to be removed of the user input
    for letter in chr_removed:
        inp_str = inp_str.replace(letter,'') # replace the special character with a blank space
    inp_str = inp_str.upper() # transform the string into uppercase letters
    print(inp_str) #program output with the new changes
