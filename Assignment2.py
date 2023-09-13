#Assignment - 1
hours = float(input('type the hours you work: \n'))
rate = float(input('type the rate you recieve: \n'))
salary = hours * rate
print('The total of salary is:',salary)

#Assignment - 2
celsius = float(input('Enter the a temperature in Celsius: \n'))
fahrenheit = celsius * 9 / 5 + 32
print('The value of the temperture typed in Celsius is Fahrenheit is:', fahrenheit)

#Assignment - 3
seconds = int(input('type an amount of seconds: \n'))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
sec = seconds % 60
print(f'The value of seconds in hours, minutes and seconds are: {hours} hrs, {minutes} min, {sec} secs.')