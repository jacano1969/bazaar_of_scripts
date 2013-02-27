#!/usr/bin/env python
#
# This script is licensed under GPL v3
# or higher.
#
# Author: Angel Berlanas Vicente 
# 	  <angel.berlanas@gmail.com>
#
# -*- coding: utf8 -*-

import sys
import potools


if len(sys.argv) > 3:
  potools.debug_msg("Starting")
  compendium_path = sys.argv[1]
  orig_path = sys.argv[2]
  dest_path = sys.argv[3]
  potools.debug_msg("Tenemos los argumentos")

else:
  print("[USAGE]")
  print("File1.po File2.po File_dest.po")
  sys.exit(0)

potools.debug_msg("Make destination PO")
potools.simple_po_creation(dest_path)
potools.debug_msg("Merge the pos")
potools.union_po(compendium_path,orig_path, dest_path)
potools.debug_msg("Checking duplicates")
potools.test_duplicates(dest_path)
