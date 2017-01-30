def gen(n):
    i = 0
    while i < n:
        yield i
        i += 1
if __name__=="__main__":
	try:
		n=int(input("Enter no: "))
		g=gen(n)
		for i in range(0,n):
			print(next(g))
# 		print(next(g))
	except ValueError:
		print("Value Error")