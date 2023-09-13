#Assignment - 1
hours = float(input('Enter Hours: \n')) #user's input
rate = float(input('Enter Rate: \n')) #user's input
salary = hours * rate
print('Salary:',salary) #program print

#Assignment - 2
celsius = float(input('Enter Celsius temperature: \n')) #user's input
fahrenheit = celsius * 9 / 5 + 32
print('Fahrenheit temperture:', fahrenheit) #program print

#Assignment - 3
seconds = int(input('Enter seconds: \n')) #user's input
hours = seconds // 3600
minutes = (seconds % 3600) // 60
sec = seconds % 60
print(f'{seconds} seconds is {hours} hours, {minutes} minutes, {sec} seconds.') #program print
