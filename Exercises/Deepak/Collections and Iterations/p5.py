user_input = input("")
list1 = " ".join(user_input).split()
#print(list1)
list2 = []
flag = 1

for i in range(0,len(list1)):
    if(list1[0] == ']'):
        flag = 0
        break
    elif (list1[i] == '['):
        list2.append('[')
        #print(list2)
    elif (list1[i] == ']'):
        try:
            list2.remove('[')
            #print(list2)
        except ValueError:
            pass

if(flag == 0):
    print ("Not Ok")
    exit()

if(len(list2) == 0):
    print ("Ok")
else:
    print ("Not Ok")
