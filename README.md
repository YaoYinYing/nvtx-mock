# NVTX-Mock: A Mock for NVTX on Non-CUDA Platforms

NVTX-Mock is a Python package that enables using the NVIDIA NVTX (NVIDIA Tools Extension Library) on platforms without CUDA support, such as macOS. It provides a mock implementation of the NVTX C headers, allowing you to develop and test your code that uses NVTX markers and ranges on these platforms.

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/YaoYinYing/nvtx-mock)

## Features

- Mocks the NVTX C headers for non-CUDA platforms like macOS.
- Enables cross-platform development and testing of NVTX-enabled code.
- Installs the mock NVTX headers to the Python installation's `include` directory.

## Requirements

- Python 3.6 or later

## Installation

You can install NVTX-Mock directly from PyPI using `pip`:
```sh
pip install nvtx-mock
```
This command will clone the repository, build the package, and install it, copy those NVTX headers to Python's `include` directory.
```shell
ls $(dirname $(which python))/../include |grep nvtx
```

After that, you can install the Python-binding of NVTX:
```sh
pip install nvtx
```
This will install the genuine NVTX library, and your code will function as expected.

## Usage
When running NVTX-enabled code on a non-CUDA platform, include the NVTX headers as usual.
Since NVTX-Mock provides a mock implementation, the NVTX functions will have no effect, but your code will compile and run without errors.

## Warning: Installing `nvtx-mock` on CUDA-Enabled Platforms

This package is **intended only for systems that do not have CUDA or the genuine NVTX library installed**.

Installing `nvtx-mock` on a CUDA-enabled system **may override or interfere with the original NVIDIA-provided NVTX headers**, particularly if:

- Your Python environment's `include/` directory is in your system’s compiler header search path.
- You rely on real NVTX instrumentation (e.g., in `nvtx`-annotated CUDA profiling code).

In such environments, the mocked headers installed by `nvtx-mock` may:
- **Override** the real `nvtx3/nvToolsExt.h`
- Cause runtime profiling or compilation errors
- Silently disable real profiling behavior

### Do Not Use If:
- You're running on a machine with CUDA and NVTX already available.
- You need real NVTX markers for performance profiling or tracing.

### Safe Use Cases:
- macOS development
- CI/CD pipelines
- Testing environments where no real NVTX instrumentation is expected

> **When in doubt**: do not install `nvtx-mock` in production CUDA environments. Use virtual environments or container isolation to avoid polluting system headers.


## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License
NVTX-Mock is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
NVIDIA for providing the NVTX library.
