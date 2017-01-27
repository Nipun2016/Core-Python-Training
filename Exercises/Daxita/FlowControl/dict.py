def dict_key(dictionary,k):
	if k in dictionary.keys():
		return ("key is already there in dictionary")
	else:
		return ("key is not in dictionary")

if __name__=="__main__":
	try:
		dictionary={"1":"daxita","2":"urvi","3":"deepak"}
		k=input("Enter any key: ")
		print(dict_key(dictionary,k))
	except ValueError:
		print('Enter valid input')