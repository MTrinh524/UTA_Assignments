# Minh Trinh
# 1001705984
# 11/7/2022
# Ubuntu 20.04.3 LTS

import os

# calculates the answer for RPN expressions
def Calculate(Line):
    answer = 0
    stack = [] #initializes the stack
    RPNExpress = Line.split() # stores each element delimited by spaces
    operators = ["+", "-", "*", "/", "%"] #includes the % operator now

    for symbs in RPNExpress:

        if symbs not in operators: # if it is not one of our specified operators
            stack.append(int(symbs)) # then push the integer form into the stack
        if symbs in operators: # if it is one of our specified operators
            second = stack.pop() # save the value that was last pushed
            first = stack.pop() # save the value that was pushed second to latest

            # compares each of our symbols to "symbs" and do that operation for "first" and "second"
            if symbs == "+":
                stack.append(first + second)
            elif symbs == "-":
                stack.append(first - second)
            elif symbs == "*":
                stack.append(first * second)
            elif symbs == "/":
                stack.append(first / second)
            #EXTRA CREDIT: I added the Modulo Division operator into the calculator
            elif symbs == "%":
                stack.append(first % second)
    
    # pops the last value in our stack (which should be the answer) and return it back
    return float(stack.pop())

# Main
f = open("input_RPN_EC.txt", 'r') # opens up that txt file to be read
Line = f.readlines() # reads each line in the file and stored into separate elements of the list
length = len(Line) # gets the size of the "Line" list to be iterated later
count = 0 # stores the iteration currently on

#iterates through the each element of the "Line" list to run the "Calculate" method
while length > 0: 
    print(Calculate(Line[count]))
    count+=1
    length-=1
