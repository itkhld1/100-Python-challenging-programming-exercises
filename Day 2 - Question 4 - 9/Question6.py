"""
                                                PYTHON 3
EXAMPLE SIX: Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 _ C _ D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.
For example Let us assume the following comma separated input sequence is given to the program:
"""
#FIRST SOLUTION 
from math import sqrt   # import specific functions. Using * will import all

C,H = 50, 30

def calc(D):
    return sqrt((2*C*D)/H)

D = [int(i)for i in input().split(',')] # splits in comma position and set up in list
D = [int(i)for i in D]   # converts strings to integer
D = [calc(i)for i in D]   # returns floating value by calc method for every item in D
D = [round(i)for i in D]   # All the floating values are rounded
D = [str(i)for i in D]  # All the integers are converted to string to be able to apply join operation


#SECOND SOLUTION
from math import sqrt

C,H = 50, 30

def calc(D):
    return sqrt((2*C*D)/H)

D = input().split(',')
D = [str(round(calc(int(i)))) for i in D]
print(",".join(D))


#THIRD SOLUTION 
from math import * # importing all math functions
C,H = 50,30

def calc(D):
    D = int(D)
    return str(int(sqrt((2*C*D)/H)))

D = input().split(',')
D = list(map(calc,D))   # applying calc function on D and storing as a list
print(",".join(D))
