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
