def lst_cmn(a,b):
    c=[]	
    for i in a:
       if i in b:
           if i not in c:
              c.append(i)
    print(c)
    if len(c)>0:
      return True        

if __name__=="__main__":
   a=[1,2,4,3,5,6,7,8,9]
   b=[5,4,3,45,345,56,67,78,79]  
   
   lst_cmn(a,b)
