def change_first(s):
	list1 = list(s)
	first = list1[0]

	for i in range(1,len(list1)):
		if list1[i] == first:
			list1[i] = "$"

	return "".join(list1)

<<<<<<< HEAD
print "".join(list1)
print("Hello")
=======
if __name__=="__main__":
	try:
		s = input("Enter string : ")
		if(s.isalpha()):
			print(change_first(s))
		else:
			print("Enter valid input as string..")
	except Exception as e:
		print(e)
>>>>>>> Collection and Iterator Unit Test
