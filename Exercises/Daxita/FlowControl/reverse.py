# string = raw_input("Enter list: ")
# list1 = list(string)

# temp = list1[0]
# list1[0] = list1[-1]
# list1[-1] = temp
# print "".join(list1[::-1])
n=input("How much number you want enter in 1st list: ")
list1=[]
for i in range(0,n):
    a=raw_input("Enter element of 1st list: ")
    list1.append(a)

# list1 = ["abcd","xyzw","jbjh","jkb"]
list2 = []
l=len(list1)
i=0
for i in range(0,l):
    ans = list1[i]
    a = list(ans)
    temp = a[0]
    a[0] = a[-1]
    a[-1] = temp
    x="".join(a)
    list2.append(x)
    i=i+1
print "Final list= ",list2