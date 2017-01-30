import unittest
from change_first import change_first

class ChangeFirstTestCase(unittest.TestCase):
    def test_change_first(self):
        self.assertEqual(change_first("restart"),"resta$t")

    def test_change_first_number(self):
        try:
            self.assertIsInstance(change_first("123"),"Enter valid input as string..")
        except Exception as e:
            print("Character is not accept Number")
            print ("Exception in Test Case : ", e)

    def test_change_first_None(self):
        try:
            self.assertIsInstance(change_first(None),"Enter valid input as string..")
        except Exception as e:
            print("Please Insert String")
            print ("Exception in Test Case : ", e)

    def test_change_first_specialsymbol(self):
    	try:
            ss=['!','@','#','$','%','^','&','*','(',')','{','}',':','[',']',';','"','\'','<',',','>','.','?','/,','-','+']
            for i in ss:
                self.assertIsInstance(change_first(i),"Enter valid input as string..")
    	except Exception as e:
            print("Please Insert String")
            print ("Exception in Test Case : ", e)

if __name__=="__main__":
	unittest.main()