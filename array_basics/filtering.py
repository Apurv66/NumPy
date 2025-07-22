import numpy as np

num = np.array([1,2,3,4,5,6,7,8,9,10])
even_num = num[num % 2 == 0]
print("even numbers: ", even_num)