#!/usr/bin/env python

# This script is licensed under GPL v3 or higher.
# Flash Videos are now under /proc/NUMBER_OF_PROCESS/fd -> /tmp/FLASH.XXX as a deleted symbolic link

import sys
import argparse
import subprocess
import os
import types
import re
import pickle

def set_re(debug=False):
	if(debug):
		print("[DEBUG] Creating regular expression")
		
	my_regex=re.compile('flashplayer',re.IGNORECASE)
	return my_regex

def list_videos(debug=False):
	
	if (debug):
		print("[DEBUG] List Videos")
	
	my_processes=subprocess.Popen(["ps","aux"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	
	my_regex_to_save=set_re()
	output = open('data.pkl', 'wb')
	pickle.dump(my_regex_to_save,output)
	
	my_regex=pickle.load('data.pkl	')
	#for my_process in myprocesses:
	for process_p in my_processes.stdout:
		print(my_regex)
		if my_regex.match(process_p):
			print(process_p)
		



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
	
	# Load REGULAR_EXPRESSION
	REGULAR_EXPRESSION=set_re(results.debug)
	
	if (results.debug):
		print("[DEBUG] Debug is enabled")
		
	if (results.list):
		list_videos(results.debug)


if __name__== "__main__":
	main()