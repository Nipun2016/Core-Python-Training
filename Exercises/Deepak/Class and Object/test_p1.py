import unittest
from p1 import Basic

class P1TestCase(unittest.TestCase):
    def test_convert(self):
        obj = Basic()
        obj.get_String("dac")
        self.assertEqual(obj.valid_input("dac"),"dac")

    def test_covert_number(self):
        obj = Basic()
        obj.get_String("123")
        self.assertFalse(obj.valid_input(3))

    def test_covert_None(self):
        obj = Basic()
        obj.get_String("")
        self.assertFalse(obj.valid_input(""))

if __name__ == "__main__":
    unittest.main()
