# -*- coding: utf-8 -*-
import os
import numpy

from setuptools import setup, Extension

install_requires = [
	"numpy",
	"matplotlib",
]

packages = [
	"swig_ex5",
	"swig_ex5.core",
]

ext_modules = [
	Extension(
		name="swig_ex5.core._global_func",
		sources=[
			os.path.join("src", "core", "global_func_wrap.cxx"),
			os.path.join("src", "core", "global_func.cxx"),
		],
	),
	Extension(
		name="swig_ex5.core._calc_func",
		sources=[
			os.path.join("src", "core", "calc_func_wrap.cxx"),
			os.path.join("src", "core", "calc_func.cxx"),
		],
		include_dirs=[
			numpy.get_include(),
		],
	),
]

setup(
	name="swig_ex5",
	version="1.0.0",
	description="SWIG Example5",
	install_requires=install_requires,
	ext_modules=ext_modules,
	packages=packages,
	package_dir={"swig_ex5": "src"},
)
