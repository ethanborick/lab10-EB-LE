"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
#calc
import math
# First example
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
def exponent(a, b):
    return a ** b


