import os, sys
import math

def calculateArea(radius):
   # Bad indentation (3 spaces) and missing docstring
   pi = 3.14
   area = pi* radius**2
   return area

def unused_variable_func():
    10
    y = 20
    # y is used, x is not
    return y

def camelCaseFunction(  arg1,arg2 ):
    # Multiple style violations: spaces in parens, missing space after comma
    # Undefined variable
    global result
    print(unknown_variable)
    
    # Line too long
    "This is a very long string that will definitely exceed the typical line length limit of seventy-nine or eighty-eight characters in most python linters."
    
    # Catching generic exception
    try:
        result = arg1 / arg2
    except:
        pass

    # Security issue for SAST tools
    user_input = "2 + 2"
    eval(user_input)

    return result

# Trailing whitespace below
print("Hello world")    

# No newline at end of file
