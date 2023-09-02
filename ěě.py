import numpy as np
import time
import matplotlib.pyplot as plt


a = []
b = []
times_jacobi = []
times_prima_metoda = []
matrix_sizes = np.arange(4, 601, 4)


def jacobi(a, b, niteraci, x0=None):
    if x0 is None:
        x0 = np.ones((len(a), 1))
    start_time = time.time()
    x = x0
    D = np.diag(a)
    a_except_diagonal = a - np.diag(D)
    for i in range(niteraci):
        x = (b - np.matmul(a_except_diagonal, x)) / D
    end_time = time.time()
    times_jacobi.append(end_time - start_time)
    return x


def prima_metoda(a, b):
    start_time = time.time()

    x = np.linalg.solve(a, b)
    end_time = time.time()
    times_prima_metoda.append(end_time - start_time)
    return x

# Bohužel nevím, jak zahrnout 0 do maticy, proto se tomu vyhneme. Cílem úkolu je zjistit, která metoda je vhodnější pro malé a velké matice.
# Našel jsem metod nazývaný Rozklad jediných hodnot (SVD), ale zatím jsem se do ní nezabýval.


for size in matrix_sizes:
    upper_bound = 10
    lower_bound = -10
    positive_float = np.random.uniform(0.0001, upper_bound)
    negative_float = np.random.uniform(lower_bound, -0.0001)
    a1 = np.random.choice([positive_float, negative_float], size=(size, size))
    b1 = np.random.choice([positive_float, negative_float], size=(size, 1))
    b1 = b1.reshape(-1, 1)
    while np.linalg.det(a1) == 0:
        a1 = np.random.choice([positive_float, negative_float], size=(size, size))
    a.append(a1)
    b.append(b1)


for matrix, matrix1 in zip(a, b):
    a_array = np.array(matrix)
    b_array = np.array(matrix1)
    jacobi(a_array, b_array, 50)
    prima_metoda(a_array, b_array)

print(times_jacobi)
print("prima metoda vysledky:", times_prima_metoda)

plt.figure(figsize=(10, 6))
plt.plot(matrix_sizes, times_jacobi, label='Jacobi', marker='x')
plt.plot(matrix_sizes, times_prima_metoda, label='Prima metoda', marker='.')
plt.xlabel('Matrix Size')
plt.ylabel('Time Taken (s)')
plt.title('Execution Time vs. Matrix Size')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()