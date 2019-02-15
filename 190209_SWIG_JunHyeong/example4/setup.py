# -*- coding: utf-8 -*-
import numpy

from setuptools import setup, Extension

install_requires = [
	"numpy",
]

packages = [
	"swig_ex4",
]

ext_modules = [
	Extension(
		name="_swig_ex4",
		sources=["ex4.cxx", "ex4_wrap.cxx"],
		include_dirs=[numpy.get_include()],
	),
]

setup(
	name="swig_ex4",
	version="1.0.0",
	description="SWIG Example4",
	install_requires=install_requires,
	ext_modules=ext_modules,
	packages=packages,
	package_dir={"swig_ex4": ""},
)
