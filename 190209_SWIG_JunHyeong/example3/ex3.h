// example3/ex3.h
#pragma once

#include <Python.h>

void print_in_cxx();
void print_in_cxx(char* str);

#define TMP_NUM 123456
enum ANIMAL { CAT, DOG, TIGER, ELEPHANT, MONKEY };

struct Candle {
	Candle(long t, long o, long h, long l, long c) {
		time = t;
		open = o;
		high = h;
		low = l;
		close = c;
	}

	long time;
	long open;
	long high;
	long low;
	long close;
};

class MyClass {
public:
	MyClass();
	~MyClass();

	void set_my_value(int val);
	int get_my_value();

private:
	int my_value;
};

PyObject* sum_tuple(PyObject* input_tuple);
PyObject* concat_list(PyObject* input_list1, PyObject* input_list2);
PyObject* get_dict_value(PyObject* input_dict, char* key_name);