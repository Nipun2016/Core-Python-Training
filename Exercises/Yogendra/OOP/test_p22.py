import unittest
from p2 import *
class p2TestCase(unittest.TestCase,Circle):
      def test_str1(self):
         try:  
            cir=Circle(3)
            #myc.area()
            self.assertEqual(cir.area(),28.27)
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
   
      def test_str2(self):
         try: 
            cir=Circle(3)
            #myc.area()
            self.assertEqual(cir.perimeter(),18.85)
            print(["success"])
         except Exception as e:
            print("Execption is:",e)

      def test_str3(self):
         try:  
            cir=Circle(1)
            self.assertEqual(cir.area(),"3.14")
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
            
if __name__=="__main__":
   unittest.main()
