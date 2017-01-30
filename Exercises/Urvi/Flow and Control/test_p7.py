import unittest
from p7 import play_game

class P7TestCase(unittest.TestCase):
    def test_playgame(self):
        self.assertIsInstance(play_game("rock","rock"),str)

    def test_check_player_none(self):
        try:
            self.assertTrue(play_game(None,"rock"))
        except Exception as e:
            print("Please Insert Any Data in Player")
            print ("Exception in Test Case : ", e)

    def test_check_computer_none(self):
        try:
            self.assertTrue(play_game("rock",None))
        except Exception as e:
            print("Please Insert Any Data in Computer")
            print ("Exception in Test Case : ", e)

    def test_check_both_none(self):
        try:
            self.assertTrue(play_game(None,None))
        except Exception as e:
            print("Please Insert Any Data")
            print ("Exception in Test Case : ", e)

    def test_playgame_True(self):
        self.assertEqual(play_game("paper","rock"),"congratulation!.....player win")

if __name__ == "__main__":
    unittest.main()
