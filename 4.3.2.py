import numpy as np
import matplotlib.pylab as plt

def function_1(x):
    return 0.01*x**2 + 0.1*x

def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)

def draw_tangent(f, x0, y0):
    k = numerical_diff(f, x0)
    x = np.arange(0.0, 20.0, 0.1)
    y = k * (x - x0) + y0
    return y

x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
y1 = draw_tangent(function_1, 5, function_1(5))
plt.plot(x, y1)
plt.show()
