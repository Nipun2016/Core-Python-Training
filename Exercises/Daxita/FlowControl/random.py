# import random
# print (random.randint(0, 10))
n=input("How much number you want enter in 1st list: ")
a=[]
for i in range(0,n):
	list1=raw_input("Enter element of 1st list: ")
	a.append(list1)

m=input("How much number you want enter in 1st list: ")
b=[]
for i in range(0,m):
	list2=raw_input("Enter element of 1st list: ")
	b.append(list2)
# # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
# a.append(list1)
# b.append(list2)
# b=list(list2)
for i in a:
	if i in b:
		if i not in c:
			c.append(i)
print c