import random
def common_list(list1,list2):
    list3 = []
    for i in list1:
        if i in list2:
            list3.append(i)
    return list3

if __name__ == "__main__":
    list1 = random.sample(range(30), 4)
    list2 = random.sample(range(30), 6)
    print("list1=",list1)
    print("list2=",list2)
    print(common_list(list1,list2))
