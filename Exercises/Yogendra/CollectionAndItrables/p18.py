
def chk_anagram(srch_ele):
    ct=0
    flag=0
    lst1=[]
    str1=''
    for str in srch_ele:
       if str!= ' ':
            str1=str
            lst1.append(str1)
    main_lst=["enlists","google","inlets","banana" ]
    for ele in main_lst: 
       ct=0
       if len(ele) == len(srch_ele):
           for ch in ele:
                cn=ele.count(ch) 
                if ch in srch_ele:
                    ct=ct+1
                    cn1=lst1.count(ch)
                    if cn!=cn1:
                        break
           if ct == len(srch_ele):
              return ("anagram")
              flag=1
              break
    if flag==0:
        return ("not anagram")


if __name__=="__main__":
    srch_ele=''
    srch_ele=input("enter search element: ")
    
    print(chk_anagram(srch_ele))
