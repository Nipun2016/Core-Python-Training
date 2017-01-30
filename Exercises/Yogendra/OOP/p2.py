import math
class Circle:
      def __init__(self,rad):
          self.rad=rad
      def area(self):
          return round(math.pi*self.rad*self.rad,2)
      def perimeter(self):
          return round(2*math.pi*self.rad,2)

if __name__=="__main__":
    rad=int(input("enter number"))
    cir=Circle(rad)
    print("area of the circle :",cir.area())
    print("perimeter of the circle :",cir.perimeter())
