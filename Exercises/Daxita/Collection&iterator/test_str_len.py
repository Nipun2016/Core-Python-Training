import unittest
from str_len import find_len

class StringLenTestCase(unittest.TestCase):
    def test_str_len(self):
        self.assertEqual(find_len(["listen","abcdd&*","Google"]),[6,7,6])

    def test_str_len_firstnum(self):
        try:
            self.assertIsInstance(find_len([2343,"abcdd&*","Google"]),"Enter valid input")
        except Exception as e:
            print("First Argument is List")
            print ("Exception in Test Case : ", e)

    def test_str_len_num(self):
        try:
            self.assertIsInstance(find_len([2343,434,3433]),"Value Error...")
        except Exception as e:
            print("First Argument is List")
            print ("Exception in Test Case : ", e)

    def test_str_len_none(self):
        try:
            self.assertIsInstance(find_len([None,"cds","sdcrf"]),"Value Error...")
        except Exception as e:
            print("First Argument is List")
            print ("Exception in Test Case : ", e)


if __name__=="__main__":
	unittest.main()