import random
def test_check(list1,list2):
    list3 = []
    for i in list1:
        if i in list2:
            list3.append(i)
    return list3

if __name__ == "__main__":
    list1 = random.sample(range(20),5)
    list2 = random.sample(range(20),7)
    print(list1)
    print(list2)
    print (test_check(list1,list2))
