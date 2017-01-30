
def is_common(list1,list2):
    for i in list1:
        if i in list2:
            return True
    else:
        return False

if __name__ == "__main__":
    list1 = [int(a) for a in input("Enter the list1:").split()]
    list2 = [int(a) for a in input("Enter the list2:").split()]
    print(list1)
    print(list2)
    print(is_common(list1,list2))
