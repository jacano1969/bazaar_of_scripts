#!/usr/bin/env python
# -*- coding: utf-8 -*-


from distutils.core import setup
from distutils.extension import Extension
import os
import subprocess


setup(  name            = "python-potools",
	description	= "A library to manipulate po files and solve some braindamage",
	version          	= "0.1",
	author           	= "Angel Berlanas Vicente",
	author_email	= "angel.berlanas@gmail.com",
	url              	= "http://github.com/aberlanas/python-potools/",
	license		= "GPLv3",
	platforms		= ['posix'],
	package_dir      = {'': 'src'},
	py_modules         = ['potools']
	)


