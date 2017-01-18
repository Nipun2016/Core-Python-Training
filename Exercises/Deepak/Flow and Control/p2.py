name = input("Enter Name:")
#print (name)
nametoList=list(name)
firstChar=nametoList[0]
x=len(nametoList)
for i in range(1,x):
    if(nametoList[i]==firstChar):
        nametoList[i]='$'
print ("".join(nametoList))

