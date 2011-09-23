#!/usr/bin/env python

import sys
import re

# Usage
if (len(sys.argv) < 2):
	print "Usage"
	print "searchDuplicatedLines.py file"
	sys.exit()

# Regex List
regexList = ["^#.*",".*msgid \"\".*",".*msgstr \"\".*"]

# Local variables
linesSeen = set() 
numBlankLines = 0
numFuzzy = 0
lineNumber = 0
fileOpen = open(sys.argv[1],"r")

# Functions
def checkRegex(str):
	for regex in regexList:
		if re.match(regex,str) :
			return True
	return False

# Main
for line in fileOpen:
	lineNumber = lineNumber + 1
	if not line.strip() == '' and not line.strip() == '\n':
		if line not in linesSeen:
			linesSeen.add(line)
		else:
			if checkRegex(line) == False:
				print "Duplicated line at "+ str(lineNumber) +" : "+ line.strip()
	else:
		numBlankLines = numBlankLines + 1

# Summary
print "Summary:"
print "Fuzzy tokens " + str(numFuzzy)
print "Total lines " + str(lineNumber)
print "Total different lines " + str(len(linesSeen))
print "Blank Lines " + str(numBlankLines)

sys.exit()
