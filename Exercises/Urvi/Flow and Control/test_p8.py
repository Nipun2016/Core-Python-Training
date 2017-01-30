import unittest
from p8 import prime_number

class P8TestCase(unittest.TestCase):
    def test_prime_number(self):
        self.assertEqual(prime_number(5),"5 is a prime number")

    def test_check_player_string(self):
        try:
            self.assertTrue(prime_number("urvi"))
        except Exception as e:
            print("Please Insert Any Data in Number")
            print ("Exception in Test Case : ", e)

    def test_check_player_none(self):
        try:
            self.assertTrue(prime_number(None))
        except Exception as e:
            print("Please Insert Any Data")
            print ("Exception in Test Case : ", e)

if __name__ == "__main__":
    unittest.main()
