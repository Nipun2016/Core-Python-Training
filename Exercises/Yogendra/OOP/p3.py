def subset(array, num):
    result = []
    fin_res=[]
    def find(arr, num, path=()):
        if not arr:
            return
        if arr[0] == num:
            result.append(path + (arr[0],))
        else:
            find(arr[1:], num - arr[0], path + (arr[0],))
            find(arr[1:], num, path)
    find(array, num)
    for ele in result:
        if len(ele)==3:
           fin_res.append(ele)
    print(fin_res)
    return True
if __name__=="__main__":
    try:
        num1=int(input("enter first num"))
        num2=int(input("enter last num"))
        lst=[]
        for i in range(num1,num2):
           if i !=0:
             lst.append(i) 
        print(subset(lst,0))
    except Exception as e:
           print("you cannot enter string")
