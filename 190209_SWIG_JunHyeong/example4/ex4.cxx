// example4/ex4.cxx
#include "ex4.h"

int find_max(int *in_arr, int in_size) {
	int ret = INT_MIN;

	for ( int i=0 ; i<in_size ; i++ ) {
		if ( ret < in_arr[i] ) {
			ret = in_arr[i];
		}
	}

	return ret;
}

void create_np_array(int* out_arr, int out_size) {
	for ( int i=0 ; i<out_size ; i++ ) {
		out_arr[i] = i;
	}
}

void sum_two_np_array(int* out_arr, int out_size, int *in_arr1, int in_size1, int *in_arr2, int in_size2) {
	for ( int i=0 ; i<out_size ; i++ ) {
		out_arr[i] = in_arr1[i] + in_arr2[2];
	}
}

void plus_one_np_array(int* io_arr, int io_size1, int io_size2) {
	for ( int i=0 ; i<io_size2 ; i++ ) {
		for ( int j=0 ; j<io_size1 ; j++ ) {
			io_arr[(i*io_size1) + j]++;
		}
	}
}
