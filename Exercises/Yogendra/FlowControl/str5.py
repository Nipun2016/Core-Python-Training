def chk_lst(a,b):
   for i in a:
       if b.count(i):
           return True     
       
if __name__=="__main__":
    a=[1,3,5,6,8,9]
    b=[2,4,6,8,10,12,14,16]
    print(chk_lst(a,b))
