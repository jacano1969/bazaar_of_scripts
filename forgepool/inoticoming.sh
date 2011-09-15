#!/bin/sh

# Reprepro & inoticoming dir for logs
# put this directory where you need
INOTICOMINGLOG="/var/log/reprepro/inoticoming/"
# For each Repository in 
REPREPROBASEDIRLIST="/srv/hardy /srv/lucid "

# Create directory (for if the flies)
if [ -d "$INOTICOMINGLOG" ] ; then
        echo "Directory created... nothing to do"
else
        echo "Create directory for LOG "
        mkdir -p "$INOTICOMINGLOG"
fi

for repo in $REPREPROBASEDIRLIST ; do
	# This create a inoticoming process to
	# keep this directory under our vigilance
	# and call reprepro with the "default" rule
	# especified into conf/incoming file on repositorie
	REPONAME=$(basename $repo)
	echo "inoticoming --logfile "$INOTICOMINGLOG$REPONAME-log" --pid-file "$INOTICOMINGLOG$REPONAME-pid" "$repo"/incoming --suffix .changes --stderr-to-log reprepro -s -b $repo  --waitforlock  1000 processincoming default {} \;"
	inoticoming --logfile "$INOTICOMINGLOG$REPONAME-log" --pid-file "$INOTICOMINGLOG$REPONAME-pid" "$repo"/incoming --suffix .changes --stderr-to-log reprepro -s -b $repo  --waitforlock  1000 processincoming default {} \;
done