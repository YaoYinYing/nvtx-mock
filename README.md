# NVTX-Mock: A Mock Package for NVTX C Headers

NVTX-Mock is a Python package that provides a convenient way to install NVIDIA NVTX C headers alongside your Python project. It's designed to simplify the integration of NVTX profiling tools in your C/C++ code when working with Python projects.

## Features

- Installs the `nvtx3` directory containing NVTX C headers to the Python installation's `include` directory.
- Uses a custom `setup.py` script to copy the headers during the build process.
- Includes a dummy C extension to trigger the build process.
