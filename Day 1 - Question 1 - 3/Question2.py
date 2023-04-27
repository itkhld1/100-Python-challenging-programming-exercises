"""
                                                PYTHON 3
SECOND EXAMPLE : Write a program which can compute the factorial of a given numbers.The results should be printed in a
comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320
"""
#FIRST SOLUTION 
n = int(input)

fact = 1
i = 1
while i <= n:
    fact *= i  #fact = fact * i 
print(fact)


#SECOND SOLUTION
n = int(input)
def shortFact(x):
    return 1 if x <= 1 else x * shortFact(x-1)
print(shortFact(n))


#THIRD SOLUTION 
while True:
    try:
        num = int(input("Enter a number: "))
        break:
    except ValueError as err:
        print(err)

org = num
fact = 1
while num:
    fact = num * fact
    num = num - 1
print(f"The factorial of {org} is {fact}")

