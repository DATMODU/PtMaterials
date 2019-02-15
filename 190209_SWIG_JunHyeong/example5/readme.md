# 성능 테스트

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
