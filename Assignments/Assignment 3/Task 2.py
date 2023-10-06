#Assignment 2
try: 
    score = float(input("Enter Score:\n > ")) #user's input
    if 101 > score >= 90:
        print("Grade is A") #program output
    elif 90 > score >= 80:
        print("Grade is B") #program output
    elif 80 > score >= 70:
        print("Grade is C") #program output
    elif 70 > score >= 60:
        print("Grade is D") #program output
    elif 0 < score < 60:
        print("Grade is F") #program output
    else:
        print("Error, please enter numeric input between 0 and 100") #program print in case of a number lower to 0 or greather than 100
except:
    print("Error, please enter numeric input between 0 and 100") #program output in case of data error