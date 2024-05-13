import numpy as np
import matplotlib.pyplot as plt
import timeit

polynomial_func = lambda x: 4*x**3 -  x**2 + 3*x - 2
exponential_func = lambda x: 7*x**2 + np.exp(3*x) - 3
logarithmic_func = lambda x: np.log(x + 1)

##  metoda puleni intervalu
def metoda_puleni(f, a, b, max_error):

    
    if f(a)*f(b) >= 0:
        raise ValueError("It won't work since the root is not included in the interval")

    start_time = timeit.default_timer()
    c = a
    while abs(b-a) > max_error:
        c = (a + b) / 2

        if (f(c) == 0.0):
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    end_time = timeit.default_timer()
    return c, end_time - start_time

def newton_raphson(f, x, error, max_steps):
    start_time = timeit.default_timer()
    def df(x):
        h = 0.001
        return (f(x+h)-f(x-h))/(2*h)

    for i in range(max_steps):
        xnew = x - f(x)/df(x)
        if abs(xnew-x) < error:
            break
        x=xnew
    end_time = timeit.default_timer()
    return xnew, end_time - start_time

def plot(f, a, b, title, method):
    if method=="Metoda puleni":
        print("Metoda puleni")
        x = metoda_puleni(f, a, b, 0.0001)[0]
        time = str(metoda_puleni(f, a, b, 0.0001)[1]) + " sec"
    else:
        print("Newton-Raphson")
        x = newton_raphson(f, 0, 0.0001, 100)[0]
        time = newton_raphson(f, 0, 0.0001, 100)[1]
    print("root: ", x)
    print(f"Time taken: {time}")
    plt.title(title)
    plt.plot(x, f(x), "bo")
    plt.plot(np.linspace(a, b, 100), f(np.linspace(a, b, 100)), "b") 
    plt.show()


root = metoda_puleni(exponential_func, 0, 1, 0.001)
newton_raphson(exponential_func, 1, 0.0001, 100)
root = metoda_puleni(polynomial_func, -1, 1, 0.001)
newton_raphson(polynomial_func, 1, 0.0001, 100)
root = metoda_puleni(logarithmic_func, -0.9, 1, 0.001)
newton_raphson(logarithmic_func, 0, 0.0001, 100)


##plot(exponential_func, 0, 1, "*Funkce: x**2 + e^(3*x) - 3", "Metoda puleni")
#plot(exponential_func, 0, 1, "*Funkce: x**2 + e^(3*x) - 3", "Newton-Raphson")

plot(polynomial_func, -1, 1, "*Funkce: 4 * x**3 -  x**2 + 3 * x - 2", "Metoda puleni")


