"""
Data science training module.
"""
import numpy as np

arr = np.array(
    [[[1, 2, 3], 
      [4, 5, 6]], 
     [[7, 8, 9], 
      [10, 11, 12]]])

print(arr[1,1,2])  # Output: 6

print(arr[-1,-1,-1])

# 1-d array with 8 elements
arr1d = np.array([0, 1, 2, 3, 4, 5, 6, 7])
arr1d = arr1d.reshape(2,2,2)
arr1d = arr1d.reshape(-1)  # Reshape to 1-d array
print(arr1d)

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr2 = np.array([13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
arr3 = np.array([25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])

combined = np.concatenate((arr1, arr2, arr3))

evenvalues = arr1[arr1 % 2 == 0]
print(evenvalues)

find2 = np.where(arr1 % 2 == 0)
print(find2)

print(combined)

arr12d = arr1.reshape(2,6)
arr22d = arr2.reshape(2,6)
arr32d = arr3.reshape(2,6)

combined2d = np.concatenate((arr12d, arr22d, arr32d))
print(combined2d)
print("-"*20)
arr42d = np.array([[1, 2, 3], [4, 5, 6]])
arr52d = np.array([[7, 8, 9], [10, 11, 12]])
arr62d = np.array([[13, 14, 15], [16, 17, 18]])

matrix = np.stack((arr42d, arr52d, arr62d), axis=2)
print(matrix)
print("-"*20)
split_arrays = np.vsplit(matrix, 2)
print(split_arrays)

# use arange to create sequences of numbers for a 2-d array
seq_array = np.arange(0, 8).reshape(1,2,2,2,1)
