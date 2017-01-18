class student:
	def __init__(self,no,name):
		self.no=no
		self.name=name
d={}
n=int(input('Enter no how many students you want to add in list: '))
for i in range(0,n):
	n=int(input('Enter your roll no: '))
	your_name=input('Enter ypur name: ')
	s=student(n,your_name)
	d[n]=your_name
for key in sorted(d):
    print("%d: %s" % (key, d[key]))