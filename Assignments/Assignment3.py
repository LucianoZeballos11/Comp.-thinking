#Assignment 1
try: 
    hours = int(input("Enter Hours:\n > ")) #user's input
    rate = float(input("Enter Rate:\n > ")) #user's input
    salary = float(hours * rate) #formula for salary below 40 hours of work
    extra = hours - 40 #formula to know to amount of hours worked after 40 hours
    salary2 = float(((extra * 1.5) * rate )+ 40 * rate)#forumla for salary over 40 hours of work
except:
    print("Error, please enter numeric input") #program print in case of a type error
else:
    if hours > 40:
        print(f'Pay: {salary2}') #program print
    else:
        print(f'Pay: {salary}') #program print

#Assignment 2
try: 
    score = float(input("Enter Score:\n > ")) #user's input
    if 101 > score >= 90:
        print("Grade is A") #program print
    elif 90 > score >= 80:
        print("Grade is B") #program print
    elif 80 > score >= 70:
        print("Grade is C") #program print
    elif 70 > score >= 60:
        print("Grade is D") #program print
    elif 0 < score < 60:
        print("Grade is F") #program print
    else:
        print("Error, please enter numeric input between 0 and 100") #program print in case of a number lower to 0 or greather than 100
except:
    print("Error, please enter numeric input between 0 and 100") #program print in case of a type error

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
print(f'Sum of input numbers: {sum}') #program print
print(f'Number of input: {count}') #program print
print(f'Average of input: {average}') #program print