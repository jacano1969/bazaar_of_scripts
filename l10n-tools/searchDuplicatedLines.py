#!/usr/bin/env python

import sys

if (len(sys.argv) < 2):
	print "Usage"
	print "searchDuplicatedLines.py file"
	sys.exit()
	
linesSeen = set() 
numBlankLines = 0
lineNumber = 0
fileOpen = open(sys.argv[1],"r")

for line in fileOpen:
	lineNumber = lineNumber + 1
	if not line.strip() == '' and not line.strip() == '\n':
		if line not in linesSeen:
			linesSeen.add(line)
		else:
			if not line.startswith("#"):
				print str(lineNumber) + ":" + line.strip()
	else:
		numBlankLines = numBlankLines + 1
print numBlankLines

sys.exit()
