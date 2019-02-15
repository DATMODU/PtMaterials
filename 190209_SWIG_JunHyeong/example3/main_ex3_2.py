# -*- coding: utf-8 -*-
import swig_ex3

print("C++에서 define한 값")
print("type:", type(swig_ex3.TMP_NUM))
print("define된 TMP_NUM:", swig_ex3.TMP_NUM)

print("\nENUM")
print("type:", type(swig_ex3.CAT))
print("CAT:", swig_ex3.CAT, "DOG", swig_ex3.DOG, "TIGER", swig_ex3.TIGER)

print("\n구조체")
candle = swig_ex3.Candle(1000, 5000, 5500, 4500, 4800)
print("type:", type(candle))
print("입력된 time:", candle.time, "입력된 close:", candle.close)

print("\nC++ 클래스")
myclass = swig_ex3.MyClass()
print("type:", type(myclass))
print("초기값:", myclass.get_my_value())
myclass.set_my_value(20)
print("변경된값:", myclass.get_my_value())
