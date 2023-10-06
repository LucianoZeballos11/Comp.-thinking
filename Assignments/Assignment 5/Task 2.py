# Assignment 2
input_str = input("Enter string: \n > ") # user input 
print(f"Input string = {input_str}") # program outputs user input
list_str = len(input_str) # get length of the string
reversed_str = list_str - 1 # formula to reverse the string from the first until the last letter based on the length
while 0 <= reversed_str:
    print(f"{input_str[reversed_str]}") # program output
    reversed_str -= 1 # reversed string letter per letter until the length is equal 0
