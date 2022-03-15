"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description_list = f.readlines()

    long_description = ""

    for line in long_description_list:
        long_description += line
    long_description = long_description.replace("\r", "")

setup(
    name='winput',
    
    version='1.4.0',

    description='Capture and send keyboard and mouse input',
    
    long_description=open(path.join(here, 'README.md')).read(),
    long_description_content_type='text/markdown',

    # The project's main homepage.
    url='https://github.com/Zuzu-Typ/winput',

    # Author details
    author='Zuzu_Typ',
    author_email='zuzu.typ@gmail.com',
    
    license='zlib/libpng license',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment',
        'Topic :: Software Development :: Libraries',
        
        'License :: OSI Approved :: zlib/libpng License',
        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    
    keywords='record send input cursor mouse keyboard keys hook hooks pyhook windows user32.dll user32',
    
    packages=["winput"],
)
