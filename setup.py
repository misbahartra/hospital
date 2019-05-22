# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

with open('requirements.txt') as f:
	install_requires = f.read().strip.split('\n')

version = '0.0.1'
#requirements = parse_requirements("requirements.txt", session="")

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
