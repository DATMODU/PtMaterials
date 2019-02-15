# -*- coding: utf-8 -*-
import swig_ex3

test_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(test_tuple, "Tuple을 다 더한다.")
print("결과:", swig_ex3.sum_tuple(test_tuple))

test_list1 = [1, 2, 3, 4, 5]
test_list2 = [6, 7, 8, 9, 10]
print("\n", test_list1, "과", test_list2, "List를 합친다.")
ret_list = swig_ex3.concat_list(test_list1, test_list2)
print("리턴된 타입:", type(ret_list))
print("결과:", ret_list)

test_dict = {"key1": 1, "key2": 2, "key3": 3}
print("\n", test_dict, "에서 key2의 값을 찾는다.")
print("결과:", swig_ex3.get_dict_value(test_dict, "key2"))
