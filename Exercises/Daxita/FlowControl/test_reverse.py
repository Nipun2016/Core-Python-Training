import unittest
from reverse import reverse_list

class ReverseTestCase(unittest.TestCase):
    def test_reverse_list(self):
        self.assertEqual(reverse_list(3,["dax","urvi","kalgi"]),["ialgk","irvu","xad"])

    def test_reverse_list_firstchar(self):
        try:
            self.assertIsInstance(reverse_list("Dhruvi",list),list)
        except Exception as e:
            print("First Argument is Number")
            print ("Exception in Test Case : ", e)

    def test_reverse_list_secondnumber(self):
        try:
            self.assertIsInstance(reverse_list(list,3),list)
        except Exception as e:
            print("Second Arg is not Number")
            print ("Exception in Test Case : ", e)

    def test_reverse_list_firstnumber(self):
        try:
            self.assertIsInstance(reverse_list(3,list),list)
        except Exception as e:
            print("First Arg is not Number")
            print ("Exception in Test Case : ", e)

    def test_reverse_list_number(self):
        try:
            self.assertIsInstance(reverse_list(3,3),list)
        except Exception as e:
            print("Both Args are not Number")
            print ("Exception in Test Case : ", e)

    def test_reverse_list_firstlist(self):
        try:
            self.assertIsInstance(reverse_list(list,list),list)
        except Exception as e:
            print("First Argument is Number")
            print ("Exception in Test Case : ", e)

    def test_reverse_list_firstnone(self):
        try:
            self.assertIsInstance(reverse_list(None,list),list)
        except Exception as e:
            print("First Argument is Number")
            print ("Exception in Test Case : ", e) 

    def test_reverse_list_secondnone(self):
        try:
            self.assertIsInstance(reverse_list(3,None),list)
        except Exception as e:
            print("Second Argument is List")
            print ("Exception in Test Case : ", e)  

    def test_reverse_list_bothnone(self):
        try:
            self.assertIsInstance(reverse_list(None,None),list)
        except Exception as e:
            print("First Argument is Number Second Argument is List")
            print ("Exception in Test Case : ", e)  

    def test_reverse_list_secondspecialsymbol(self):
        try:
            ss=['!','@','#','$','%','^','&','*','(',')','{','}',':','[',']',';','"','\'','<',',','>','.','?','/,','-','+']
            for i in ss:
                self.assertIsInstance(reverse_list(3,i),list)
        except Exception as e:
            print("Second Argument is List")
            print ("Exception in Test Case : ", e) 

    def test_reverse_list_firstspecialsymbol(self):
        try:
            ss=['!','@','#','$','%','^','&','*','(',')','{','}',':','[',']',';','"','\'','<',',','>','.','?','/,','-','+']
            for i in ss:
                self.assertIsInstance(reverse_list(i,list),list)
        except Exception as e:
            print("First Argument is Number")
            print ("Exception in Test Case : ", e)

    def test_reverse_list_bothspecialsymbol(self):
        try:
            ss=['!','@','#','$','%','^','&','*','(',')','{','}',':','[',']',';','"','\'','<',',','>','.','?','/,','-','+']
            for i in ss:
                self.assertIsInstance(reverse_list(i,i),list)
        except Exception as e:
            print("First Argument is Number Second Argument is List")
            print ("Exception in Test Case : ", e)   
if __name__=='__main__':
    unittest.main()