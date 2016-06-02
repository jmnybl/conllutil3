from __future__ import print_function
from setuptools import setup, find_packages

setup(
    name='conllutil3',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.2.1',

    description='Simple functions to process CONLL-U files.',
    long_description="Simple functions to process CONLL-U files.",

    # The project's main homepage.
    url='https://github.com/jmnybl/conllutil3',

    # Author details
    author='Jenna Kanerva and other contributors',
    author_email='jmnybl@utu.fi',

    # Choose your license
    license='GNU GPL 2',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GPL',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],

    # What does your project relate to?
    keywords='universal dependencies, conll-u',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    py_modules=["conllutil3"],
    
  #  install_requires=['numpy>=1.1.0']
)
