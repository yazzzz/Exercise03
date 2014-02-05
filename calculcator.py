
#pseudo code for this exercise
   # repeat forever:
   #      read input
   #      tokenize input
   #      if the first token is 'q', quit
   #      otherwise decide which math function to call based on the tokens we read

import arithmetic

while True:
    user_input = raw_input(">> ")
    user_input_list = []
    user_input_list = user_input.split(" ")
    if user_input_list[1].isdigit() and user_input_list[2].isdigit():
        if user_input_list[0] == "+":
            print arithmetic.add(int(user_input_list[1]), int(user_input_list[2]))
    else:   
        print "That's not a valid integer!"


