import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([[10], [20], [30]])
result = arr1 + arr2
print(result)

""" 
arr1:      [[1], [2], [3]]   (broadcasted)
arr2:      [[10], [20], [30]]
result:    [[1 + 10], [2 + 20], [3 + 30]]
result:    [[11], [22], [33]] 
 """
