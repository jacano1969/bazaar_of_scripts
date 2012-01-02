#!/bin/sh

#mencoder -idx $1 -ovc lavc -oac lavc -lavcopts vcodec=mpeg2video -of mpeg -o $1.mpg

mencoder $1 -ovc xvid -oac mp3lame -xvidencopts pass=1 -o $1.avi
exit 0