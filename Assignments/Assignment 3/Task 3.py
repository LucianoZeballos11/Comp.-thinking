#Assignment 3
sum = 0 #Assign a variable to make the addition of all the numbers that the user input
count = 0 #Assign a variable to count the amount of valid inputs by the user 
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break #finsh the loop while true
        num = int(num) #declare that 'num' will be defined as a integrer in case of a type error
        sum += num 
        count += 1
    except ValueError:
        print("invalid input. enter a number") #program print in case of a type error
if count > 0: #declare this function becuase 0 is not a valid value
    average = sum / count
else:
    average = 0
print(f'Sum of input numbers: {sum}') #program output
print(f'Number of input: {count}') #program output
print(f'Average of input: {average}') #program output