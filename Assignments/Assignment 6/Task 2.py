# Assignment 2
count = 0 # variable to count the line with the seeked word
with open("mbox.txt", "r") as file: # open mbox.txt file using "with" statement
    for line in file: # for loop
        if line.startswith("From:"): # the program will seek a specific word
            line = line.rstrip() # the program will erase all the blank spaces around the line
            line = line.split("@")[1] # the program will read the splitted line from the specific symbol defined
            print(line) # program output
            count += 1 # variable will increase the count of lines of the seeked until the end
    print("Total %d hosts printed" %count) # program output the amount of the seeked word