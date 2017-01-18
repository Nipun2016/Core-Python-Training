from parent import Polygone
from math import sqrt

class Square(Polygone):

    def __init__(self):
        Polygone.__init__(self)
        print("S called")

    #@abstractmethod
    def compute_Area(self):
        ans = self.list_size[0]*self.list_size[0]
        return "area of Square is {}".format(ans)

class Rectangle(Polygone):

    def __init__(self):
        Polygone.__init__(self)
        print("R called")

    #@abstractmethod
    def compute_Area(self):
        ans = self.list_size[0]*self.list_size[1]
        return "area of Rectangle is {}".format(ans)

class Triangle(Polygone):

    def __init__(self):
        Polygone.__init__(self)
        print("T called")

    #@abstractmethod
    def compute_Area(self):
        s = (self.list_size[0]+ self.list_size[1]+ self.list_size[2])/2
        x = s*(s-self.list_size[0])*(s-self.list_size[1])*(s-self.list_size[2])
        ans = sqrt(x)
        return "area of triangle is {}".format(ans)

s = Square()
print (s.compute_Area())

r = Rectangle()
print(r.compute_Area())

t = Triangle()
print(t.compute_Area())
