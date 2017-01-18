
# def even_num(l):
# 	b=[]
# 	print ([i for i in l if i%2==0])
# l=[1,2,3,4,5,6,7,3,23,34]
# even_num(l);	
print (list(filter(lambda x:x%2==0,[int(x) for x in input('Enter values: ').split()])))