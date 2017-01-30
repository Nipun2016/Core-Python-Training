from itertools import count
class Square:
    obj=0
    def __init__(self):
       self.__class__.obj=self.__class__.obj+1

    def get_square(self):
           return self.__class__.obj
if __name__=="__main__":
    class call(Square):
         sq1=Square()
         sq1=Square()
         a=sq1.get_square()
         print(a)
