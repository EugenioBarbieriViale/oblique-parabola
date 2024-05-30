import matplotlib.pyplot as plt
import numpy as np
from random import random, randint, choice

dim = 10

def parabola(xs, a, b, c, xf, yf):
    # The equation of a parabola with oblique axis:
    # 0 = A*x**2 + B*y**2 + C*x + D*x + E*x*y + F

    A = -(b**2)
    B = -(a**2)
    C = 2*a*c+2*a**2*xf+2*b**2*xf
    D = 2*b*c+2*a**2*yf+2*b**2*yf
    E = 2*a*b
    F = -xf**2 * (a**2 + b**2) -yf**2 * (a**2 + b**2) + c**2

    big_ys = []
    low_ys = []
    for x in xs:
        alpha = E*x
        beta = A*x**2 + C*x + F
        delta = (alpha + D)**2 - 4*B*beta

        big_y = (-alpha - D + np.sqrt(delta))/(2*B)
        low_y = (-alpha - D - np.sqrt(delta))/(2*B)

        big_ys.append(big_y)
        low_ys.append(low_y)
    return big_ys, low_ys

for i in range(120):
    x,y = random()*dim, random()*dim
    plt.plot(x,y, "ro")

# Well
xf, yf = randint(3,7), randint(3,7)
plt.plot(xf, yf, "bo")

# River
# a = choice([i for i in range(-4,-3) if i != 0])
# b = choice([i for i in range(3,4) if i != 0])
# c = choice([i for i in range(-4,-3) if i != 0])

# a = choice([i for i in range(-3,-2) if i != 0])
# b = choice([i for i in range(-4,-3) if i != 0])
# c = choice([i for i in range(6,9) if i != 0])

a = choice([i for i in range(0,10) if i != 0])
b = choice([i for i in range(0,2) if i != 0])
c = choice([i for i in range(-10,0) if i != 0])


xs = range(dim*2)
y = [(-a/b)*x + (-c/b) for x in xs]

plt.plot(xs, y, "g")

# Parabola
p_xs = range(600)
big_ys = parabola(p_xs, a, b, c, xf, yf)[0]
low_ys = parabola(p_xs, a, b, c, xf, yf)[1]
plt.plot(p_xs, big_ys, "y")
plt.plot(p_xs, low_ys, "y")

plt.xlim(0,dim)
plt.ylim(0,dim)

plt.show()
