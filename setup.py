import sys
import os
from distutils.core import setup, Extension
from shutil import copy2, rmtree

sys.argv.append("build")

if sys.platform == "win32":
    sys.argv.append("-cmingw32")

module = Extension("c_fib", sources=["c_files/pyc_module.c"])

setup(name="c_fib_package", version="1.0", description="Fibonacci in C", ext_modules=[module])

for _file in os.listdir("build"):
    if "lib" in _file:
        for compiled_file in os.listdir(f"build/{_file}"):
            copy2(f"build/{_file}/{compiled_file}", f"{compiled_file}")


rmtree("build")
