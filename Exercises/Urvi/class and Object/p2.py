from math import pi
class circle:
    'this is circle class'
    def __init__(self,r):
        self.r = r
        print("circle called")

    def compute_Area(self):
        a = pi*self.r*self.r
        print("The area of circle is ",a)

    def compute_Perimiter(self):
        p = 2*pi*self.r
        print("The perimeter of circle is ",p)

c = circle(int(input("Enter the radius:")))
c.compute_Area()
c.compute_Perimiter()
