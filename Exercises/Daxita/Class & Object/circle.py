import math
class Circle:
	def __init__(self,radius):
		self.radius=radius
	def area(self,radius):
		self.radius=radius
		a=math.pi*self.radius**2
		return a
	def parimeter(self,radius):
		self.radius=radius
		p=2*math.pi*self.radius
		return p

r=int(input('Enter the radius of circle: '))
c=Circle(r)
area=c.area(r)
print('\nCircle Area is: {:0.2f}'.format(area))
parimeter=c.parimeter(r)
print('\nCircle Perimeter is: {:0.2f}'.format(parimeter))