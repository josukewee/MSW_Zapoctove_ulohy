import timeit
import time

## Násobení matic

import math, random
import numpy as np

# Pure python doesn't have class Matrix, so i will define it with "nasobeni matic" as a method.

class Matrix:

    # Dunder methods. __len__ method is used to define len of matrix, __getitem__ method makes possible to itarate through matrices' values.
    def __init__(self, r, c):
        self.matrix = self.vytvori_matice(r, c)

    def __str__(self):
        return self.matrix(self.matrix)

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    ## R stands for row, c for column. I'll use random.randit() to fill the matrix.

    def vytvori_matice(self, r, c):
        matrix = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(random.randint(-10, 10))
            matrix.append(row)
        return matrix


    def nasobeni_matic(self, matrix):
        result = [[0 for j in range(len(matrix[i]))] for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(matrix[0])):
                for k in range(len(matrix)):
                    result[i][j] += self.matrix[i][k] * matrix[k][j]
        return result


m=Matrix(4,4)
m1=Matrix(4,4)
print(m.matrix, "   ", m1.matrix, )
print(m.nasobeni_matic(m1), timeit.timeit(stmt=''))

## Matrices multiplication powered by numpy with the same matrieces.

arr1 = np.array(m.matrix)
arr2 = np.array(m1.matrix)
mul = np.matmul(arr1, arr2)
print("Matrix1 shape:",arr1.shape,"Matrix2 shape: ", arr2.shape,"Matrix3 shape: ", mul.shape, timeit.timeit(stmt='mul'))

print(mul)


## Intagrate a function.


def function(x):
    return x ** 0.5

a=0
b=1
n=1000

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n  # Width of each interval
    integral = (f(a) + f(b)) / 2  # Sum of the first and last terms
    for i in range(1, n):
        x = a + i * h
        integral += f(x)
    integral *= h
    return integral

print(trapezoidal_rule(function, a, b, n))

def integral_numpy()

######

#Porovnání času, potřebného k nalezení uspokojivého řešení soustav lineárních rovnic
# pomoci iterační a přímé metody.

def jacobi(a, b, niteraci, x0=np.ones(len(a))):
    x = x0
    D = np.diag(a)
    L = np.tril(a, k = -1)
    U = np.triu(a, k = 1)
    for i in range(niteraci):
        x=(b - np.matmul((L + U), x))/D
        print("iterace", i, "x=", x)
    return x

def prima_metoda(a, b):
    x = np.linalg.solve(a, b)
    print(x)

def solve_time(A, b, x0, method):
    start_time = time.time()
    method(A, b, x0)
    end_time = time.time()
    return end_time - start_time

matrix_sizes = np.arange(10, 201, 10)
matrices = []

for size in matrix_sizes:
    a = np.random.randint(0, 11, size=(size, size))
    b = np.random.randint(0, 11, size=(size, 1))
    matrices.append(a)