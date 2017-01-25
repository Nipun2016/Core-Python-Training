def str_mul(str):
   i=str[0:1]
   b=i
   ct=0
   for a in str[1:]:
       if a!=i:       
          b=b+a
       elif a==i:
          b=b+'$'
          ct=ct+1
   if ct >0:
         return b
   else:
         return False

if __name__=="__main__":
   try:
       str=input("enter string:")
       print(str_mul(str))
   except Exception as e:
       print(e)
