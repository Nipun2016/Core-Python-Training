import unittest
from p1 import calculate, check_valid_data

class P1TestCase(unittest.TestCase):

    def test_calculate_valid_data(self):
        try:
            self.assertFalse(check_valid_data("deepak","dac","multiple"))
        except TypeError:
            print ("Please Insert Enc Character and Multiple in number.")

    def test_calculate(self):
        self.assertEqual(calculate("deepak",2,3), "dedede")

    def test_calculate_endchar(self):
        try:
            self.assertIsInstance(calculate("deepak","abc",3),str)
        except Exception as e:
            print("End Character is not Number")
            print ("Exception in Test Case : ", e)

    def test_calculate_multiply_number(self):
        try:
            self.assertIsInstance(calculate("deepak",3,"abc"),str)
        except Exception as e:
            print("Multiply is not Number")
            print ("Exception in Test Case : ", e)

    def test_calculate_multiply(self):
        try:
            self.assertIsInstance(calculate("deepak","abc","def"),str)
        except Exception as e:
            print("Multiply and End Character are not Number")
            print ("Exception in Test Case : ", e)

    def test_print_String_EndChar_None(self):
        try:
            self.assertIsInstance(calculate("deepak",None,2),str)
        except Exception as e:
            print("Please Insert Number in End Character")
            print ("Exception in Test Case : ", e)

    def test_print_String_Multiply_None(self):
        try:
            self.assertIsInstance(calculate("deepak",2,None),str)
        except Exception as e:
            print("Please Insert Number in Multiply")
            print ("Exception in Test Case : ", e)

    def test_print_String_Both_None(self):
        try:
            self.assertIsInstance(calculate("deepak",None,None),str)
        except Exception as e:
            print("Please Insert Number in End Character and Multiply")
            print ("Exception in Test Case : ", e)

if __name__ == "__main__":
    unittest.main()
