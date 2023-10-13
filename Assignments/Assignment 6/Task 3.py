# Assignment 3
file_name = input("Enter a file name: ") # user input
total_sum = 0 # variable to add the seeked numbers 
count_nums = 0 # variable to count the line with the seeked number 
try:
    with open(file_name, "r") as file: # "with" statement 
        for line in file: 
            if line.startswith("X-DSPAM-Confidence"): # the program will seek a specific word
                line.rstrip() # the program will erase all the blank spaces around the line
                line = line.split(":")[1].strip() # the program will read the splitted line in the specfic symbol and erase all the blank spaces
                real_number = float(line) # we define the line as a float knowing that it will only conformed by numbers 
                count_nums += 1 # variable will increase the count of numbers per line until the end
                total_sum += real_number # variable will add the seeked numbers until the end
    if count_nums == 0:
        print("Average spam confidence: 0") # program ouput if the file do not contain the seeked word with numbers or if the value of the number is 0
    else: 
        sum_average = total_sum / count_nums
        print(f"Average spam confidence: {sum_average}") # program output
except:
    print(f"File cannot be opened: {file_name}") # program output if the file don't exist