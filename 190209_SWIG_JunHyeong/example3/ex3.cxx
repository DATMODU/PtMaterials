// example3/ex3.cxx
#include "ex3.h"

PyObject* sum_tuple(PyObject* input_tuple) {
    if ( !PyTuple_Check(input_tuple) ) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    const Py_ssize_t tuple_size = PyTuple_Size(input_tuple);
    PyObject* iter = PyObject_GetIter(input_tuple);

    if ( NULL == iter ) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    long ret = 0;
    PyObject* item = NULL;

    while( item = PyIter_Next(iter) ){
        if ( PyLong_Check(item) ) {
            ret += PyLong_AsLong(item);
        }

        Py_DECREF(item);
    }

    Py_DECREF(iter);
    
    return PyLong_FromLong(ret);
}

PyObject* concat_list(PyObject* input_list1, PyObject* input_list2) {
    if ( !PyList_Check(input_list1) || !PyList_Check(input_list2) ) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    const Py_ssize_t list1_size = PyList_Size(input_list1);
    const Py_ssize_t list2_size = PyList_Size(input_list2);
    const Py_ssize_t ret_list_size = list1_size + list2_size;
	Py_ssize_t i = 0;

    PyObject* ret_list = PyList_New(ret_list_size);
	PyObject* iter1 = PyObject_GetIter(input_list1);
	PyObject* iter2 = PyObject_GetIter(input_list2);

    if ( NULL == ret_list || NULL == iter1 || NULL == iter2 ) {
        Py_INCREF(Py_None);
        return Py_None;
    }

	PyObject* item = NULL;

	while( item = PyIter_Next(iter1) ){
        PyList_SetItem(ret_list, i, item);
		i++;
    }

	while( item = PyIter_Next(iter2) ){
        PyList_SetItem(ret_list, i, item);
		i++;
    }

    Py_DECREF(iter1);
	Py_DECREF(iter2);

	return ret_list;
}

PyObject* get_dict_value(PyObject* input_dict, char* key_name) {
	if ( !PyDict_Check(input_dict) ) {
		Py_INCREF(Py_None);
        return Py_None;
	}

	return PyDict_GetItemString(input_dict, key_name);
}
