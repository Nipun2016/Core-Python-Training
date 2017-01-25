def lst(a):
    if len(a)!=0:
       for ls in a:
           str1=ls
           ln=len(str1)
           ft=str1[:1]
           lt=str1[ln-1:]
           print(str1.replace(ft,lt,1))
           print(str1.replace(lt,ft))
           print("----------")
           print("")            
       a.reverse()
       print(a)
       return True
    else:
       return False   

if __name__=="__main__":
   str=input("element for lists:")
   a=[]
   b=""
   for i in str:
      if i != " ":
          b=b+i
      else:
          a.append(b)
          b=""	 
   a.append(b)
   print(a)
   lst(a) 
