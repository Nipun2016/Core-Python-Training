n=input("Enter the range:")
for k in range(2,n+1):
    flag=1
    for i in range(2,(k-1/2)):
        if(k%i==0):
	    print k," equals ",i,"*",k//i
            flag=0
    if(flag==1):
        print k," is prime number"
