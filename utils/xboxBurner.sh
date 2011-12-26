#!/bin/sh

_usage()
{
	echo "xboxBurner.sh ISO"
	exit 1
}

if [ $# -eq 0 ] ; then
	_usage
fi

echo "First Truncate the file"
truncate --size=8547991552 $1 
echo "Burning on /dev/sr0"
growisofs -use-the-force-luke=dao -use-the-force-luke=break:2086912 -dvd-compat -speed=2 -Z /dev/sr0=$1
exit 0
