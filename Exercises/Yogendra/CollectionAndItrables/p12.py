def wrd_len(lst1):
  dict={}
  print("enter 1 for for loop 2 for list coperhensive:")
  ch=int(input("enter choice: "))
  if ch==1:
        for ele in lst1:
            n1=len(ele)
            dict[ele]=n1
            print(ele,n1)
        return True
        
  elif ch==2:
        return([(ele,len(ele)) for ele in lst1])

if __name__=="__main__":
    in_lst=input("enter list items: ")
    str1=''
    lst1=[]
    for str in in_lst:
        if str!= ' ':
           str1=str1+str
        else:
           lst1.append(str1)
           str1=''
    lst1.append(str1)
    ot_lst=[]
    print(lst1)
    print(wrd_len(lst1))
         
