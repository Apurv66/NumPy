import numpy as np

a = np.array([7,5,3,4,8,9,2,1])
print("sorted array:\n", np.sort(a))

b = np.array([[9,2,7],[3,4,1],[8,6,5]])
print("sorted array:\n", np.sort(b, axis=1))

c = np.array([[9,2,7],[3,4,1],[8,6,5]])
print("sorted array:\n", np.sort(c, axis=0))