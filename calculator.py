"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError("division by zero")
    return b / a
def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("math domain error")
    return math.log(b, a)
def exp(a, b):
    return a ** b
