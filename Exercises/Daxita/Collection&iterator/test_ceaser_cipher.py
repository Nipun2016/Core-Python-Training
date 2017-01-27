import unittest
from ceaser_cipher import ceaser_cipher

class CeaserTestCase(unittest.TestCase):
    def test_cipher(self):
        self.assertEqual(ceaser_cipher("hello kjb"),('Encrypted Text is:', 'u r y y b  x w o'))
if __name__=="__main__":
	unittest.main()