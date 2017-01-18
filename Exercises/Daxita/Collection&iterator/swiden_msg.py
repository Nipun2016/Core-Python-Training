inp=input("Enter msg: ")
l=[]
str=''
l=inp.split(' ')
print (l)
dic={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
d=dic.keys()
print (d)
print([dic[d] for d in l if d in dic])