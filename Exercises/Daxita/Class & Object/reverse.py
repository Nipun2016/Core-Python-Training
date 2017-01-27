def reverse_list(n,list1):
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
    print("Final List is:")
    return (list(reversed(list2)))
        #return i

if __name__=="__main__":
    try:
        n=int(input("How much number you want enter in 1st list: "))
        list1=[]
        for i in range(0,n):
            a=input("Enter element of 1st list: ")
            if a.isalpha():
                list1.append(a)
            else:
                print("Enter valid input")
        print(reverse_list(n,list1))
    except ValueError:
        print("Value Error")