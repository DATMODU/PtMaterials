// example5/src/core/ex5.cxx
#include <chrono>
#include "calc_func.h"

double get_std_using_rand_access(PyObject* in_list) {
	double std = 0;
	double sum = 0;
	double square_sum = 0;
	double buffer = 0;

	const Py_ssize_t tot_size = PyList_Size(in_list);
	Py_ssize_t i = 0;

	for ( i=0 ; i<tot_size ; i++ ) {
		buffer = PyFloat_AS_DOUBLE(PyList_GET_ITEM(in_list, i));
		sum += buffer;
		square_sum += (buffer * buffer);
	}

	const double mean = sum / (double)tot_size;
	std = sqrt((square_sum / (double)tot_size) - (mean * mean));

	return std;
}

double get_std_using_iterator(PyObject* in_list) {
	double std = 0;
	double sum = 0;
	double square_sum = 0;
	double buffer = 0;
	const double tot_size = (double)PyList_Size(in_list);

	PyObject* iter = PyObject_GetIter(in_list);
	PyObject* item = NULL;

	while ( item = PyIter_Next(iter) ) {
		buffer = PyFloat_AS_DOUBLE(item);
		sum += buffer;
		square_sum += (buffer * buffer);
		Py_DECREF(item);
	}

	Py_DECREF(iter);

	const double mean = sum / (double)tot_size;
	std = sqrt((square_sum / (double)tot_size) - (mean * mean));

	return std;
}

double get_std_using_ndarray(double* in_arr, int in_size) {
	double std = 0;
	double sum = 0;
	double square_sum = 0;
	double buffer = 0;
	int i = 0;

	for ( i=0 ; i<in_size ; i++ ) {
		buffer = in_arr[i];
		sum += buffer;
		square_sum += (buffer * buffer);
	}

	const double mean = sum / (double)in_size;
	std = sqrt((square_sum / (double)in_size) - (mean * mean));

	return std;
}
