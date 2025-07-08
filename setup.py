import os
import sys
import shutil
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

# Define the target include directory
python_include_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(sys.executable)), '..', 'include'))

def copy_headers():
    target_dir=os.path.join(python_include_path,'nvtx3')
    print(f'Copying headers nvtx/c/include/nvtx3 to {target_dir}')
    if os.path.exists(target_dir):
        print(f'Warning: {target_dir} already exists.')
    else:
        shutil.copytree('nvtx/c/include/nvtx3',target_dir)

class CustomBuildExt(build_ext):
    def run(self):
        copy_headers()
        build_ext.run(self)

# Package metadata
setup(
    name='nvtx-mock',
    version='0.1.2',
    author='Yinying Yao',
    author_email='yaoyy.hi@gmail.com',
    description='A mock package for NVTX C headers.',
    ext_modules=[Extension('dummy_extension', sources=[])],  # A dummy extension to trigger the build process
    cmdclass={'build_ext': CustomBuildExt},
)