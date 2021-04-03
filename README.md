# Fibonacci function implemented in C and Python

## Setup
The setup is to compile pyc_module.c into a python readable dll.

## C
The C code is compiled to a .pyd (on Windows) or .so (Linux) and is imported into main.py

## Python
Pulls together the C implemented fib function, and the Python implemented fib function. 
It then runs one after another measuring how quick it calculates the fib of the supplied
int.
