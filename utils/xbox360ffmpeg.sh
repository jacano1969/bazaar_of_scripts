#!/bin/bash
for file in $@ ; do
	echo " Processing $file"
	ffmpeg -i "$file" -sameq -ac 2 -aspect 16:9 "$file".mp4
	echo " ****************"
done
