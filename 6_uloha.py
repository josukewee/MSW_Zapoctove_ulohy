import numpy as np
import pyautogui
import random

data_list = []

def collect_mouse_information():
    while len(data_list) < 1000:
        x, y = pyautogui.position()
        data_list.append((x, y))

def create_seed(data):
    seed = 0
    for x, y in data:
        seed ^= x  # XOR operation accumulates randomness
        seed ^= y
    return seed


collect_mouse_information()

random_seed = create_seed(data_list)
print(random_seed)

random.seed(random_seed)

m = random.randint(1, 100)
n = random.randint(1, 100)

print(m, n)