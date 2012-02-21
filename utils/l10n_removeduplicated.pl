#!/usr/bin/perl -w 

use strict;
use File::Find;
use Locale::PO;

my @files = ();
my $filepo ;
my $dir = shift || die "Algun directorio es necesario dar\n";
my $po;
my $msgid;
my $msgstr ; 

sub myFunction()
{
	print $File::Find::name . "\n";
	my $potRef=Locale::PO->load_file_asarray("/svn/polin/llx1009/llx-l10n/firefox-10/".$File::Find::name);
	
	foreach my $x (@$potRef) {
		$msgid = $x->msgid;
		$msgstr = $x->msgstr;
		if (defined $msgid and defined $msgstr) {
			if ( $msgstr eq $msgid){
					print "Las cadenas son iguales\n";
					print " ".$msgid."\n==============\n".$msgstr."\n* AHORA OPERAMOS *\n";
					$x->msgstr("");
					$x->fuzzy(1);
					$msgstr = $x->msgstr;
					print " ".$msgid."\n==============\n".$msgstr."\n********\n";
			}
		}
	}
	
	 Locale::PO->save_file_fromarray("/svn/polin/llx1009/llx-l10n/firefox-10/".$File::Find::name,$potRef);
} 

sub loadFiles()
{
	  my @array={"$dir"};
      find(\&myFunction,$dir); 
}

loadFiles();






