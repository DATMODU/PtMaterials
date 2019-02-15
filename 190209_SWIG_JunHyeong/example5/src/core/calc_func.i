// example5/src/core/ex5.i
%module calc_func

%{
#define SWIG_FILE_WITH_INIT
#include "calc_func.h"
%}

%include "numpy.i"

%init %{
import_array();
%}

%apply (double* IN_ARRAY1, int DIM1) {(double* in_arr, int in_size)};

%include "calc_func.h"
