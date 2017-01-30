def fun(list1,list2):
    for i in list1:
        if i in list2:
            return True
    else:
        return False

if __name__ == "__main__":
    list1 = [1,2,3,4]
    list2 = [1,22,33,44]
    print(list1)
    print(list2)
    print (fun(list1,list2))
