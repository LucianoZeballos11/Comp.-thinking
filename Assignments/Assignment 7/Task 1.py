# Assignment 1
def chop(z): # define the function as chop
   z.pop(0), z.pop(-1) # eliminate the first and last element
   return None # return none

list_def = [1, 2, 3, 4] # define the list as variable
print(f"my list before call chop function => {list_def}") # program output before call the function
chop(list_def) # call the function
print(f"my list after call chop  function => {list_def  }\n") # program output after call the function


def middle(t): # define the function as middle
    return t[1:-1] # return new list without first and last element

fst_list = [1, 2, 3, 4] # define the list as variable
print(f"my list before call middle function => {fst_list}") # program output before call the function
new_list = middle(fst_list) # call the function
print(f"my list after call middle function => {fst_list}") # program output after call the function
print(f"new list after call middle function => {new_list}") # program output the function