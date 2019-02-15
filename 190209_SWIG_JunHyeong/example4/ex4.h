// example4/ex4.h
#pragma once

#include <Python.h>

extern "C" {
    int find_max(int* in_arr, int in_size);
    void create_np_array(int* out_arr, int out_size);
    void sum_two_np_array(int* out_arr, int out_size, int* in_arr1, int in_size1, int* in_arr2, int in_size2);
    void plus_one_np_array(int* io_arr, int io_size1, int io_size2);
}
