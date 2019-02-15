# -*- coding: utf-8 -*-
import numpy as np
import swig_ex5.core.global_func as gf
import swig_ex5.core.calc_func as cf

data_ndarr = np.random.random_sample(10000000)
data_list = data_ndarr.tolist()

st_time = gf.get_timestamp_16d()
ret = data_ndarr.std()
ed_time = gf.get_timestamp_16d()

print(ret)
print(ed_time - st_time)

st_time = gf.get_timestamp_16d()
ret = cf.get_std_using_rand_access(data_list)
ed_time = gf.get_timestamp_16d()

print(ret)
print(ed_time - st_time)

st_time = gf.get_timestamp_16d()
ret = cf.get_std_using_iterator(data_list)
ed_time = gf.get_timestamp_16d()

print(ret)
print(ed_time - st_time)

st_time = gf.get_timestamp_16d()
ret = cf.get_std_using_ndarray(data_ndarr)
ed_time = gf.get_timestamp_16d()

print(ret)
print(ed_time - st_time)
