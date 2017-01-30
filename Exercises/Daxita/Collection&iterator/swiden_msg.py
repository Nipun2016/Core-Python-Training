def swiden(inp):
	l=[]
	str=''
	l=inp.split(' ')
	dic={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
	d=dic.keys()
	return ([dic[d] for d in l if d in dic])

if __name__=="__main__":
	inp=input("Enter msg: ")
	print(swiden(inp))