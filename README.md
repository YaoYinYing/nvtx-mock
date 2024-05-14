# NVTX-Mock: A Mock for NVTX on Non-CUDA Platforms

NVTX-Mock is a Python package that enables using the NVIDIA NVTX (NVIDIA Tools Extension Library) on platforms without CUDA support, such as macOS. It provides a mock implementation of the NVTX C headers, allowing you to develop and test your code that uses NVTX markers and ranges on these platforms.

## Features

- Mocks the NVTX C headers for non-CUDA platforms like macOS.
- Enables cross-platform development and testing of NVTX-enabled code.
- Installs the mock NVTX headers to the Python installation's `include` directory.

## Requirements

- Python 3.6 or later

## Installation

You can install NVTX-Mock directly from the GitHub repository using `pip`:
```sh
pip install git+https://github.com/YaoYinYing/nvtx-mock --force-reinstall
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

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License
NVTX-Mock is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
NVIDIA for providing the NVTX library.