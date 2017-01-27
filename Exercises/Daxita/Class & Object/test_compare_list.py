import unittest
from compare_list import fun

class CompareListTestCase(unittest.TestCase):
    def test_fun(self):
        self.assertEqual(fun(["dax","krupa","kalgi","urvi"],["dhruvi","deepak","kalgi"]),True)

    def test_fun1(self):
        self.assertEqual(fun(["dax","krupa","kalgi","urvi"],["dhruvi","deepak","mona"]),False)

    def test_fun_firstnum(self):
        try:
            self.assertIsInstance(fun([1],["dfdf"]),False)
        except Exception as e:
            print("First Argument is List")
            print ("Exception in Test Case : ", e)

    def test_fun_bothnum(self):
        try:
            self.assertIsInstance(fun([1],[2]),False)
        except Exception as e:
            print("Both Argumenta are Lists")
            print ("Exception in Test Case : ", e)

    def test_fun_bothchar(self):
        try:
            self.assertIsInstance(fun(["abc"],["jhdb"]),False)
        except Exception as e:
            print("Both Argumenta are Lists")
            print ("Exception in Test Case : ", e)

    def test_fun_firstnone(self):
        try:
            self.assertIsInstance(fun(None,list),False)
        except Exception as e:
            print("First Argument is List")
            print ("Exception in Test Case : ", e)

    def test_fun_firstspecialsymbol(self):
        try:
            ss=['!','@','#','$','%','^','&','*','(',')','{','}',':','[',']',';','"','\'','<',',','>','.','?','/,','-','+']
            for i in ss:
                self.assertIsInstance(calculate([i],["dfvd",1]),False)
        except Exception as e:
            print("First Argument is List")
            print ("Exception in Test Case : ", e)

    def test_fun_secondspecialsymbol(self):
        try:
            ss=['!','@','#','$','%','^','&','*','(',')','{','}',':','[',']',';','"','\'','<',',','>','.','?','/,','-','+']
            for i in ss:
                self.assertIsInstance(calculate([1,"es"],[i]),False)
        except Exception as e:
            print("Second Argument is List")
            print ("Exception in Test Case : ", e)

    
if __name__=="__main__":
	unittest.main()