# import itertools
# n=int(input("Enter n: "))
# l=[]
# for i in range(0,n):
# 	lt=input("Enter integers in list")
# l.append(lt)
# print (l)
# #print ([ii for ii in zip(*l)])
t=1,2,4,56554
t1='a','frv','dsfawd'
t2='s3de',2,'sadas'
tupple_list=[t,t1,t2]
new_list=[]
print("list of tuples: ")
print(tupple_list)
for tpple in tupple_list:
          for ele in tpple:
                 new_list.append(ele)
          # print("TUPPPLE IN LIST------------>")
          # print(new_lst)
          # new_lst.clear()