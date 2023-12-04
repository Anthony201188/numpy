import numpy as np

one_nine = range(1,10)
array_1d = np.array([one_nine])

#print(array_1d)
#print(array_1d.dtype)

array_rand = np.random.rand(3,4) #random.rand creates random floats between 0-1
#print(array_rand)

num_shape_elems = ( 2* 3 * 2) #232 are the length of the odd number arrays required
print(num_shape_elems)

numbers_odd = np.arange(1, 24 , 2) #np.arrange() method generates an array of sequential numbers with (start, stop, step) syntax.
print("standard array:",numbers_odd)

array_3d = numbers_odd.reshape(2,3,2) # (layers, rows, columns)
print("reshaped array:",array_3d)

""" 
output:
[[[ 1  3]
  [ 5  7]
  [ 9 11]]

 [[13 15]
  [17 19]
  [21 23]]]

This is a 3D array with a shape of (2, 3, 2):

The first dimension (axis 0) has a size of 2. (layers)
The second dimension (axis 1) has a size of 3.(three rows)
The third dimension (axis 2) has a size of 2.(2 columns)
"""
