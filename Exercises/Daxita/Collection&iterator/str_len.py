import re
def find_len(l):
	l1=[]
	for i in l:
		l1.append(len(i))
	return l1

if __name__=="__main__":
	try:
		l=input("Enter sentence: ").split()
		if(l[0].isalpha()):
			print(find_len(l))
		else:
			print("Enter valid input")
	except Exception as e:
		print("Value Error...")
#print ([len(s) for s in str(input('Enter string: ')).split()])