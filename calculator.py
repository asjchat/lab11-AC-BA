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

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError
    if b <= 0:
        raise ValueError
    math.log(b, a)

def exp(a, b):
    return a**b


def square_root(a):
    if a < 0:
        raise ValueError("Error")
    math.sqrt(a)

def hypotenuse(a, b):
    math.hypot(a, b) # can have negative nums



