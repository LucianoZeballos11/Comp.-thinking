# Assignment 1
while True: # infinite loop
    try: 
        input_word = input("Please enter two words:\n > ").strip() # user input and the program will erase all white spaces
        list_words = input_word.split() # transform the string into list
        if input_word == "done" or input_word == "": # user input to break the loop
            print("--bye!!") # program output after user breaker input
            break # break infinite loop
        if len(list_words) == 2:
            if list_words[0] < list_words[1]: 
                print(f"{list_words[0]} comes first") # program output if the first word is less important than the second word
            else:
                print(f"{list_words[1]} comes first") # program output if the second word is less important than the first word
        else: 
            continue # the program will still asking until the user introduce only 2 words
    except:
        input("Please enter two words:\n > ").strip() #program output in case of data error, ask for new user input erasing all white spaces
