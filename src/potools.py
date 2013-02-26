#!/usr/bin/env python

import polib
import sys
import getopt
import glob
import os
import string


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
	return Bcolors.HEADER + "[" + Bcolors.ENDC + Bcolors.OKBLUE +"DEBUG" + Bcolors.HEADER + "] " + Bcolors.ENDC + str(msg)

def error_msg(msg):
	"""
	Print error messages with fancy colours
	"""
	return Bcolors.FAIL + "[" + Bcolors.ENDC + Bcolors.WARNING +"ERROR" + Bcolors.FAIL + "] " + Bcolors.ENDC + str(msg)

def info_msg(msg):
	"""
	Print info messages with fancy colours
	"""
	return Bcolors.HEADER + "[" + Bcolors.ENDC + Bcolors.HEADER +"INFO" + Bcolors.HEADER + "] " + Bcolors.ENDC + str(msg)

	
def simple_po_creation(outputfile):
	"""Function create a empty po, with a example `metadata`
	:param outputfile: Path to new po.
	"""
	
	try :
		if os.path.exists(outputfile):
			set_metadata_pilarized(outputfile)
		else:
			open(outputfile, 'w').close()
			po = polib.pofile(outputfile)
			set_metadata_pilarized(outputfile)
			po.save(outputfile)
		return True
	except Exception as e:
		print ( error_msg(str(e)) )
		return False
#def simple_po_creation(outputfile):

def union_po(inputfile1,inputfile2,outputfile):
	"""Returns a po at outputfile that is the union of two arguments inputfile1 & 2
	inputfile1 -- Path to new po
	inputfile2 -- Path to new po
	outputfile -- Path to new po
	"""
	
	# If po not exists, first create it!
	try: 
		if (os.paht.exists(outputfile)):
			set_metadata_pilarized(outputfile)
		else:
			simple_po_creation(outputfile)
	except Exception as e:
		print (error_msg(str(e)))
		return False

	# Doing the Magic
	po1 = polib.pofile(inputfile1)
	po2 = polib.pofile(inputfile2)
	dest = polib.pofile(outputfile)
	dic_compendium = {}

	for entry in po1:
		dest.append(entry)
	dest.save(outputfile)

	for entry in po2:
		dest.append(entry)
	dest.save(outputfile)

	# All is done
	return True

#def union_po(inputfile1,inputfile2,outputfile):

def lowerator(inputfile,outputfile):
	"""Returns a outputfile with all msgid and msgstr with lowercase"""
	
	# Doing the Magic
	try :
		if (os.path.exists(outputfile)):
			set_metadata_pilarized(outputfile)
		else:
			simple_po_creation(outputfile)
	except Exception as e:
		print (error_msg(str(e)))
		return False
	
	try:
	
		po_dest = polib.pofile(outputfile)
		po_orig = polib.pofile(inputfile)

		for entry in po_orig:
			aux = polib.POEntry()
			aux.msgid = string.lower(entry.msgid)
			aux.msgstr = string.lower(entry.msgstr)
			po_dest.append(aux)

		po_dest.save(outputfile)

	
		# All is done
		return True
	except Exception as e:
		print (error_msg(str(e)))
#def lowerator(inputfile,outputfile):


def empty_po(inputfile):
	"""empty_po empty all entries at inputfile """
	po = polib.pofile(inputfile)
	for entry in po:
		if entry.msgstr :
			entry.msgstr = ""
		try:
			if entry.msgstr[0] :
				entry.msgstr[0] = ""
			if entry.msgstr[1] :
				entry.msgstr[1] = ""
		except Exception as e:
			pass
#def empty_po

def test_duplicates(inputfile):
	"""return the duplicates entries at a given po"""
	po = polib.pofile(inputfile)
	tmp_list=set()
	
	for entry in po:
		tmp_list.add(entry.msgid)
		
	if len(po) > len(tmp_list):
		for index in range(len(po)-1,-1,-1):
			entry=po[index]
			po.pop(index)
			for entry2 in po:
				if entry.msgid==entry2.msgid:
					print (info_msg("[!] "+ entry.msgid + " is duplicated [!] "))
					break
					
	else:
		debug_msg("No duplicates found")

#def test_duplicates(inputfile)

def test_metadata(pofile):
	"""Return the metadata and Last-Translator field"""
	print (info_msg("Working with " + pofile))
	po = polib.pofile(pofile)
	if ( po.metadata["Last-Translator"]):
		print (info_msg("Last-Translator is " + po.metadata["Last-Translator"]))
	else :
		print (info_msg("No metadata in po present"))

#def test_metadata(pofile):

def set_metadata_pilarized(pofile):
	"""Set the metada at custom Translator"""
	po = polib.POFile(pofile)
	po.metadata = {
		'Project-Id-Version': '1.0',
		'Report-Msgid-Bugs-To': 'lliurex@lliurex.net',
		'POT-Creation-Date': '2012-12-21 00:00+0100',
		'PO-Revision-Date': '2012-12-21 00:00+0100',
		'Last-Translator': 'Pilar Embid Giner <embid_mar@gva.es>',
		'Language-Team': 'LliureX',
		'MIME-Version': '1.0',
		'Content-Type': 'text/plain; charset=utf-8',
		'Content-Transfer-Encoding': '8bit',
		'Plural-Forms':'nplurals=2; plural=(n != 1);',
	}
	po.save(pofile)

