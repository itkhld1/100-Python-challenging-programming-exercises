"""
                                                PYTHON 3
EXAMPLE FIVE: Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""
class IOString():
    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())

a = IOString()
a.get_string()
a.print_string()
