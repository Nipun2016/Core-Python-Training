from polygon import *
class triangle(Polygon):
        pass
class square(Polygon):
        pass
class rectangle(Polygon):
        pass


def area(poly,base,high=1):  
   if poly == '1':
       t=triangle(poly,base,high)
       return(t.tri_area())
       
   elif poly == '2':
       s=square(poly,side)
       return(s.sq_area())
       
   elif poly == '3':
        r=rectangle(poly,width,high)
        return(r.rect_area())
        
  

if __name__=="__main__":
     ch='y'
     while ch=='y':
           poly=input("enter 1 for triangle 2 for square 3 for rectangle: ")
           if poly == '1':
              base=int(input("enter base: "))
              high=int(input("enter height: "))
              print(area(poly,base,high))
           elif poly == '2':
              side=int(input("enter side: "))
              print(area(poly,side))
           elif poly == '3':
              width=int(input("enter width: "))
              high=int(input("enter height: "))
              print(area(poly,width,high))
           ch=input("do u wish to continue: enter y for continue: ")