#def set_metadata_pilarized(pofile):

def append_compendium(compendium,appendfile,outputfile):
	"""Returns a outputfile as a union po"""
	print(debug_msg(" Compendium : "+str(compendium) + "... Appendfile : " + str(appendfile)+ "... Outputfile : "+str(outputfile)))
	# For files in directory create a compendium
	set_metadata_pilarized(outputfile)
	compendiumpo = polib.pofile(outputfile)
	appendpo = polib.pofile(appendfile)
	previouscompendium = polib.pofile(compendium)
	compendiumpo_set=set([])
	print(debug_msg("Angel"))
	try:
		

		print(info_msg(" Compendium is " +str(compendium) +" ..."))
		valid_entries = [e for e in previouscompendium if not e.obsolete and not "fuzzy" in e.flags]
		for entry in valid_entries:
			old_size=len(compendiumpo_set)
			compendiumpo_set.add(entry.msgid)
			if len(compendiumpo_set)>old_size:
				compendiumpo.append(entry)

		print(info_msg("Reading " + str(appendfile) + " ..."))
		valid_entries = [e for e in appendpo if not e.obsolete and not "fuzzy" in e.flags]
		for entry in valid_entries:
			old_size=len(compendiumpo_set)
			compendiumpo_set.add(entry.msgid)
			if len(compendiumpo_set)>old_size:
				compendiumpo.append(entry)

	except Exception as e:
		print(error_msg(str(e)))

	compendiumpo.save()
	info_msg("Result is now : "+str(outputfile))

#def create_compedium(compendiumdir, outputfile)

def create_compendium(compendiumdir, outputfile):
	"""Returns a outputfile as a compendium po"""
	# For files in directory create a compendium
	set_metadata_pilarized(outputfile)
	compendiumpo = polib.pofile(outputfile)
	# 
	compendiumdir+="/"
	listofpos = glob.glob(compendiumdir+"*.po")	
	set_metadata_pilarized(outputfile)
	compendiumpo = polib.pofile(outputfile)
	compendiumpo_set=set([])

	for f in listofpos:
		try:
			print(info_msg(str(f) + " ..."))
			po=polib.pofile(f)
			valid_entries = [e for e in po if not e.obsolete and not "fuzzy" in e.flags]
			for entry in valid_entries:
				old_size=len(compendiumpo_set)
				compendiumpo_set.add(entry.msgid)
				if len(compendiumpo_set)>old_size:
					compendiumpo.append(entry)

		except Exception as e:
			print(error_msg(str(e)))

	compendiumpo.save()

#def create_compedium(compendiumdir, outputfile)
	

def search_duplicates(duplicatedfiles,pooutput=False,logoutput=False):
	
	print (info_msg("Working with :"+ str(duplicatedfiles)))
	setofsets = set([])
	empty=True
	for file in duplicatedfiles:
		po=polib.pofile(file)
		auxset=set([])
		valid_entries = [e for e in po if not e.obsolete]
		for entry in valid_entries:
			auxset.add(entry.msgid)
		if  empty :
			setofsets = auxset
			empty=False
		else:
			setofsets = setofsets.intersection(auxset)
	
			
	# If logoutput is active	the output is as Syslog 
	if (logoutput):
		for msgid in setofsets:
			print (info_msg(msgid))
	
	
	# If pooutput flag is active the output of the duplicated search
	# is in po format (redirection is posible).
	if (pooutput != "" ):
		
		# Open the firs as a example traduction
		poex = polib.pofile(duplicatedfiles[0])
		
		set_metadata_pilarized(pooutput)
		pofinal = polib.pofile(pooutput)

		for msgid in setofsets:
			for entry in poex:
				if msgid == entry.msgid:
					pofinal.append(entry)
		
		pofinal.save(pooutput)
		print (info_msg("All is done : "+pooutput))
#def search_duplicates(duplicatedfiles,pooutput=False,logoutput=False)


def compare_langpack(inputdir,otherdir):
	"""Returns a differences between two directories"""
	gorig=glob.glob(inputdir+"*.po")
	gother=glob.glob(otherdir+"*.po")
	
	dic_orig={}
	dic_dest={}

	for f in gorig:
		dic_orig[os.path.basename(f)]=f
	
	for f in gother:
		dic_dest[os.path.basename(f)]=f
	
	
	print (debug_msg("--- ALL STATISTICS --"))
	print (debug_msg("--- COMMON --"))
	
	for item in set(dic_dest).intersection(dic_orig):
		try :
			poorig_len = len(polib.pofile(dic_orig[item]))
			podest_len =  len(polib.pofile(dic_dest[item]))
			print (debug_msg("[" + item+ "] [QCV] "+ str(poorig_len) + " [DEST] "+ str(podest_len)))
		except IOError as e:
			print (error_msg(item))
			pass
