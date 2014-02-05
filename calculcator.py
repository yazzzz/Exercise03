
#pseudo code for this exercise
   # repeat forever:
   #      read input
   #      tokenize input
   #      if the first token is 'q', quit
   #      otherwise decide which math function to call based on the tokens we read

import arithmetic

while True:
    user_input = raw_input(">> ")
    #print user_input
    user_input_list = []
    user_input_list = user_input.split(" ")
    #print user_input_list


