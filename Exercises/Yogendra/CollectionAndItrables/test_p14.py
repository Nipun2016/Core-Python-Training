import unittest
from p14 import *
class p14TestCase(unittest.TestCase):
      def test_swd(self):
         try:  
            self.assertEqual(swedish(["happy","new","year"]),['gott', 'nytt', 'år'])
            print(['gott', 'nytt', 'år'])
         except Exception as e:
            print("Execption is:",e)
   
      def test_swd2(self):
         try:
           self.assertEqual(swedish(["happy"]),['gott'])
           print(['gott'])
         except Exception as e:
           print("Exception is: ",e)

      def test_swd3(self):
         try:
           self.assertEqual(swedish("yogendra"),[])
           print("match not found")
         except Exception as e:
           print("Exception is: ",e)

if __name__=="__main__":
   unittest.main()
