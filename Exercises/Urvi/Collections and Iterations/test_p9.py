import unittest
from p9 import multiple

class MultiplierTestCase(unittest.TestCase):
    def test_multiple(self):
        self.assertEqual(multiple(['3','5','15','4']),[3 ,5 ,15])

    def test_multiple_char(self):
        try:
            self.assertIsInstance(multiple(["dcd","vd"]),str)
        except Exception as e:
            print("First Argument is List")
            print ("Exception in Test Case : ", e)

    def test_multiple_none(self):
        try:
            self.assertEqual(multiple(None),"Enter Valid Inputs")
        except Exception as e:
            print("First Argument is List")
            print ("Exception in Test Case : ", e)

    def test_multiple_specialsymbol(self):
        try:
            self.assertIsInstance(multiple(["$$%3"]),str)
        except Exception as e:
            print("First Argument is List")
            print ("Exception in Test Case : ", e)
if __name__=="__main__":
	unittest.main()
