# -*- coding: utf-8 -*-
import swig_ex3

test_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(swig_ex3.sum_tuple(test_tuple))

test_list1 = [1, 2, 3, 4, 5]
test_list2 = [6, 7, 8, 9, 10]
print(swig_ex3.concat_list(test_list1, test_list2))

test_dict = {"key1": 1, "key2": 2, "key3": 3}
print(swig_ex3.get_dict_value(test_dict, "key2"))
