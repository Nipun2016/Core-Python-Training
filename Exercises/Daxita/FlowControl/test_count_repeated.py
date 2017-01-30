import unittest
from count_repeated import calculate

class CountRepeatedTestCase(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(calculate("Dhruvi",2,3),"DhDhDh")

    def test_calculate_endchar(self):
        try:
            self.assertIsInstance(calculate("Dhruvi","abc",3),"Enter only Integer")
        except Exception as e:
            print("End Character is not Number")
            print ("Exception in Test Case : ", e)

    def test_calculate_multiply_number(self):
        try:
            self.assertIsInstance(calculate("Dhruvi",3,"abc"),"Enter only Integer")
        except Exception as e:
            print("Multiply is not Number")
            print ("Exception in Test Case : ", e)

    def test_calculate_multiply(self):
        try:
            self.assertIsInstance(calculate("Dhruvi","abc","def"),"Enter only Integer")
        except Exception as e:
            print("Multiply and End Character are not Number")
            print ("Exception in Test Case : ", e)

    def test_print_String_EndChar_None(self):
        try:
            self.assertIsInstance(calculate("Dhruvi",None,2),"Enter only Integer")
        except Exception as e:
            print("Please Insert Number in End Character")
            print ("Exception in Test Case : ", e)

    def test_print_String_Multiply_None(self):
        try:
            self.assertIsInstance(calculate("Dhruvi",2,None),"Enter only Integer")
        except Exception as e:
            print("Please Insert Number in Multiply")
            print ("Exception in Test Case : ", e)

    def test_print_String_Both_None(self):
        try:
            self.assertIsInstance(calculate("Dhruvi",None,None),"Enter only Integer")
        except Exception as e:
            print("Please Insert Number in End Character and Multiply")
            print ("Exception in Test Case : ", e)

    def test_print_String_Both_None1(self):
        try:
            self.assertIsInstance(calculate(None,None,None),"Enter only string")
        except Exception as e:
            print("Please Insert String in First Arg and in 2nd 3rd int")
            print ("Exception in Test Case : ", e)

    def test_print_String_secondspecialsymbol(self):
        try:
            ss=['!','@','#','$','%','^','&','*','(',')','{','}',':','[',']',';','"','\'','<',',','>','.','?','/,','-','+']
            for i in ss:
                self.assertIsInstance(calculate("Dhruvi",i,3),"Enter only Integer")
        except Exception as e:
            print("Second Argument is Number")
            print ("Exception in Test Case : ", e) 

    def test_print_String_firstspecialsymbol(self):
        try:
            ss=['!','@','#','$','%','^','&','*','(',')','{','}',':','[',']',';','"','\'','<',',','>','.','?','/,','-','+']
            for i in ss:
                self.assertIsInstance(calculate(i,2,3),"Enter only string")
        except Exception as e:
            print("First Argument is String")
            print ("Exception in Test Case : ", e)

    def test_print_String_lastspecialsymbol(self):
        try:
            ss=['!','@','#','$','%','^','&','*','(',')','{','}',':','[',']',';','"','\'','<',',','>','.','?','/,','-','+']
            for i in ss:
                self.assertIsInstance(calculate("Dhruvi",2,i),"Enter only Integer")
        except Exception as e:
            print("Last Argument is Number")
            print ("Exception in Test Case : ", e)

    

if __name__ == "__main__":
    unittest.main()
