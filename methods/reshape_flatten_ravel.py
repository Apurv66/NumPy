import numpy as np

arr = np.arange(12)
print("array: ", arr)

reshaped = arr.reshape((3,4))
print("reshape array:\n", reshaped)

flattened = reshaped.flatten()
print("flattened array:\n", flattened)

raveled = reshaped.ravel()
print("raveled array:\n", raveled)