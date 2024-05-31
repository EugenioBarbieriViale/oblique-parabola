import matplotlib.pyplot as plt
import numpy as np
from random import random, randint, choice

dim = 10

xf, yf = randint(3,7), randint(3,7)

# a = choice([i for i in range(-4,-3) if i != 0])
# b = choice([i for i in range(3,4) if i != 0])
# c = choice([i for i in range(-4,-3) if i != 0])

a = choice([i for i in range(2,5) if i != 0])
b = choice([i for i in range(-4,-3) if i != 0])
c = choice([i for i in range(2,5) if i != 0])

A = -(b**2)
B = -(a**2)
C = 2*a*c+2*a**2*xf+2*b**2*xf
D = 2*b*c+2*a**2*yf+2*b**2*yf
E = 2*a*b
F = -xf**2 * (a**2 + b**2) -yf**2 * (a**2 + b**2) + c**2

big_ys = []
low_ys = []
p_xs = range(600)
for x in p_xs:
    alpha = E*x
    beta = A*x**2 + C*x + F
    delta = (alpha + D)**2 - 4*B*beta

    big_y = (-alpha - D + np.sqrt(delta))/(2*B)
    low_y = (-alpha - D - np.sqrt(delta))/(2*B)

    big_ys.append(big_y)
    low_ys.append(low_y)

plt.plot(xf, yf, "bo")

xs = range(dim*2)
y = [(-a/b)*x + (-c/b) for x in xs]

plt.plot(xs, y, "g")
plt.plot(p_xs, big_ys, "y")
plt.plot(p_xs, low_ys, "r")

plt.xlim(0,dim)
plt.ylim(0,dim)

plt.show()
