# 성능 테스트

- Plot TimeStamp: main_ex5_1.py
- Standard Deviation: main_ex5_2.py

## Build/Setup
src/core에서
```commandline
swig -c++ -python global_func.i
swig -c++ -python calc_func.i
```

root에서
```commandline
python setup.py build
python setup.py install
```
