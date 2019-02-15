# -*- coding: utf-8 -*-
import swig_ex4
import numpy as np

np_array = np.array([5, 4, 3, 2, 1])
print(np_array, "에서 Max값을 찾는다.")
print("결과:", swig_ex4.find_max(np_array))

np_array = swig_ex4.create_np_array(10)
print("\n입력받은 사이즈만큼의 numpy.array를 생성한다")
print("생성된 객체의 타입:", type(np_array))
print("결과:", np_array)

np_array1 = np.array([1, 2, 3, 4, 5])
np_array2 = np.array([6, 7, 8, 9, 10])
np_array = swig_ex4.sum_two_np_array(np_array1.size, np_array1, np_array2)
print("\n두 numpy.array를 요소끼리 더한다. 입력1:", np_array1, "입력2:", np_array2)
print("생성된 객체의 타입:", type(np_array))
print("결과:", np_array)

np_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("\n기존의 2차원 numpy.array에서 각각의 요소에 1을 더한다.")
print("기존값:")
print(np_array)
swig_ex4.plus_one_np_array(np_array)
print("결과:")
print(np_array)
