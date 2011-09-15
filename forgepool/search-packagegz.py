#!/usr/bin/env python

# Copyright
# This script is licensed under GPL v3 or higher.


import sys
import gzip

def readGzip():
	gzipFile = gzip.open('Packages.gz','r')
	gzipFileContent = gzipFile.read()
	gzipFile.close()
	return gzipFileContent



# Main Script
componentPackages = readGzip()

print (componentPackages)


sys.exit()
