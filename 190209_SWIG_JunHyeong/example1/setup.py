# -*- coding: utf-8 -*-
from setuptools import setup, Extension

ext_modules = [
	Extension(
		name="swig_ex1",
		sources=["ex1.c"]
	),
]

setup(
	name="swig_ex1",
	version="1.0.0",
	description="SWIG Example1",
	ext_modules=ext_modules,
)
