def unpack(tupple_list):
    new_lst=[]
    print("LIST OF TUPPLES")
    print("----------------")
    print(tupple_list)
    print("-------------------------------------")
    for tpple in tupple_list:
             for ele in tpple:
                  new_lst.append(ele)
             print("TUPPPLE IN LIST------------>")
             print(new_lst)
             new_lst.clear()

if __name__=="__main__":
    t='yogendra','katewa','dharmesh'
    t1=14112,527235,623328
    t2='ravi','amit','abhishek'
    tupple_list=[t,t1,t2]
    unpack(tupple_list)
