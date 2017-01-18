import random
list1 = random.sample(range(30), 4)
print ("list1=",list1)
list2 = random.sample(range(30), 6)
print ("list2=",list2)
list3 = [] 
for i in list1:
    if i in list2:
        list3.append(i)
print("list3=",list3)
        
