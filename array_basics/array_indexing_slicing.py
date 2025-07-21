import numpy as np

# indexing in one dimensional array
arr = np.array([1,2,3,4,5])
print(arr[0])
print(arr[1])
print(arr[-1])

# indexing in multi dimesional array
m_arr = np.array([[1,2,3],[4,5,6]])
print(m_arr[0][1])
print(m_arr[1][2])
print(m_arr[1][-1])

# slicing in array
arr2 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr2[0:7])
print(arr2[0:9:2])
