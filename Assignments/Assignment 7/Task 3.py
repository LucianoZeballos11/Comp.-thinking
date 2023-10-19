# Assignment 3
count = 0 # variable to store the amount of emails
with open("mbox.txt", "r") as file: # open mbox.txt file using "with" statement
    for line in file: # for loop
        if line.startswith("From:"): # the program will seek the specefic word
            continue # will continue the program
        elif line.startswith("From"): # the program will seek the specefic word
            new_line = line.split(" ")[1] # the program will read the splitted line from the specific position defined
            print(new_line) # program output
            count += 1 # variable will increase the count of its search until the end
    print(f"Total {count} lines were printed") # program output the amount of the seeked word
