# -*- coding: utf-8 -*-
from setuptools import setup, Extension

packages = [
	"swig_ex2",
]

ext_modules = [
	Extension(
		name="_swig_ex2",
		sources=["simple.c", "simple_wrap.c"],
	),
]

setup(
	name="swig_ex2",
	version="1.0.0",
	description="SWIG Example2",
	ext_modules=ext_modules,
	packages=packages,
	package_dir={"swig_ex2": ""},
)
