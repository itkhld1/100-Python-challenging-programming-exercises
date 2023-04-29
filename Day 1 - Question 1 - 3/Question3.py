"""
                                                PYTHON 3
EXAMPLE THREE: With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an
integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8
"""
#FIRST SOLUTION
n = int(input())
ans = {}
for i in range(1, 1+n):
    ans[i]= i * i
print(ans)


#SECOND SOLUTION
n = int(input())
ans = {i: i*i for i in range(1, 1+n)}
print(ans)


#THIRD SOLUTION
num = int(input())
print(dict(enumerate([i * i for i in range(1, num+1)], 1)))
