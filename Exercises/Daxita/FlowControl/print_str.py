class s:
	def __init__(self):
		pass
	def get_String(self):
		name=input('Enter Your Name: ')
		return name
	def print_String(self,name):
		self.name=name
		print("Your Good name is:",self.name.upper())
if __name__=="__main__":
	try:
		S=s()
		n=S.get_String()
		print(type(n))
		if(n.isalpha() and n!="None"):
			S.print_String(n)
		else:
			print("Enter String..")
	except Exception:
		print("Enter Valid Input")