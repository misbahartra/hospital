# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
#from pip.req import parse_requirements
from pip.req import parse_requirements
import re, ast

version = '0.0.1'
with open('hospital_bed_management/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(__version_re.search(
		f.read().decode('utf-8')).group(1)))
requirements = parse_requirements("requirements.txt",session="")
setup(
	name='hospital_bed_management',
	version=version,
	description='Charitable Trust : Hospital Bed Management System',
	author='Bed Management System',
	author_email='priya.s@indictranstech.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=[str(ir.req) for ir in requirements],
	dependency_links=[str(ir._link) for ir in requirements if ir._link]
)
