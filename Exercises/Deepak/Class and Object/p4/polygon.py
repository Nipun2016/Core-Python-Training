from polygonmodule import *
from math import sqrt

class Square(Polygon):
    #initialize the variables
    def __init__(self,sides,list_size):
        #print ("Square Called")
        Polygon.__init__(self,sides,list_size)

    #get Area of Square
    @abstractmethod
    def get_area(self):
        #print ("Square Area Called")
        return (self.list_size[0]*self.list_size[0])

class Rectangle(Polygon):
    #initialize the variables
    def __init__(self,sides,list_size):
        #print ("Rectangle Called")
        Polygon.__init__(self,sides,list_size)

    #get Area of Rectangle
    def get_area(self):
        #print ("Rectangle Area Called")
        return (self.list_size[0]*self.list_size[1])

class Triangle(Polygon):
    #initialize the variables
    def __init__(self,sides,list_size):
        #print ("Triangle Called")
        Polygon.__init__(self,sides,list_size)

    #get Area of Triangle
    def get_area(self):
        #print ("Triangle Area Called")
        p = ((self.list_size[0] + self.list_size[1] + self.list_size[2]) / 2)
        return (sqrt(p*(p-self.list_size[0])*(p-self.list_size[1])*(p-self.list_size[2])))

if __name__ == "__main__":
    try:
        sides = int(input("Enter Number Of Sides (3/4) : "))
        list_size = [int(a) for a in input("Enter Value : ").split()]

        if (len(list_size) == sides) :
            if (sides == 4) :
                pollygon_name = input("Enter name of Polygon (Square / Rectangle) : ")

                if (pollygon_name == "Square" or pollygon_name == "square") :
                    obj = Square(sides,list_size)
                    print (obj.get_area())

                if (pollygon_name == "Rectangle" or pollygon_name == "rectangle") :
                    obj = Rectangle(sides,list_size)
                    print (obj.get_area())

            elif (sides == 3) :
                obj = Triangle(sides,list_size)
                print (obj.get_area())
            else:
                print ("Please Enter Valid Input..")
        else:
            print ("Please Enter Valid Input..")
    except Exception:
        print ("Please Insert Digit Only..")
