import unittest
from p8 import compute_anagram

class AnagramsTestCase(unittest.TestCase):
    def test_anagram(self):
        self.assertEqual(compute_anagram("listen",["inlets","Google","letsin","listens"]),["inlets","letsin"])

    def test_anagram_firstnum(self):
        try:
            self.assertIsInstance(compute_anagram(123,["dcw",233]),"Enter valid Inputs..")
        except Exception as e:
            print("First Argument is List")
            print ("Exception in Test Case : ", e)

    def test_anagram_firstnone(self):
        try:
            self.assertIsInstance(compute_anagram(None,["dcw",233]),"Enter valid Inputs..")
        except Exception as e:
            print("First Argument is List")
            print ("Exception in Test Case : ", e)

    def test_anagram_secondnone(self):
        try:
            self.assertIsInstance(compute_anagram("abcd",None),"Please enter alternatives")
        except Exception as e:
            print("First Argument is List")
            print ("Exception in Test Case : ", e)

    def test_anagram_bothnone(self):
        try:
            self.assertIsInstance(compute_anagram(None,None),"Enter valid Inputs..")
        except Exception as e:
            print("First Argument is List")
            print ("Exception in Test Case : ", e)

if __name__=="__main__":
	unittest.main()
