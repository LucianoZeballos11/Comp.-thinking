# Assignment 3
input_str = input("Please enter string:\n> ") # user input
upper_count = 0 # define variable to store the amount of uppercases letters
lower_count = 0 # define variable to store the amount of lowercases letters
num_count = 0 # define variable to store the amount of numbers
special_count = 0 # define variable to store the amount of special characters and spaces
for letter in input_str: # define a variable that review each letter of the user input
    if letter.isupper(): 
        upper_count += 1 # increase the store of uppercase letters
    elif letter.islower(): 
        lower_count += 1 # increase the store of lowercase letters
    elif letter.isdigit():
        num_count += 1 # increase the store of number count
    else:
        special_count += 1 # increase the store of special characters
print(f"- Uppercase letters; {upper_count}") # program output the total amout of uppercase letters
print(f"- Lowercase letters: {lower_count}") # program output the total amout of lowerrcase letters
print(f"- Numbers: {num_count}") # program output the total amout of numbers
print(f"- Other characters: {special_count}") # program output the total amout of special characters