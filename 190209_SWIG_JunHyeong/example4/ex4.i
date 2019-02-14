// example4/ex4.i
%module swig_ex4

%{
#define SWIG_FILE_WITH_INIT
#include "ex4.h"
%}

%include "numpy.i"

%init %{
import_array();
%}

%apply (int* IN_ARRAY1, int DIM1) {(int* in_arr, int in_size)};
%apply (int* ARGOUT_ARRAY1, int DIM1) {(int* out_arr, int out_size)};
%apply (int* IN_ARRAY1, int DIM1) {(int *in_arr1, int in_size1), (int *in_arr2, int in_size2)};
%apply (int* INPLACE_ARRAY2, int DIM1, int DIM2) {(int* io_arr, int io_size1, int io_size2)};

%include "ex4.h"
