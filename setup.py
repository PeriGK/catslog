"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from codecs import open
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name="catslog",
    version='1.0.9',
    py_modules=['catslog'],
    description="Logs the execution of the wrapped function and, if applicable, does a basic handling of the raised exception. Please check the github page for more detailed instructions",
    url='https://github.com/PeriGK/catslog',
    author='Periklis Gkolias',
    long_description='Please check the README file in the github repository, on the left',
    author_email='per.gkolias@gmail.com',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',],
    keywords='exceptions exception-handling logging',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
)
