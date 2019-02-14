# -*- coding: utf-8 -*-
import swig_ex4
import numpy as np

np_array = np.array([5, 4, 3, 2, 1])
print(swig_ex4.find_max(np_array))

np_array = swig_ex4.create_np_array(10)
print(type(np_array))
print(np_array)

np_array1 = np.array([1, 2, 3, 4, 5])
np_array2 = np.array([6, 7, 8, 9, 10])
np_array = swig_ex4.sum_two_np_array(np_array1.size, np_array1, np_array2)
print(type(np_array))
print(np_array)

np_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
swig_ex4.plus_one_np_array(np_array)
print(type(np_array))
print(np_array)
