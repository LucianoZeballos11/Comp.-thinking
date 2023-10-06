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
        if num <= 0:
            print("Please enter a positive number")  # program output if the user's input is a number below 0
        else:
            result = num_divide3(num)  # call the function
            print(f"Number divisible by 3 among numbers from 1 to {num}: {result}")  # program output result
    except:
        print("Please enter a positive number")  # program output if there is any data error on the user's input