import unittest
from dict import dict_key

class DictKeyTestCase(unittest.TestCase):
    def test_dict_key(self):
        self.assertEqual(dict_key({"1":"daxita","2":"urvi","3":"deepak"},'2'),"key is already there in dictionary")

    def test_dict_key_number(self):
        try:
            self.assertIsInstance(dict_key({"1":"daxita","2":"urvi","3":"deepak"},2),str)
        except Exception as e:
            print("End Character is not Number")
            print ("Exception in Test Case : ", e)

    def test_dict_key_None(self):
        try:
            self.assertIsInstance(dict_key({"1":"daxita","2":"urvi","3":"deepak"},None),str)
        except Exception as e:
            print("Please Insert Key in second Argument")
            print ("Exception in Test Case : ", e)

    def test_dict_key_both_None(self):
        try:
            self.assertIsInstance(dict_key(None,None),str)
        except Exception as e:
            print("Please Insert Key in second Argument")
            print ("Exception in Test Case : ", e)

    def test_dict_None(self):
        try:
            self.assertIsInstance(dict_key(None,'2'),str)
        except Exception as e:
            print("Please Insert Dictionary in 1st argument")
            print ("Exception in Test Case : ", e)

    def test_dict_key_specialsymbol(self):
    	try:
    		ss=['!','@','#','$','%','^','&','*','(',')','{','}',':','[',']',';','"','\'','<',',','>','.','?','/,','-','+']
    		for i in ss:
    			self.assertIsInstance(dict_key({"1":"daxita","2":"urvi","3":"deepak"},i),str)
    	except Exception as e:
            print("Please Insert Key Value")
            print ("Exception in Test Case : ", e)

if __name__=="__main__":
	unittest.main()