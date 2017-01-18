def fun(list1,list2):
	flag=0
	for i in list1:
		#for j in list2:
			if i in list2:
				print "True"
				flag=1
				break
	if flag==0:
		print "False"
fun(["daxita","urvi","deepak","krupa"],["dax","kalgi","krupa"])