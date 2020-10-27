# -*- coding: utf-8 -*-
# 

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package for Tic Toc Toe',
    long_description=readme,
    author='Patrick McCarthy',
    author_email='patrick.mccarthy56@gmail.com',
    url='https://github.com/TrickMcCarthy',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

