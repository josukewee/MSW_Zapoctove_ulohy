## Násobení matic

import math, random
import numpy as np

## Pure python doesn't have class Matrix, so i will define it with "nasobeni matic" as a method.

class Matrix:
    def __init__(self, r, c):
        self.matrix = self.vytvori_matice(r, c)


    ## r stands for row, c for column. I'll use random.randit() to fill the matrix.

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


m=Matrix(4,3)
m1=Matrix(3,4)
print(m.matrix)



arr1 = np.array(m.matrix)
arr2 = np.array(m1.matrix)
print(np.multiply(arr1, arr2))


