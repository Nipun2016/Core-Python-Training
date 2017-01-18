list1 = [(1,2),(3,4),(5,6,7,8),(5,6,8)]

for i in list1:
    if (type(i) == tuple):
        print (list(i))
    else:
        print "Variable is not tuple in list"
