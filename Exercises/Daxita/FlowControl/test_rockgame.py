import unittest
from rockgame import game

class CountRepeatedTestCase(unittest.TestCase):
    def test_game(self):
        self.assertEqual(game("Rock","Scissor"),str)

    def test_game_firstnone(self):
        try:
            self.assertIsTrue(game(None,str))
        except Exception as e:
            print("First Argument is String")
            print ("Exception in Test Case : ", e)

    def test_game_secondnone(self):
        try:
            self.assertIsTrue(game(str,None))
        except Exception as e:
            print("Second Argument is String")
            print ("Exception in Test Case : ", e)

    def test_game_bothnone(self):
        try:
            self.assertIsTrue(game(None,None))
        except Exception as e:
            print("Both Arguments are String")
            print ("Exception in Test Case : ", e)

    def test_game_firstno(self):
        try:
            self.assertIsInstance(game(2,str),str)
        except Exception as e:
            print("First Argument is String")
            print ("Exception in Test Case : ", e)

    def test_game_secondno(self):
        try:
            self.assertIsInstance(game(str,2),str)
        except Exception as e:
            print("Second Argument is String")
            print ("Exception in Test Case : ", e)

    def test_game_bothno(self):
        try:
            self.assertIsInstance(game(1,2),str)
        except Exception as e:
            print("Both Arguments are String")
            print ("Exception in Test Case : ", e)

    def test_game_secondspecialsymbol(self):
        try:
            ss=['!','@','#','$','%','^','&','*','(',')','{','}',':','[',']',';','"','\'','<',',','>','.','?','/,','-','+']
            for i in ss:
                self.assertIsInstance(game(str,i),str)
        except Exception as e:
            print("Second Argument is String")
            print ("Exception in Test Case : ", e)

    def test_game_firstspecialsymbol(self):
        try:
            ss=['!','@','#','$','%','^','&','*','(',')','{','}',':','[',']',';','"','\'','<',',','>','.','?','/,','-','+']
            for i in ss:
                self.assertIsInstance(game(i,str),str)
        except Exception as e:
            print("First Argument is String")
            print ("Exception in Test Case : ", e)


    def test_game_bothspecialsymbol(self):
        try:
            ss=['!','@','#','$','%','^','&','*','(',')','{','}',':','[',']',';','"','\'','<',',','>','.','?','/,','-','+']
            for i in ss:
                self.assertIsInstance(game(i,i),str)
        except Exception as e:
            print("Both Arguments are String")
            print ("Exception in Test Case : ", e)

            
if __name__=="__main__":
	unittest.main()