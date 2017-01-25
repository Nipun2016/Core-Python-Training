import unittest
from str7 import *
class str7TestCase(unittest.TestCase):
      def test_chk_game_1(self):
         try:  
            self.assertEqual(game("rock","paper"),"player2")
            print("player2")
         except Exception as e:
            print("Execption is:",e)
   
      def test_chk_game_2(self):
         try:
           self.assertEqual(game("PapEr","RoCk"),"player1")
           print("player1")
         except Exception as e:
           print("Exception is: ",e)

      def test_chk_game_3(self):
         try:
           self.assertEqual(game("rock","scissors"),"player1")
           print("player1")
         except Exception as e:
           print("Exception is: ",e)

      def test_chk_game_4(self):
         try:
           self.assertEqual(game("ROck","ScISSoRs"),"player1")
           print("player1")
         except Exception as e:
           print("Exception is: ",e)

      def test_chk_game_5(self):
         try:
           self.assertEqual(game("ScISSoRs","paper"),"player1")
           print("player1")
         except Exception as e:
           print("Exception is: ",e)

      def test_chk_game_6(self):
         try:
           self.assertEqual(game("paper","scissors"),"player2")
           print("player2")
         except Exception as e:
           print("Exception is: ",e)
      def test_chk_game_7(self):
         try:
           self.assertEqual(game("ScISSoRs","paper"),"player1")
           print("player1")
         except Exception as e:
           print("Exception is: ",e)
      def test_chk_game_8(self):
         try:
           self.assertEqual(game("PaPeR","paper"),"tie")
           print("tie")
         except Exception as e:
           print("Exception is: ",e)

 
if __name__=="__main__":
   unittest.main()
