class s:
	def __init__(self):
		pass
	def get_String(self):
		name=input('Enter Your Name: ')
		return name
	def print_String(self,name):
		self.name=name
		print("Your Good name is:",self.name)

S=s()
n=S.get_String()
S.print_String(n)
