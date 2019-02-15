# -*- coding: utf-8 -*-
import swig_ex3

print("C++내에서 출력:")
swig_ex3.print_in_cxx()

print("\nPython에서 넘겨준 문자열을 C++내에서 출력:")
swig_ex3.print_in_cxx("안녕하세요 !\n")
