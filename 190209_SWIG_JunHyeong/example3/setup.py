# -*- coding: utf-8 -*-
from setuptools import setup, Extension

packages = [
	"swig_ex3",
]

ext_modules = [
	Extension(
		name="_swig_ex3",
		sources=["ex3.cxx", "ex3_wrap.cxx"],
	),
]

setup(
	name="swig_ex3",
	version="1.0.0",
	description="SWIG Example3",
	ext_modules=ext_modules,
	packages=packages,
	package_dir={"swig_ex3": ""},
)
