Python Library Documentation: module potools

# __NAME__

potools

# __CLASSES__

builtins.object
    Bcolors

#### Bcolors
__Bcolors__ = 
	\<class 'potools.Bcolors'\>

# __FUNCTIONS__

#### def __append\_compendium__(compendium, appendfile, outputfile):

Returns a outputfile as a union po

#### def __compare\_langpack__(inputdir, otherdir):

Returns a differences between two directories

#### def __create_compendium__(compendiumdir, outputfile):

Returns a outputfile as a compendium po

#### def __debug_msg__(msg):

Print debug messages with fancy colours

#### def __empty\_po__(inputfile):

empty_po empty all entries at inputfile

#### def __error_msg__(msg):

Print error messages with fancy colours

#### def __info_msg__(msg):

Print info messages with fancy colours

#### def __lowerator__(inputfile, outputfile):

Returns a outputfile with all msgid and msgstr with lowercase

#### def __search_duplicates__(duplicatedfiles, pooutput=False, logoutput=False):


#### def __set_metadata_pilarized__(pofile):

Set the metada at custom Translator

#### def __simple_po_creation__(outputfile):

Function create a empty po, with a example `metadata`
:param outputfile: Path to new po.

#### def __test_duplicates__(inputfile):

return the duplicates entries at a given po

#### def __test_metadata__(pofile):

Return the metadata and Last-Translator field

#### def __union\_po__(inputfile1, inputfile2, outputfile):

Returns a po at outputfile that is the union of two arguments inputfile1 & 2
	inputfile1 -- Path to new po
	inputfile2 -- Path to new po
	outputfile -- Path to new po

