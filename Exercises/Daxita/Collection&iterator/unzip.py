# import itertools
# n=int(input("Enter n: "))
# l=[]
# for i in range(0,n):
# 	lt=input("Enter integers in list")
# l.append(lt)
# print (l)
# #print ([ii for ii in zip(*l)])
def tuple_con_list(t,t1,t2):
	tupple_list=[t,t1,t2]
	new_list=[]
	print("list of tuples: ")
	return(tupple_list)

if __name__=="__main__":
	try:
		t=1,2,4,56554
		t1='a','frv','dsfawd'
		t2='s3de',2,'sadas'
		print(tuple_con_list(t,t1,t2))
	except ValueError:
		print("Value Error")