import time
import c_fib


def py_fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return py_fib(n - 1) + py_fib(n - 2)


target = int(input("What integer to fib to race C vs python? "))

t1 = time.time()
c_answer = c_fib.fib(target)
print(f"C took: {time.time() - t1:.3f}s to work out fib({target}) = {c_answer}")


t1 = time.time()
py_answer = py_fib(target)
print(f"Python took: {time.time() - t1:.3f}s to work out fib({target}) = {py_answer}")
