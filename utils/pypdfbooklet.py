#!/usr/bin/env python

# This script are licensed under GPL 3 or higher
# Author: Angel Berlanas Vicente

import PythonMagick
from pyx import *
import sys
import argparse

def main():
	
	# Parser creation with a simple description
	parser = argparse.ArgumentParser(prog='pypdfbooklet',description='Pdfbooklet python implementation')
	# Add arguments to parser
	parser.add_argument('--japan-order', help='Japan order for images or pages', action='store_true')
	parser.add_argument('--keep-resolution',help='Keep the original aspect ration and resolution',action='store_true')
	parser.add_argument('--images', help='list of images',nargs='*' )
	parser.add_argument('--pdfoutput', help='Pdf generated',nargs=1)
	parser.add_argument('--pdfinput',help='Pdf to be bookleted', nargs=1)
	
	
	args = parser.parse_args()
	print args
	
	
	
	
if __name__ == "__main__":
    main()
