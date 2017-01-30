import unittest
from tuple_dict import tup_dic

class TupleDictTestCase(unittest.TestCase):
    def test_tuple_dict(self):
        self.assertEqual(tup_dic(((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'))),{1: 'a', 2: 'b', 3: 'c', 4: 'd'}	)
	
    def test_tuple_dict_none(self):
        try:
            self.assertIsInstance(tup_dic(()),"Value Error")
        except Exception as e:
            print("First Argument is tuple")
            print ("Exception in Test Case : ", e)
if __name__=="__main__":
	unittest.main()