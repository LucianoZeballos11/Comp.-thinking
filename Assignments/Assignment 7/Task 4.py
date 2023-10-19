# Assignment 4
list_num = [] # variable to store the elements of the main list
print("Typing 'done' will exit the program") # program output
while True: # infinite loop
    input_int = input("Please enter an integrer: ") # program output
    if input_int == "done": # user input to break the loop
        print("---------- Bye !! --------------") # program output after break the loop
        break # break infinite loop
    try:
        num = int(input_int) # define the user input as integrer
    except ValueError:
        continue # the program will continue runing asking for the user input until recieve a integrer
    list_num.append(num) # add the element inputed to the main list
    avr = sum(list_num) / len(list_num) # average formula using the main list elements
    print(f"{list_num}, average = {(round(avr, 2))}") # program output with maximum 2 decimals