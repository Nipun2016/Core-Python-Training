import unittest
from prime import find_prime

class FindPrimeTestCase(unittest.TestCase):
    def test_find_prime(self):
        self.assertIsInstance(find_prime(7),str)

    def test_find_prime1(self):
        try:
            self.assertIsInstance(find_prime(int),str)
        except Exception as e:
            print("Argument is Number")
            print ("Exception in Test Case : ", e)
 
    def test_find_prime_char(self):
        try:
            self.assertIsInstance(find_prime(str),str)
        except Exception as e:
            print("Argument is Number")
            print ("Exception in Test Case : ", e) 

    def test_find_prime_none(self):
        try:
            self.assertIsInstance(find_prime(None),str)
        except Exception as e:
            print("Argument is Number")
            print ("Exception in Test Case : ", e)

    def test_find_prime_specialsymbol(self):
        try:
            ss=['!','@','#','$','%','^','&','*','(',')','{','}',':','[',']',';','"','\'','<',',','>','.','?','/,','-','+']
            for i in ss:
                self.assertIsInstance(find_prime(i),str)
        except Exception as e:
            print("Argument is Number")
            print ("Exception in Test Case : ", e)

if __name__=="__main__":
    unittest.main()