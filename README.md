python-potools
==============

python-potools

Functions
=========
**append_compendium**(compendium, appendfile, outputfile)
    Returns a outputfile as a union po

**compare_langpack**(inputdir, otherdir)
    Returns a differences between two directories

create_compendium(compendiumdir, outputfile)
    Returns a outputfile as a compendium po

debug_msg(msg)
    Print debug messages with fancy colours

empty_po(inputfile)
    empty_po empty all entries at inputfile

error_msg(msg)
    Print error messages with fancy colours

info_msg(msg)
    Print info messages with fancy colours

lowerator(inputfile, outputfile)
    Returns a outputfile with all msgid and msgstr with lowercase

search_duplicates(duplicatedfiles, pooutput=False, logoutput=False)

set_metadata_pilarized(pofile)
    Set the metada at custom Translator

simple_po_creation(outputfile)
    Function create a empty po, with a example `metadata`
    :param outputfile: Path to new po.

test_duplicates(inputfile)
    return the duplicates entries at a given po

test_metadata(pofile)
    Return the metadata and Last-Translator field

union_po(inputfile1, inputfile2, outputfile)
    Returns a po at outputfile that is the union of two arguments inputfile1 & 2
    inputfile1 -- Path to new po
    inputfile2 -- Path to new po
    outputfile -- Path to new po
