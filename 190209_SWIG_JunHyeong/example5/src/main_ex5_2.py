# -*- coding: utf-8 -*-
import numpy as np
import swig_ex5.core.global_func as gf
import swig_ex5.core.calc_func as cf
import matplotlib.pyplot as plt

data_size = []
using_numpy = []
c_using_rand_access = []
c_using_iterator = []
c_using_ndarray = []


for i in range(1, 100):
	data_size.append(i * 10000)

for n in data_size:
	data_ndarr = np.random.random_sample(n)
	data_list = data_ndarr.tolist()

	st_time = gf.get_timestamp_16d()
	ret = data_ndarr.std()
	ed_time = gf.get_timestamp_16d()

	using_numpy.append(ed_time - st_time)

	st_time = gf.get_timestamp_16d()
	ret = cf.get_std_using_rand_access(data_list)
	ed_time = gf.get_timestamp_16d()

	c_using_rand_access.append(ed_time - st_time)

	st_time = gf.get_timestamp_16d()
	ret = cf.get_std_using_iterator(data_list)
	ed_time = gf.get_timestamp_16d()

	c_using_iterator.append(ed_time - st_time)

	st_time = gf.get_timestamp_16d()
	ret = cf.get_std_using_ndarray(data_ndarr)
	ed_time = gf.get_timestamp_16d()

	c_using_ndarray.append(ed_time - st_time)

plt.plot(data_size, using_numpy, label="np.std()")
plt.plot(data_size, c_using_rand_access, label="C++(Input List, Random Access)")
plt.plot(data_size, c_using_iterator, label="C++(Input List, Iterator)")
plt.plot(data_size, c_using_ndarray, label="C++(Input np.array, Random Access)")
plt.legend(loc='upper left')
plt.xlabel("Data Length")
plt.ylabel("Time (Micro Seconds)")
plt.show()
