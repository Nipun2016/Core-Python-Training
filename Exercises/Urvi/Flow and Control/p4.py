def reverselist(list1):
    list2 = []
    i=0
    for i in range(0,len(list1)):
        ans = list1[i]
        a = list(ans)
        temp = a[0]
        a[0] = a[-1]
        a[-1] = temp
        x="".join(a)
        list2.append(x)
    return (list2[::-1])

if __name__ == "__main__":
    list1 = [str(b) for b in input("Enter Data to the list : ").split()]
    print (reverselist(list1))
