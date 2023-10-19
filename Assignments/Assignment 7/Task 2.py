# Assignment 2
only_words = [] # variable to store the elements of the main list
with open("romeo.txt","r") as file: # open romeo.txt file using "with" statement
    for line in file: # for loop
        words = line.split() # seperate the words into list
        for word in words: # for loop
            if not word in only_words: # function in case the word is not in the storage
                only_words.append(word) # function to add the words in the storage
print(sorted(only_words)) # program output with the words organized 