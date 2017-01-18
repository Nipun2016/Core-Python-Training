pt=input("Enter the plantext:")
print ("plantext=",pt,"\nencoding...")
pt2=pt.split()
ct = []
for c in pt2:
    pt3=" ".join(c).split()
    for i in pt3:
        j=ord(i)
        if(j>78 and j<91):
            ct.append(chr(j-13))
        elif(j>109 and j<123):
            ct.append(chr(j-13))
        else:
            ct.append(chr(j+13))
    ct.append(" ")

cypherText = "".join(ct).split()
print ("cypher text=",cypherText,"\ndecoding...")
#print (cypherText)
dt=[]
for c in cypherText:
    #print (c)
    ct2=" ".join(c).split()
    #print (ct2)
    for i in ct2:
        j=ord(i)
        if(j>78 and j<91):
            dt.append(chr(j-13))
        elif(j>109 and j<123):
            dt.append(chr(j-13))
        elif(j==32):
            pass
        else:
            dt.append(chr(j+13))
    dt.append(" ")
#print (dt)
print ("plantext=","".join(dt))
