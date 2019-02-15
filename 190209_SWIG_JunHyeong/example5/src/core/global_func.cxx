// example5/src/core/global_func.cxx
#include <chrono>
#include "global_func.h"


PyObject* get_timestamp_13d() {
    const long long ts = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now().time_since_epoch()).count();
	return PyLong_FromLongLong(ts);
}

PyObject* get_timestamp_16d() {
    const long long ts = std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::system_clock::now().time_since_epoch()).count();
    return PyLong_FromLongLong(ts);
}
