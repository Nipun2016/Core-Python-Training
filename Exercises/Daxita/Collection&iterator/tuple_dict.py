#t=((1,'a'),(2,'b'),(3,'c'),(4,'d'))
#t=input("please enter tuples in main tuple")
def tup_dic(t):
	return (dict((x,y) for x,y in t))

if __name__=='__main__':
	try:
		t=((1,'a'),(2,'b'),(3,'c'),(4,'d'))
		print(tup_dic(t))
	except ValueError:
		print("Value Error")