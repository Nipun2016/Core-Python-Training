#print (list(filter(lambda a: a%3==0 or a%5==0,[int(a) for a in range(int(input('Enter range: ')))])))
def multiple(n):
	n1=[]
	res=[int(a) for a in n]
	for i in res:
		if(i%3==0 or i%5==0):
			n1.append(i)
	return(n1)
if __name__=="__main__":
	try:
		n=input("Enter integer to find multiplier with 3 or 5: ").split()
		if(len(n)!=0):
			print(multiple(n))
		else:
			print("Enter only Integer")
	except ValueError:
		print("Enter Valid Inputs")
