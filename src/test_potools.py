import unittest
import potools
import os
import shutil
import polib

class TestPotools(unittest.TestCase):

	def test_create_po(self):
		temporalfile="/tmp/potools_tmp_file.po"
		potools.simple_po_creation(temporalfile)
		self.assertTrue(os.path.exists(temporalfile))
		os.remove(temporalfile)

	def test_is_a_po(self):
		temporalfile="/tmp/potools_tmp_file.po"
		potools.simple_po_creation(temporalfile)
		try:
			po = polib.pofile(temporalfile)
			if len(po)>= 1:
				return True
			else:
				return False
		except Exception as e:
			print ("[ERROR] : " +str(e) )
			return False
		

if __name__ == '__main__':
	unittest.main()

