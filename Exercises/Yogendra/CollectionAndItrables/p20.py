def yrange(n):
	i=0
	while i<n:
		yield i
		i=i+1

if __name__=="__main__":
	try:
		n=int(input("enter number"))
		y=yrange(n)
		for i in range(n):
			print(y.__next__())
	except Exception as e:
		print(e)
		print("string is not valid here")
