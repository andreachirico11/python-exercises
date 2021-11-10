import numpy as numpy
from scipy.optimize import fsolve
from scipy import integrate
from numpy import sin, pi


result = integrate.quad(sin, 0, pi)

print(result)


sol = fsolve(lambda x: x**2 + x, [0])
print(sol)
