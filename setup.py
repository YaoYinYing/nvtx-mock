import os
import sys
import shutil
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

# Define the target include directory
python_include_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(sys.executable)), '..', 'include'))

package_dir=os.path.dirname(os.path.abspath(__file__))

def copy_headers():
    print(f'Copying headers {package_dir}/nvtx/c/include/nvtx3 to {python_include_path}')
    shutil.copytree(os.path.join(package_dir, 'nvtx/c/include/nvtx3'),os.path.join(python_include_path,'nvtx3'))

class CustomBuildExt(build_ext):
    def run(self):
        copy_headers()
        build_ext.run(self)

# Package metadata
setup(
    name='nvtx-mock',
    version='0.1.0',
    author='Yinying Yao',
    author_email='yaoyy.hi at gmail.com',
    description='A mock package for NVTX C headers.',
    ext_modules=[Extension('dummy_extension', sources=['dummy.c'])],  # A dummy extension to trigger the build process
    cmdclass={'build_ext': CustomBuildExt},
)