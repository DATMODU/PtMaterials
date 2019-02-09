#include "Python.h"

static PyObject* add_func(PyObject* self, PyObject* args) {
	int arg1 = 0;
	int arg2 = 0;

	if ( !PyArg_ParseTuple(args, "ll", &arg1, &arg2) ) {
		return NULL;
	}

	int ret = arg1 + arg2;

	return Py_BuildValue("i", ret);
}

static PyMethodDef simpleMethods[] = {
	{"add", add_func, METH_VARARGS, "Add two integers"},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef simpleModule = {
	PyModuleDef_HEAD_INIT,
	"simple",
	NULL,
	-1,
	simpleMethods
};

PyMODINIT_FUNC
PyInit_simple(void)
{
    return PyModule_Create(&simpleModule);
}
