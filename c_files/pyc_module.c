#include <Python.h>
#include "fibonacci.h"


static PyObject* fib(PyObject* self, PyObject* args) {
    int n;
    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;

    return Py_BuildValue("i", Cfib(n));
}


static PyMethodDef myMethods[] = {
    {"fib", fib, METH_VARARGS, "Calculate the fibonacci numbers."},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef c_fib = {
    PyModuleDef_HEAD_INIT,
    "c_fib",
    "Fibonacci module in C",
    -1,
    myMethods
};


PyMODINIT_FUNC PyInit_c_fib(void) {
    return PyModule_Create(&c_fib);
}
