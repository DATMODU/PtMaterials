// example5/src/core/ex5.h
#pragma once

#include <Python.h>

double get_std_using_rand_access(PyObject* in_list);
double get_std_using_iterator(PyObject* in_list);
double get_std_using_ndarray(double* in_arr, int in_size);
