#!/bin/sh

# Some values
# Reprepro & inoticoming dir for logs
# put this directory where you need
INOTICOMINGLOG="/var/log/reprepro/inoticoming/"
# For each Repository in 
REPREPROBASEDIRLIST="/srv/hardy /srv/lucid "

_testDirectories(){
    # Create directory (for if the flies)
    if [ -d "$INOTICOMINGLOG" ] ; then
        echo "llx-pools-inoticoming : Directory created... nothing to do"  
    else
        echo "Create directory for LOG "
        mkdir -p "$INOTICOMINGLOG"
    fi
}

_updateRepositories(){
	# This create a inoticoming process to
	# keep this directory under our vigilance
	# and call reprepro with the "default" rule
	# especified into conf/incoming file on repositories
	for repo in $REPREPROBASEDIRLIST ; do
		REPONAME=$(basename $repo)
		inoticoming --logfile "$INOTICOMINGLOG$REPONAME-log" --pid-file "$INOTICOMINGLOG$REPONAME-pid" "$repo"/incoming --suffix .changes --stderr-to-log reprepro -s -b $repo  --waitforlock  1000 processincoming default {} \;
	done
}

# Main
_testDirectories
_updateRepositories

exit 0
