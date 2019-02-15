// example5/src/core/global_func.h
#pragma once

#include <Python.h>

extern "C" {
    PyObject* get_timestamp_13d();
    PyObject* get_timestamp_16d();
}