guide = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
k = guide.keys()
sm=[]
flag = 0
intext = input("Enter the text=").split()
#print (intext)
for i in intext:
    if(i in k):
        sm.append(guide[i])
        #print ("swidden message=",sw)
    else:
        flag = 1
        break
if(flag == 0):
    print ("swidden message="," ".join(sm))
else:
    print("oops..... insert valid input......")
