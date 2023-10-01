# Assignment 1
def N_list(note):  # function defined & developed
    if 90 <= note < 101:
        return 'A'
    elif 80 <= note < 90:
        return 'B'
    elif 70 <= note < 80:
        return 'C'
    elif 60 <= note < 70:
        return 'D'
    elif 0 < note < 60:
        return 'F'
try:
    score = float(input("Enter score: \n > "))  # user's input
    if score < 0: 
        print("Error, please enter a numeric input between 0 and 100")
    elif 100 < score: 
        print("Error, please enter a numeric input between 0 and 100")
    else:
        grade = N_list(score)  # call the function
        print(f"Grade is: {grade}")  # program output result
except:
    print("Error, please enter a numeric input between 0 and 100")  # program output if there is any data error on the user's input

    # Assignment 2
computepay = lambda hrs, rt: (hrs * rt)  # function defined & developed
try:
    hours = int(input("Enter Hours: \n > "))  # user's input
    if hours < 0:
        print("Error, please enter numeric input")
    else: 
        rate = float(input("Enter Rate: \n > "))  # user's input
        if rate < 0:
            print("Error, please enter numeric input")
        else:
            salary = float(computepay(hours, rate))  # formula defined and call the function
            if hours <= 40:
                print(f"Pay: {salary}")  # program output result if hours is below to 40 hours
            else:
                salary = float((40 * rate) + (((hours - 40) * 1.5) * rate))  # formula for workers that worked more than 40 hours calling the function
                print(f"Pay: {salary}")  # program output if hours is grader than 40 hours
except:
    print("Error, please enter numeric input")  # program output if there is any data error on the user's input

    # Assignment 3
def num_divide3(num):  # function defined & developed
    count = 0
    for z in range(1, num + 1):
        if z % 3 == 0:
            count += 1
    return count
while True:  # infine loop
    try:
        InpNum = input("Enter a positive integrer: \n > ")  # user's input
        if InpNum == "done":  # user's input to break the loop
            print("bye!!")  # program output after user's input is for breaking the infinite loop
            break  # break the infinite loop
        num = int(InpNum)  # define the input as an integer
        if num < 0:
            print("Please enter a positive number")  # program output if the user's input is a number below 0
        else:
            result = num_divide3(num)  # call the function
            print(f"Number divisible by 3 among numbers from 1 to {num}: {result}")  # program output result
    except:
        print("Please enter a positive number")  # program output if there is any data error on the user's input