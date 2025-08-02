import numpy as np

a = np.array([
    [1, 1, 1],
    [0.10, 0.15, 0.20],
    [0.10, 0, 0.20]
])
b = np.array([10000, 1600, 1000])
rezult = np.linalg.solve(a, b)
x, y, z = rezult

print(f'{x:.0f}')
print(f'{y:.0f}')
print(f'{z:.0f}')
