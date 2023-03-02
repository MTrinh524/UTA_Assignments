# Minh Trinh
# 1001705984
# 11/30/2022
# Ubuntu 20.04.3 LTS, Python 3.8.10

import os

# traverses the Java Program input to be updated to the specified annotation
def ProgTraverse(Line):
    count = 0 # stores the line number to be modified
    annote = 0
    comment = ""

    for indLine in Line:
        Tokens = indLine.split() # stores each element delimited by spaces
        Line[count] = str(annote) + " " + indLine # rewrites that specific line to the annoated version 
        for Elem in Tokens: # traverses the tokens in the specific line
            if Elem in ["//", "/*", "*/", "\""]: # stores the Elem into comment if it is either "//" or "/*"
                comment = Elem
            elif Elem == "{": # checks to see if your token is a "{"
                if comment not in ["//", "/*"]: # makes sure it's not part of a comment
                    annote+=1 # increments the annotation
                    Line[count] = str(annote) + " " + indLine # rewrites that specific line to the annotated version
            elif Elem == "}": # checks to see if your token is a "}"
                if comment not in ["//", "/*"]: # makes sure it's not part of a comment
                    Line[count] = str(annote) + " " + indLine # rewrites that specific line to the annotated version
                    annote-=1 # decrements AFTER the line modification

        count+=1 #increments count so that the next line can be modified when needed
        if comment != "/*":
            comment = ""


    return Line

# Main
javaInp = open("input.txt", "r") # opens up that txt file to be read
Line = javaInp.readlines() # reads each line in the file and stored into separate elements of the list


# iterates through the each element of the "Line" list to run the "ProgTraverse" method
ProgTraverse(Line)
for iter in Line:
    Tokens = iter.split() # splits it "iter" into tokens to check for error later
    print(iter, end="")
    if iter == Line[len(Line)-1]: # if iter is the last Line
        if Tokens[0] not in ["0"]: # if the first element isn't 0, sends an error as their are mismatching curly braces
            print()
            print("ERROR: Mismatching \"{\" or \"}\"", end="") 
print()

javaInp.close()