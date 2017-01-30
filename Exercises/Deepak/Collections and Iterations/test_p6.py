import unittest
from unzip import tuple_con_list

class UnzipTestCase(unittest.TestCase):
    def test_unzip(self):
        self.assertEqual(tuple_con_list((1,2,4,56554),('a','frv','dsfawd'),('s3de',2,'sadas')),[(1, 2, 4, 56554), ('a', 'frv', 'dsfawd'), ('s3de', 2, 'sadas')])
	
    def test_unzip_none(self):
        try:
            self.assertIsInstance(tuple_con_list(),"Value Error")
        except Exception as e:
            print("First Argument is tuple")
            print ("Exception in Test Case : ", e)
if __name__=="__main__":
	unittest.main()