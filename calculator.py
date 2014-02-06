import arithmetic

while True:
    user_input = raw_input(">> ")
    
    if user_input.lower() == "q":
        break

    user_input_list = []
    user_input_list = user_input.lstrip().split(" ")
    for i in user_input_list[1:]:
        if not i.isdigit():
            print "Found non valid integers, please try again!"
            break
        break

    # first check for proper number of arguments.
    if  len(user_input_list) < 2:
        print "incorrect number of arguments! please try again!"

    # if 2 arguments, we are running the funcs that only take 2 argumentss

    ### would like to get rid of .isdigit, but not working right now 5:50pm 2/5
    elif len(user_input_list) == 2:
        arg0 = user_input_list[0]
        arg1 = user_input_list[1]
        if arg0 == "square" and arg0.isdigit():
            print arithmetic.square(int(arg1))
        elif arg0 == "cube" and arg0.isdigit():
            print arithmetic.cube(int(arg1))


    # if 3 arguments, we are running the other functions
    elif len(user_input_list) == 3 and arg0 not in ["square", "cube"]:
        arg0 = user_input_list[0]
        arg1 = user_input_list[1]
        arg2 = user_input_list[2]
        
        if arg1.isdigit() and arg2.isdigit():
            if arg0 == "pow":
                print arithmetic.power(int(arg1), int(arg2))

    elif len(user_input_list) >= 3:
        if arg1.isdigit() and arg2.isdigit():
            if arg0 == "+":
                print arithmetic.add(int(arg1), int(arg2))
            if arg0 == "-":
                print arithmetic.subtract(int(arg1), int(arg2))
            if arg0 == "*":
                print arithmetic.multiply(int(arg1), int(arg2))
            if arg0 == "/":
                print arithmetic.divide(int(arg1), int(arg2))
            if arg0 == "mod":
                print arithmetic.mod(int(arg1), int(arg2))

        else:   
            print "That's not a valid integer!"




