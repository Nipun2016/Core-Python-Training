def count_str(str):
  str1=""
  lst=[]
  lst2=[]
  lst3=[]
  dict={}
  count=0
  j=0
  if str=="":
     return False
  for i in str:
     if i != " ":
          str1=str1+i
     else:
          lst.append(str1)   
          str1=""
  lst.append(str1)
  lst.sort()
  for i in sorted(lst):	
    lst2.append(i)


  for i in lst:
    count=0
    s1=i
    for j in lst:
      s2=j
      if s1==s2:
         if s1 in lst2:       
            lst2.remove(s1)
            count=count+1
    
    if count >0:
      lst3.append((i,count))
  return lst3
if __name__=="__main__":
      str=input("enter string:")
      print(count_str(str))
