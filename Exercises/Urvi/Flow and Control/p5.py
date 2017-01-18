def fun():
    flag=0
    list1 = [1,2,3,4,5]
    list2 = [4,6,8,9,20] 
    for i in list1:
        if i in list2:
            print("true")
            flag=1
            break
        #else:
          #  flag = 1
	
    if(flag == 0):
        print("false")
print("Enjoy python exercise......")
fun()
     
