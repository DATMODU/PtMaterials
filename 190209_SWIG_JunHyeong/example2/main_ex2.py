# -*- coding: utf-8 -*-
import swig_ex2

print("SWIG를 사용하여 두 정수를 더함")

a = 1
b = 2

c = swig_ex2.add(a, b)

print("{0} + {1} = {2}".format(a, b, c))
