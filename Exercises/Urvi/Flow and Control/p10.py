str1 = raw_input("Enter String : ")
list1 = str1.split(" ")
#list2 = list1[0].split()
list2 = []
#print list2

for i in range(0,len(list1)):
	cnt = list1.count(list1[i])
	if list1[i] not in list2:
		list2.append(list1[i])
		print list1[i]," : ",cnt
