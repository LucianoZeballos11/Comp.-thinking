# Assignment 1
try: 
    hours = int(input("Enter Hours:\n > ")) #user's input
    rate = float(input("Enter Rate:\n > ")) #user's input
    salary = float(hours * rate) #formula for salary below 40 hours of work
    extra = hours - 40 #formula to know to amount of hours worked after 40 hours
    salary2 = float(((extra * 1.5) * rate )+ 40 * rate)#forumla for salary over 40 hours of work
except:
    print("Error, please enter numeric input") #program output in case of a data error
else:
    if hours > 40:
        print(f'Pay: {salary2}') #program output
    else:
        print(f'Pay: {salary}') #program output