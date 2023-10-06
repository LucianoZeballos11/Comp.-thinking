# Assignment 2
computepay = lambda hrs, rt: (hrs * rt)  # function 1 defined & developed
computepay_extra = lambda hrs, rt: ((40 * rt) + (((hrs - 40) * 1.5) * rt))  # function 2 defined & developed
try:
    hours = int(input("Enter Hours: \n > "))  # user input
    if hours < 0:
        print("Error, please enter numeric input")
    else: 
        rate = float(input("Enter Rate: \n > "))  # user input
        if rate < 0:
            print("Error, please enter numeric input")
        else:
            salary = float(computepay(hours, rate))  # formula defined and call the function 1
            if hours <= 40:
                print(f"Pay: {salary}")  # program output result if hours is below to 40 hours
            else:
                salary = float(computepay_extra(hours, rate))  # formula for workers that worked more than 40 hours calling the function 2
                print(f"Pay: {salary}")  # program output if hours is grader than 40 hours
except:
    print("Error, please enter numeric input")  # program output if there is any data error on user input
