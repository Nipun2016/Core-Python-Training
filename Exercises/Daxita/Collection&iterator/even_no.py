# def even_num(l):
# 	b=[]
# 	print ([i for i in l if i%2==0])
# l=[1,2,3,4,5,6,7,3,23,34]
# # even_num(l);
# def even_no():
# 	print (set(filter(lambda x:x%2==0,[int(x) for x in input('Enter values: ').split()])))

# if __name__=="__main__":
# 	try:
# 		even_no()

def even_num(list1):
    return (list(filter(lambda a : a%2 == 0,list1)))

if __name__ == "__main__":
    try:
        list1 = [int(x) for x in input("Enter Value to list :").split()]
        print (even_num(list1))
    except Exception as e:
        print ("Enter Integer Only")