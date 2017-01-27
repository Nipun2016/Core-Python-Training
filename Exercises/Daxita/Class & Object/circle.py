import math
import numbers
class Circle:
	def __init__(self,radius):
		self.radius=radius
	def area(self):
		a=math.pi*self.radius**2
		return a
	def parimeter(self):
		p=2*math.pi*self.radius
		return p
if __name__=="__main__":
	try:
		r=float(input('Enter the radius of circle: '))
		if (isinstance(r,numbers.Number)):
			c=Circle(float(r))
			area=c.area()
			print('\nCircle Area is: {:0.2f}'.format(area))
			parimeter=c.parimeter()
			print('\nCircle Perimeter is: {:0.2f}'.format(parimeter))
		else:
			print("Enter proper Inputs")
	except Exception as e:
		print("Please Enter Integer or Float")