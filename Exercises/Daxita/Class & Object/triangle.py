from polygon import polygon
n=int(input('Enter no of sides: '))




if n==3:
	class triangle(polygon):
		def noofsides(self,no):
			return no
		def getarea(self,side1,side2,side3):
			self.side1=side1
			self.side2=side2
			self.side3=side3
			s=(self.side1+self.side2+self.side3)/2
			area=((s*(s-self.side1)*(s-self.side2)*(s-self.side3))**(1/2))
			print("Area of triangle is: ",area)

	s1=int(input('Enter s1: '))
	s2=int(input('Enter s2: '))
	s3=int(input('Enter s3: '))
	t=triangle()
	t.getarea(s1,s2,s3)



if n==4:
	name=input('Enter name of polygon(square/rectangle): ')



	if name=="square" or name=="Square" or name=="SQUARE":
		class square(polygon):
			def noofsides(self,no):
				return no
			def getarea(self,side1):
				self.side1=side1
				area=(self.side1**2)
				print("Area of square is: ",area)
		s1=int(input('Enter s1: '))
		s=square()
		s.getarea(s1)


	if name=="rectangle" or name=="Rectangle" or name=="RECTANGLE":
		class rectangle(polygon):
			def noofsides(self,no):
				return no
			def getarea(self,l,w):
				self.l=l
				self.w=w
				area=(self.l*self.w)
				print("Area of square is: ",area) 
		s1=int(input('Enter s1: '))
		s2=int(input('Enter s2: '))
		r=rectangle()
		r.getarea(s1,s2)