# Minh Trinh
# 1001705984
# Python 3.8.10
# Linux

import os

def traverse(CWD):
    sum = 0
    for contents in os.listdir(CWD):
        # if the 'contents' of CWD is a file, store the byte size of that file into 'sum'
        if os.path.isfile(contents):
            sum += os.path.getsize(contents)

        # if the 'contents' of CWD is a directory, call the 'traverse' function to get the 
        # of the contents in that specified directory and add it to 'sum'
        if os.path.isdir(contents):
            sum += traverse(contents)
    
    return sum

totSpace = 0

# this stores the current working directory as a string into 'CWD'
CWD = os.getcwd()
print("This is the CWD: ", CWD)

#after calling the recursion, stores the total byte size into 'totSpace;
totSpace = traverse(CWD)

print('Byte Size: ', totSpace, '\n')

# Questions:
#  1) Was one language easier or faster to write the code for this? If so, describe in detail
#     why, as in what about the language made that case.
#         - It was much easier and faster to write the code in java and python because they had
#           various functions to easily find if something was a file or a directory and get the
#           the size of them. Whereas C, required the usage of dirent which required pointers to
#           be used to find the path of a file/folder and it's contents.
#  2) Even though a language may not (e.g. FORTRAN) support recursion, describe how you could write
#     a program to produce the same results without using recursion. Would that approach have any
#     limitations and if so, what would they be?
#         - You could store the contents of the CWD into arrays which will then go through each one
#           adding up the sizes of each file, and recreating more arrays as more subdirectories show.
