
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
    arg1 = user_input_list[1]
    arg2 = user_input_list[2]

    if len(user_input_list) > 3:
        print "too many numbers!"
    else:
        if arg1.isdigit() and arg2.isdigit():
            if user_input_list[0] == "+":
                print arithmetic.add(int(arg1), int(arg2))
            if user_input_list[0] == "-":
                print arithmetic.subtract(int(arg1), int(arg2))
            if user_input_list[0] == "*":
                print arithmetic.multiply(int(arg1), int(arg2))
            if user_input_list[0] == "/":
                print arithmetic.divide(int(arg1), int(arg2))
            if user_input_list[0] == "square":
                print arithmetic.square(int(arg1))
            if user_input_list[0] == "cube":
                print arithmetic.cube(int(arg1))
            if user_input_list[0] == "pow":
                print arithmetic.power(int(arg1), int(arg2))
            if user_input_list[0] == "mod":
                print arithmetic.mod(int(arg1), int(arg2))
        else:   
            print "That's not a valid integer!"


