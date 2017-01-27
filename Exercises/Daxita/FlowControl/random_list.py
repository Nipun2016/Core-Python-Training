import random
def random_common(n,m):
	a=[]
	for i in range(0,n):
		list1=random.randrange(0,10)
		a.append(list1)
	print(a)

	b=[]
	for i in range(0,m):
		list2=random.randrange(0,10)
		b.append(list2)
	print(b)
	c = []

	for i in a:
		if i in b:
			if i not in c:
				c.append(i)
	return c

if __name__=="__main__":
	n=int(input("How much number you want enter in 1st list: "))
	m=int(input("How much number you want enter in 2nd list: "))
	print(random_common(n,m))