def compute_anagram(s,alternatives):
	b=[]
	word=sorted(s)
	for a in alternatives:
	    if word == sorted(a):
	    	b.append(a)
	return(b)

if __name__=="__main__":
	try:
		s = str(input('Enter string:'))
		if (s.isalpha() or s.isalnum() or len(s)!=0):
			alternatives = (list(str(ar) for ar in input('Enter Alternatives: ').split()))
			if len(alternatives)!=0:
				print(compute_anagram(s,alternatives))
			else:
				print("Please enter alternatives")
		else:
			print("Enter valid Inputs..")
	except ValueError:
		print("Value error caught")
	except Exception as e:
		print(e)