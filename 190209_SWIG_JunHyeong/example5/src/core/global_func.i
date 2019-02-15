// example5/src/core/global_func.i
%module global_func

%{
#define SWIG_FILE_WITH_INIT
#include "global_func.h"
%}

%include "global_func.h"
