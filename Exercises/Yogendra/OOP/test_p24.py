import unittest
from p4 import *
class p4TestCase(unittest.TestCase):
      def test_area1(self):
         try:  
            t=triangle(1,10,20)
            self.assertEqual(t.tri_area(),100)
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
   
      def test_area2(self):
         try: 
            s=square(1,10)
            self.assertEqual(s.sq_area(),100)
            print(["success"])
         except Exception as e:
            print("Execption is:",e)

      def test_area3(self):
         try: 
            r=rectangle(1,10,20)
            self.assertEqual(r.rect_area(),200)
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
      
      def test_area4(self):
         try: 
            s=square(1)
            self.assertEqual(s.sq_area(),100)
            print(["success"])
         except Exception as e:
            print("side cannot be null:")
            print("Execption is:",e)
            
if __name__=="__main__":
   unittest.main()
