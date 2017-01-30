import unittest
from p1 import nameformation, check_valid_data

class P1TestCase(unittest.TestCase):

    def test_calculate_valid_data(self):
        try:
            self.assertFalse(check_valid_data("urvi","endchar","multiple"))
        except TypeError:
            print ("Please Insert Enc Character and Multiple in number.")

    def test_nameformation(self):
        self.assertEqual(nameformation("urvi",2,3), "ururur")

    def test_nameformation_endchar(self):
        try:
            self.assertIsInstance(nameformation("urvi","abc",3),str)
        except Exception as e:
            print("End Character is not Number")
            print ("Exception in Test Case : ", e)

    def test_nameformation_multiply_number(self):
        try:
            self.assertIsInstance(nameformation("urvi",3,"abc"),str)
        except Exception as e:
            print("Multiply is not Number")
            print ("Exception in Test Case : ", e)

    def test_nameformation_both(self):
        try:
            self.assertIsInstance(nameformation("urvi","abc","def"),str)
        except Exception as e:
            print("Multiply and End Character are not Number")
            print ("Exception in Test Case : ", e)

    def test_print_String_EndChar_None(self):
        try:
            self.assertIsInstance(nameformation("urvi",None,2),str)
        except Exception as e:
            print("Please Insert Number in End Character")
            print ("Exception in Test Case : ", e)

    def test_print_String_Multiply_None(self):
        try:
            self.assertIsInstance(nameformation("urvi",2,None),str)
        except Exception as e:
            print("Please Insert Number in Multiply")
            print ("Exception in Test Case : ", e)

    def test_print_String_Both_None(self):
        try:
            self.assertIsInstance(nameformation("urvi",None,None),str)
        except Exception as e:
            print("Please Insert Number in End Character and Multiply")
            print ("Exception in Test Case : ", e)

if __name__ == "__main__":
    unittest.main()
