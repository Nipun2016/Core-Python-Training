str = raw_input("Enter string : ")
#print str
list1 = list(str)
#print list1
#print len(list1)

first = list1[0]
#print first

for i in range(1,len(list1)):
	if list1[i] == first:
		list1[i] = "$"

print "".join(list1)