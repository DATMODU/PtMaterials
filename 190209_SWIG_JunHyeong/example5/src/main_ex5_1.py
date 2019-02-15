# -*- coding: utf-8 -*-
import time
import swig_ex5.core.global_func as gf

for i in range(100):
	print("time.time(): {0:10.6f}, c++: {1:10.6f}".format(time.time(), gf.get_timestamp_16d()*0.000001))
