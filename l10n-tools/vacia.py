#!/usr/bin/env python

import polib
import sys


def main(argv):
	# Some values to solve
	print(str(sys.argv[1]))
	po = polib.pofile(sys.argv[1])
	for entry in po:
		if entry.msgstr:
			entry.msgstr=""
	po.save()

if __name__ == "__main__":
	
	main(sys.argv[1:])
