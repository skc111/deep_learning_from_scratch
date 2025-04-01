import numpy as np

def f(x):
    return x ** 2

def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)

x = 2
print(numerical_diff(f, x))