inp=input("Enter braces to check balanced or not: ")
counter=0
for i in range(0,len(inp)):
	if(inp[i]=='['):
		counter+=1
	if(inp[i]==']'):
		counter-=1
	if(counter<0):
		print("NOT OK")
		break
if(counter==0):
	print("OK")
elif(counter>0):
	print("NOT OK")