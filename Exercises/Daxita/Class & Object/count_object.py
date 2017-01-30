class count(object):
	counter = 0
	def __init__(self):
		count.counter += 1
		print(count.counter)
if __name__=="__main__":
	a = count()
	a=count() 
	a=count() 
	a=count()