#!/bin/sh
# Author: Angel Berlanas Vicente
# This script is licensed under GPL v3 or higher

# Some temporal values
TRANSFIGURATION_DIRECTORY="$(mktemp -d /tmp/pdfbooklet.XXXXX)"
FINAL_PDF="book_output.pdf"

_usage()
{
	echo "pdfbooklet.sh --book FILE_TO_PARSE"
	echo "pdfbooklet.sh --target FINAL_PDF.pdf --png FILE1.png FILE2.png .."
	exit 1
}

_clean_booklet()
{
	echo "Cleaning area"
	rm "$FILE_TO_PARSE.ps"
	rm "$FILE_TO_PARSE.A5.ps"
}

_booklet()
{	
	FILE_TO_PARSE="$1"
	pdftops "$FILE_TO_PARSE" "$FILE_TO_PARSE.ps"
	psbook "$FILE_TO_PARSE.ps" | psnup -pa4 -l -2 > "$FILE_TO_PARSE.A5.ps"
	ps2pdf "$FILE_TO_PARSE.A5.ps" "$FILE_TO_PARSE.A5.pdf"
}

_process_single_image()
{
	echo "Processing $1"
	convert $2 $TRANSFIGURATION_DIRECTORY/$1.$(basename "$2").ps
}

_process_images()
{
	echo "Processing files"	
	TOTAL_NUMBER="$#"
	CURRENT=0
	for f in $@ ; do
		CURRENT=$(($CURRENT+1))
		_process_single_image "$CURRENT.of.$TOTAL_NUMBER" "$f"
	done	
}

_process_directory()
{
	echo "Process transfiguration directory"
	gs -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=$FINAL_PDF "$TRANSFIGURATION_DIRECTORY"/*.ps
}

_clean_process()
{
	echo "Cleaning working area $TRANSFIGURATION_DIRECTORY"
	rm -rf $TRANSFIGURATION_DIRECTORY
}

if [ $#  -eq 0 ]; then 
	_usage
fi

case "$1" in
	--book)
	shift
	_booklet "$1"
	_clean_booklet
	;;
	--target)
	shift
	FINAL_PDF="$1"
	shift
	shift
	_process_images $@
	_process_directory
	_clean_process
	;;
	*)
	_usage
	;;
esac

# Main 
exit 0
