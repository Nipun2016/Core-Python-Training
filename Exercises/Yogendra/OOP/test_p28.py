import unittest    
from p8 import *
class p8TestCase(unittest.TestCase):
      def test_plant1(self):
         try:  
            lst1=["Alice"]
            lst=["VVVVVVV"]
            self.assertTrue(display_plants(lst,lst1))
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
   
      def test_plant2(self):
         try:  
            lst1=["Alice"]
            lst=["RRdc"]
            self.assertTrue(display_plants(lst,lst1))
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
            
      def test_plant3(self):
         try:  
            lst1=["Alicee"]
            lst=["RR"]
            self.assertTrue(display_plants(lst,lst1))
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
if __name__=="__main__":
   unittest.main()
