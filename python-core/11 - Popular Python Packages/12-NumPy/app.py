import numpy as np


array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)
print(type(array)) # <class 'numpy.ndarray'> nd = n-dimensional
print(array.shape)

array = np.zeros(shape=(3, 4), dtype=int)
array = np.ones(shape=(3, 4), dtype=int)
array = np.full(shape=(3, 4), fill_value=5, dtype=int)
array = np.random.random((3, 4))
print(array)
print(array[0, 0])
print(array[0][0])
print(array > 0.5) # returns array of bools corresponding to expr
print(array[array > 0.2]) # returns array of vals corresponding to expr
print('arr sum:', np.sum(array)) # returns sum of array vals
print('floors:', np.floor(array)) # returns array of floor vals
print('ceil:', np.ceil(array)) # returns array of floor vals
print('round:', np.round(array)) # returns array of floor vals
first = np.array([1, 2, 3])
second = np.array([1, 2, 3])
print(first + second)
print(first + 2)
inch = np.array([1, 2, 3])
cm = inch * 2.54
print(cm)