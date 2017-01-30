def calculate(s,n,m):
	return (s[:n]*m)

if __name__=="__main__":
	try:
		s=input('Enter string ')
		if(s.isalpha()):
			n=int(input('Enter value of n '))
			m=int(input('Enter value of m '))
			print(calculate(s,n,m))
		else:
			print("Enter only string")
	except ValueError:
			print("Enter only integers in value of n and m")
	except OSError as err:
	    print("OS error: {0}".format(err))
	except RuntimeError as e:
		print("Runtimeerror: ",e)