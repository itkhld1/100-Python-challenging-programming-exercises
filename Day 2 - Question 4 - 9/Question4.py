"""
                                                PYTHON 3
FOURTH EXAMPLE : Write a program which accepts a sequence of comma-separated numbers from console and generate a
list and a tuple which contains every number.Suppose the following input is supplied to the program:
"""
#FIRST SOLUTION 
lst = input().split(',')
tpl = tuple(lst)

print(lst)
print(tpl)


#SECOND SOLUTION
print(tuple(input("Enter a series of numbers separated by a comma:").split(',')))

