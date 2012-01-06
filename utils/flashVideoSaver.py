#!/usr/bin/env python

# This script is licensed under GPL v3 or higher.
# Flash Videos are now under /proc/NUMBER_OF_PROCESS/fd -> /tmp/FLASH.XXX as a deleted symbolic link

import sys
import argparse
import subprocess
import os
import types

def list_videos(debug=False):
	
	if (debug)
		print("[DEBUG] List Videos")
	
	


def main():
	
	# Parser creation with a simple description
	parser = argparse.ArgumentParser(prog='flashVideoSaver',add_help=False)
	
	# Parser show help
	parser.add_argument('--help', help='Show help' , action = 'store_true', default=False)
	
	# Parser add debug options
	parser.add_argument('--debug', help='Show debug messages', action='store_true', default=False)
	
	# Parser  list 
	parser.add_argument('--list',help="List videos", action = 'store_true', default=False)
	
	results = parser.parse_args()
	
	# Help
	if (results.help):
		parser.print_help()
	
	if (results.debug):
		print("[DEBUG] Debug is enabled")
		
	if (results.list):
		list_videos(debug)


if __name__== "__main__":
	main()