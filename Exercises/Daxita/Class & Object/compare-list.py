def fun(list1,list2):
	flag=0
	for i in list1:
		#for j in list2:
			if i in list2:
				return "True"
				flag=1
				break
	if flag==0:
		return "False"
if __name__=="__main__":
	try:
		n=int(input("How much number you want enter in 1st list: "))
		list1=[]
		for i in range(0,n):
			a=input("Enter element of 1st list: ")
			list1.append(a)
		m=int(input("How much number you want enter in 1st list: "))
		list2=[]
		for i in range(0,m):
			b=input("Enter element of 2nd list: ")
			list2.append(b)
		print(fun(list1,list2))
	except ValueError:
		print("Value Error..")