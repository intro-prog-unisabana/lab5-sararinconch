def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num2 - num1

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        return num1/num2
    
def exponent(num1, num2):
    return num1**num2

def modulo(num1, num2):
    if num2 == 0:
        return "Error: Modulo by zero is not allowed."
    else:
        return num1 % num2

import math

def floor_divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    else: 
        return math.floor(num1/num2)
    
def absolute(num):
    return abs(num)