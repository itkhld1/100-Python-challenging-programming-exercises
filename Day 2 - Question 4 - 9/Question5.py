"""
                                                PYTHON 3
FIFTH EXAMPLE : Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""
class IOString():
    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())

x = IOString()
x.get_string()
x.print_string()