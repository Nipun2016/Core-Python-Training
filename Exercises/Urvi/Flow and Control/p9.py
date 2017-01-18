stmt= input("enter the string: ")
str1= stmt.lower()
list1=str1.split(" ")
print (list1)
fstr="".join(list1)
print (fstr)
list2 = []
list3 = list(fstr)
print (list3)
for i in list3:
    if i not in list2:
        list2.append(i)
print (list2)
l=len(list2)
if(l == 26):
    print (stmt ," is panagram string.")
else:
    print (stmt ," is not panagram string.")
