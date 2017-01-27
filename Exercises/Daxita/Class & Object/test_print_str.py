import unittest
from print_str import s

class PrintStrTestCase(unittest.TestCase):
    def test_print_str(self):
    	S=s()
    	self.assertEqual(S.print_str("Daxita"),"DAXITA")

    def test_print_str_none(self):
    	S=s()
    	self.assertEqual(S.print_str("None"),"Enter String..")

    def test_print_str_space(self):
    	S=s()
    	self.assertEqual(S.print_str(" "),"Enter String..")

if __name__=="__main__":
	unittest.main()