import unittest
from p1 import *
class p1TestCase(unittest.TestCase,MyClass):
      def test_str1(self):
         try:  
            myc=MyClass()
            myc.get_String("katewa")
            self.assertEqual(myc.print_String(),"katewa")
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
   
      def test_str2(self):
         try: 
            myc=MyClass() 
            myc.get_String("yogendra")
            self.assertEqual(myc.print_String(),"yogendra")
            print(["success"])
         except Exception as e:
            print("Execption is:",e)

      def test_str3(self):
         try:  
            myc=MyClass()
            myc.get_String(" katewa")
            self.assertEqual(myc.print_String(),"katewa")
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
            
if __name__=="__main__":
   unittest.main()
