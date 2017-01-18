name= input("Enter name:")
print (name)
m=list(name)
n=m[0]
#print (n)
#print (m)
x=len(m)
for i in range(1,x):
    if(m[i]==n):
        m[i]='$'
print ("".join(m))

