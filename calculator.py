# https://github.com/asjchat/lab11-AC-BA
# Partner 1: Ananda Chatterjee
# Partner 2: Brayden Allen

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
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if a <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a**b

def square_root(a):
    if a < 0:
        raise ValueError("Error")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b) # can have negative nums

def subtract():
    return

def logarithm():
    return
