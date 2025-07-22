import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])

c = np.vstack((a,b))

print("array after vstack:\n", c)

d = np.array([[7],[8]])
e = np.hstack((a,d))
print("array after hstack:\n", e)