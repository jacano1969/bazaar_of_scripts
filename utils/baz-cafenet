#!/bin/sh

SVN_DIRECTORY="$1"

for f in $(ls -1 "$SVN_DIRECTORY"); do
	echo "Processing $f"
	svn up $f
done

exit 0
