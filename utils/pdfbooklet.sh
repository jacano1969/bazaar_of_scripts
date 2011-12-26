#!/bin/sh
# Author: Angel Berlanas Vicente
# This script is licensed under GPL v3 or higher

function _usage()
{
	echo "pdfbooklet.sh FILE_TO_PARSE"
	exit 1
}

function _clean()
{
	echo "Cleaning area"
	rm "$FILE_TO_PARSE.ps"
	rm "$FILE_TO_PARSE.A5.ps"
}

function _booklet()
{	
	FILE_TO_PARSE="$1"
	pdftops "$FILE_TO_PARSE" "$FILE_TO_PARSE.ps"
	psbook "$FILE_TO_PARSE.ps" | psnup -pa4 -l -2 > "$FILE_TO_PARSE.A5.ps"
	ps2pdf "$FILE_TO_PARSE.A5.ps" "$FILE_TO_PARSE.A5.pdf"
}

if [  -eq 0 ]; then 
	_usage
fi

# Main 
_clean
_booklet "$1"

exit 0
