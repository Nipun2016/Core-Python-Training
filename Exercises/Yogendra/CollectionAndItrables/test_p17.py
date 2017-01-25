import unittest
from p17 import *
class p17TestCase(unittest.TestCase):
      def test_tupp1(self):
         try:  
            self.assertEqual(tupp2dict(('i','am','yogendra','katewa',647346)),{1: 'i', 2: 'am', 3: 'yogendra', 4: 'katewa', 5: 647346})
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
   
      def test_tupp2(self):
         try:  
            self.assertEqual(tupp2dict(()),{})
            print(["success"])
         except Exception as e:
            print("Execption is:",e)
      
if __name__=="__main__":
   unittest.main()
