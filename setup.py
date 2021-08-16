# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in estores/__init__.py
from estores import __version__ as version

setup(
	name='estores',
	version=version,
	description='Estores',
	author='Estores',
	author_email='omar.ja93@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
