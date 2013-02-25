#!/usr/bin/env python

import polib
import sys
import getopt
import potools


class Bcolors:
	"""
	Class bcolors to solve the Colour in terminal
	"""
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

	def disable(self):
		self.HEADER = ''
		self.OKBLUE = ''
		self.OKGREEN = ''
		self.WARNING = ''
		self.FAIL = ''
		self.ENDC = ''
	#def disable


def debug_msg(msg):
	"""
	Print debug messages with fancy colours
	"""
	return Bcolors.FAIL + "[" + Bcolors.ENDC + Bcolors.OKBLUE +"DEBUG" + Bcolors.FAIL + "]" + Bcolors.ENDC + str(msg)


def usage():
	"""
	Show usage with fancy colours
	"""
	print(Bcolors.HEADER+"[ USAGE ]"+ Bcolors.ENDC)
	print(Bcolors.HEADER+"         -i translate"+ Bcolors.ENDC)
	print(Bcolors.HEADER+"         -a append"+ Bcolors.ENDC)


def translate_po(compendium,po):
	"""
	Simple translate tool
	"""
	compendium = polib.pofile(compendium)
	traducir = polib.pofile(po)
	temp_compendium=compendium
	temp_compendium.merge(traducir)
	potools.simple_po_creation("final.po")
	potools.set_metadata_pilarized("final.po")
	final_po=polib.pofile("final.po")
	for entry in temp_compendium:
		if not entry.obsolete:
			final_po.append(entry)
	final_po.save("final.po")

def update_po_with_other_po(po):
	"""
	Add the messages on po to the compendium
	"""
	potools.append_compendium("poto.po",po,"aux_poto.po")
	potools.test_duplicates("aux_poto.po")

	print(debug_msg(" En aux_poto.po tienes la suma "))

def main(argv):
	# Some values to solve
	inputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:a:",["ifile=","afile="])
		if len(opts) == 0 :
			print(debug_msg(" Ni idea tienes ..."))
			print(debug_msg(" traduce.py -i TRANSLATE ..."))
			print(debug_msg(" traduce.py -a APPEND TO poto.po ..."))
		for opt, arg in opts:
			if opt == '-h':
				usage()
			elif opt in ("-i", "--ifile"):
				inputfile = arg
				print (debug_msg(Bcolors.OKGREEN+ " Working with: "+  Bcolors.ENDC + inputfile ))
				translate_po("poto.po",inputfile)
			elif opt in ("-a","--append"):
				inputfile = arg
				print (debug_msg(Bcolors.OKGREEN+ " Working with: "+  Bcolors.ENDC + inputfile ))
				update_po_with_other_po(inputfile)
	except getopt.GetoptError:
		sys.exit(2)


if __name__ == "__main__":
	
	main(sys.argv[1:])
