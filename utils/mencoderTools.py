#!/usr/bin/env python

# This script is licensed under GPL v3 or higher.
# mencoder -idx $1 -ovc lavc -oac lavc -lavcopts vcodec=mpeg2video -of mpeg -o $1.mpg
# You must install mencoder
#mencoder $1 -ovc xvid -oac mp3lame -xvidencopts pass=1 -o $1.avi

import sys
import argparse
import subprocess
import os
import types


def tompg2(file_input,file_output,debug=False):
	
	if (debug):
		print("[DEBUG] tompg2 is invoked")
		
	#TODO
	print("mencoder -idx "+file_input[0]+" -ovc lavc -oac lavc -lavcopts vcodec=mpeg2video -of mpeg -o "+file_output+" ")

def main():
	
	# Parser creation with a simple description
	parser = argparse.ArgumentParser(prog='mencoderTools',add_help=False)
	
	# Parser show help
	parser.add_argument('--help', help='Show help', action = 'store_true', default=False)
	
	# Parser add debug options
	parser.add_argument('--debug', help='Show debug messages', action='store_true', default=False)
	
	# Parser  mpg2
	parser.add_argument('--tompg2',help="Encoding in mpeg2video", action = 'store_true', default=False)
	
	# Parser arguments input
	parser.add_argument('--input', help='Input files', nargs='+')
	
	# Parser arguments output
	parser.add_argument('--output', help='Output file', nargs=1)
	parser.add_argument('--outputdirectory', help='Output directory', nargs=1)
	
	
	results = parser.parse_args()
	
	# Help
	if (results.help):
		parser.print_help()
	
	if (results.debug):
		print("[DEBUG] Debug is enabled")
		
	if (results.tompg2):
		try:
			if (results.input):
				if (results.output):
					this_output=results.output
				else:
					this_output=" "+results.input[0]+".mpg"
				
				if(results.debug):
					print("[DEBUG]: the output file is "+ this_output)
				tompg2(results.input,this_output,results.debug)
			
			else:
				print("[ERROR]: A input file is needed")
				sys.exit()
		except:
			print("[ERROR]: An error ocurred")
			pass
	

if __name__ == "__main__":
    main()