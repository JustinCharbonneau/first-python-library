from setuptools import setup

setup(name='justin_py',
      version='0.1',
      description='A simple library for me',
      url='https://github.com/justincharbonneau/first-python-library',
      author='Justin Charbonneau',
      author_email='justin.m.charbonneau@gmail.com',
      license='MIT',
      zip_safe=False,
      install_requires=['pandas'],
      include_package_data=True
      )