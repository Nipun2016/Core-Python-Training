import unittest
from random_list import random_common

class RandomcommonTestCase(unittest.TestCase):
    def test_random_common(self):
        self.assertIsInstance(random_common(4,5),list)

    def test_random_common_firstchar(self):
        try:
            self.assertIsInstance(random_common("abcd",2),list)
        except Exception as e:
            print("First Argument is Number")
            print ("Exception in Test Case : ", e)


    def test_random_common_secondchar(self):
        try:
            self.assertIsInstance(random_common(5,"abcd"),list)
        except Exception as e:
            print("Second Argument is Number")
            print ("Exception in Test Case : ", e)

    def test_random_common_bothchar(self):
        try:
            self.assertIsInstance(random_common("dfv","abcd"),list)
        except Exception as e:
            print("Both Arguments are Number")
            print ("Exception in Test Case : ", e)

    def test_random_common_secondnone(self):
        try:
            self.assertIsInstance(random_common(5,None),list)
        except Exception as e:
            print("Second Argument is Number")
            print ("Exception in Test Case : ", e)

    def test_random_common_firstnone(self):
        try:
            self.assertIsInstance(random_common(2,None),list)
        except Exception as e:
            print("First Argument is Number")
            print ("Exception in Test Case : ", e)

    def test_random_common_bothnone(self):
        try:
            self.assertIsInstance(random_common(None,None),list)
        except Exception as e:
            print("Both Arguments are Number")
            print ("Exception in Test Case : ", e)

    def test_random_common_secondspecialsymbol(self):
        try:
            ss=['!','@','#','$','%','^','&','*','(',')','{','}',':','[',']',';','"','\'','<',',','>','.','?','/,','-','+']
            for i in ss:
                self.assertIsInstance(random_common(3,i),list)
        except Exception as e:
            print("Second Argument is Number")
            print ("Exception in Test Case : ", e)

    def test_random_common_firstspecialsymbol(self):
        try:
            ss=['!','@','#','$','%','^','&','*','(',')','{','}',':','[',']',';','"','\'','<',',','>','.','?','/,','-','+']
            for i in ss:
                self.assertIsInstance(random_common(i,3),list)
        except Exception as e:
            print("First Argument is Number")
            print ("Exception in Test Case : ", e) 

    def test_random_common_bothspecialsymbol(self):
        try:
            ss=['!','@','#','$','%','^','&','*','(',')','{','}',':','[',']',';','"','\'','<',',','>','.','?','/,','-','+']
            for i in ss:
                self.assertIsInstance(random_common(i,i),list)
        except Exception as e:
            print("First Arguments are Number")
            print ("Exception in Test Case : ", e) 
if __name__=="__main__":
	unittest.main()