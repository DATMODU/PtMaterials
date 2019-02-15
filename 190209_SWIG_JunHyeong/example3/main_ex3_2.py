# -*- coding: utf-8 -*-
import swig_ex3

print(swig_ex3.TMP_NUM)
print(swig_ex3.TIGER, swig_ex3.DOG)

candle = swig_ex3.Candle(1000, 5000, 5500, 4500, 4800)
print(candle.time, candle.close)

myclass = swig_ex3.MyClass()
print(myclass.get_my_value())
myclass.set_my_value(20)
print(myclass.get_my_value())
