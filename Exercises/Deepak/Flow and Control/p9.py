stmt= input("enter the string: ")
str1= stmt.lower()

list1=str1.split(" ")

fstr="".join(list1)

list2 = []
list3 = list(fstr)

for i in list3:
    if i not in list2:
        list2.append(i)

length=len(list2)

if(length == 26):
    print (stmt ," is panagram string.")
else:
    print (stmt ," is not panagram string.")
