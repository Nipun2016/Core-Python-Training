flist=[]
str1=raw_input("Enter any sentence for find paramgram or not..")
str2=str1.split(' ')
print str2
str3=''.join(str2)
print str3
str4=list(str3)
print str4
for i in str4:
	if i not in flist:
		flist.append(i)
print flist
l=len(flist)
if l == 26:
	print "pangram"
else:
	print "not pangram"