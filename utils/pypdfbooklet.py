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
	parser.add_argument('--images', help='list of images', action='store_images')
	# Created the parser for "--images" command
	subparsers = parser.add_subparsers(help='List of images')
	parser_a = subparsers.add_parser('a', help='a help')
	
	
	
	
	
	
	args = parser.parse_args()
	print args
	
	
if __name__ == "__main__":
    main()
