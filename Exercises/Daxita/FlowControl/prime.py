def find_prime(n):
	flag=0
	if n in range(0,1):
		return 'not prime'
	for i in range(2,n):
		if n%i==0:
			return 'not prime'
			flag=1
			break
	if flag==0:
		return 'prime'

if __name__=="__main__":
	try:
		n=input('Enter Number')
		if (n.isdigit()):
			print(find_prime(int(n)))
		else:
			print ('Enter Only integer')
	except Exception as e:
		print(e)