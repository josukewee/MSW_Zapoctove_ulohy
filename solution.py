import numpy as np
from scipy.optimize import fsolve

def equations(vars):
    x, y = vars
    a = np.array([101.1, 206.8, 304.3, 411.7, 508.4])
    b = np.array([0.5, 1.0, 1.5, 2.0, 2.5])
    c = np.dstack((a,b))
    rows, cols = c.shape()
    for a_i in range(rows):
        for b_i in range(cols):
            eq1 = np.sum(2 * (a_i - y * np.power(b_i, x)) * (-y * np.power(b_i, x) * np.log(b_i))) 
            eq2 = np.sum(2 * (a_i - y * np.power(b_i, x)) * (-np.power(b_i, x)) for a_i, b_i in zip(a, b))
    return [eq1, eq2]

initial_guess = [1, 1]
solution = fsolve(equations, initial_guess)
print(f'Solution: x = {solution[0]}, y = {solution[1]}')