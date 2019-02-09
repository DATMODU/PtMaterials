// example2/simple.i

%module swig_ex2

%{
#define SWIG_FILE_WITH_INIT
#include "simple.h"
%}

%include "simple.h"
