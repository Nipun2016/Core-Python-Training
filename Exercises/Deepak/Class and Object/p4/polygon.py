from polygonmodule import *
from math import sqrt

class Square(Polygon):
    #initialize the variables
    def __init__(self):
        print ("Square Called")
        Polygon.__init__(self)

    #get Area of Square
    @abstractmethod
    def get_area(self):
        print ("Square Area Called")
        return (self.list_size[0]*self.list_size[0])

class Rectangle(Polygon):
    #initialize the variables
    def __init__(self):
        print ("Rectangle Called")
        Polygon.__init__(self)

    #get Area of Rectangle
    def get_area(self):
        print ("Rectangle Area Called")
        return (self.list_size[0]*self.list_size[0])

class Triangle(Polygon):
    #initialize the variables
    def __init__(self):
        print ("Triangle Called")
        Polygon.__init__(self)

    #get Area of Triangle
    def get_area(self):
        print ("Triangle Area Called")
        p = ((self.list_side[0] + self.list_side[1] + self.list_side[2]) / 2)
        return (sqrt(p*(p-self.list_side[0])*(p-self.list_side[1])*(p-self.list_side[2])))

sides = int(input("Enter Number Of Sides : "))

if (sides == 4) :
    pollygon_name = input("Enter name of Polygon (Square / Rectangle) : ")

    if (pollygon_name == "Square" or pollygon_name == "square") :
        #print (list_side)
        obj = Square()
        #print ("Before Method Call")
        print (obj.get_area())
        #print ("After Method Call")

    if (pollygon_name == "Rectangle" or pollygon_name == "rectangle") :
        obj = Rectangle()
        #print ("Before Method Call")
        print (obj.get_area())
        #print ("After Method Call")

if (sides == 3) :
        obj = Triangle()
        #print ("Before Method Call")
        print (obj.get_area())
        #print ("After Method Call")
