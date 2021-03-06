
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

    if len(user_input_list) > 3 or len(user_input_list) < 2:
        print "incorrect number of arguments! please try again!"
    elif len(user_input_list) == 2:
        arg1 = user_input_list[1]
        if user_input_list[0] == "square" and arg1.isdigit():
            print arithmetic.square(int(arg1))
        elif user_input_list[0] == "cube" and arg1.isdigit():
            print arithmetic.cube(int(arg1))
        else:
            print "That's not a valid integer!"


    elif len(user_input_list) == 3:
        arg1 = user_input_list[1]
        arg2 = user_input_list[2]

        if arg1.isdigit() and arg2.isdigit():
            if user_input_list[0] == "+":
                print arithmetic.add(int(arg1), int(arg2))
            if user_input_list[0] == "-":
                print arithmetic.subtract(int(arg1), int(arg2))
            if user_input_list[0] == "*":
                print arithmetic.multiply(int(arg1), int(arg2))
            if user_input_list[0] == "/":
                print arithmetic.divide(int(arg1), int(arg2))
            if user_input_list[0] == "pow":
                print arithmetic.power(int(arg1), int(arg2))
            if user_input_list[0] == "mod":
                print arithmetic.mod(int(arg1), int(arg2))

        else:   
            print "That's not a valid integer!"


