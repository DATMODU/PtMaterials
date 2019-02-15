# -*- coding: utf-8 -*-
import swig_ex1

print("Python C/API만을 이용하여 두 정수를 더함")

a = 1
b = 2

c = swig_ex1.add(a, b)

print("{0} + {1} = {2}".format(a, b, c))
