list1 = [str(b) for b in input("Enter list ").split()]
print (list1)
list2 = []
l=len(list1)
i=0
while i<l:
    ans = list1[i]
    print ("ans=",ans)
    a = list(ans)
    temp = a[0]
    a[0] = a[-1]
    a[-1] = temp
    x="".join(a)
    print ("x=",x)
    list2.append(x)
    i=i+1
print ("list2=",list2) 
		


