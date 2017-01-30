def find_length(valid_list):
    outputList = []
    for i in valid_list:
        outputList.append(len(i))
    return (outputList)

def valid_input(input_List):
    try:
        if len(input_List) == 0:
            return False

        for i in input_List:
            if not i.isalpha():
                return False

        return input_List
    except Exception as e:
        return False

if __name__ == "__main__":
    input_List = [x for x in input("Enter Value to list :").split()]
    valid_list = valid_input(input_List)
    if valid_list is False:
        print ("Please Enter String only...")
    else:
        print (find_length(valid_list))
