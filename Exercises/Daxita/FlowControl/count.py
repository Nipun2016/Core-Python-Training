# def count_word(str1):
# 	list1 = str1.split(" ")
# 	list2 = []

# 	for i in range(0,len(list1)):
# 		cnt = list1.count(list1[i])
# 		if list1[i] not in list2:
# 			list2.append(list1[i])
# 			print (list1[i]," : ",cnt)	

# if __name__=="__main__":
# 	str1 = input("Enter String : ")
# 	if(str1.isalnum() or str1.find(" ")):
# 		count_word(str1)
# 	else:
# 		print("Enter valid inputs")


def count_words(input_l):
    d = {}

    for i in input_l:
        count_word = input_l.count(i)
        if i not in d:
            d.update({i: count_word})
    return (d)

def valid_data(input_l):
    try:
        if len(input_l) == 0:
            return False

        for i in input_l:
            if not i.isalpha():
                return False
    except Exception as e:
        return False

    return input_l

if __name__ == "__main__":
    #Takes the input from User and convert to list
    input_l = [x for x in input("Enter String : ").split()]

    valid_input = valid_data(input_l)

    if valid_input is False:
        print ("Please insert string only.")
    else:
        answer_dict = count_words(valid_input)
        for key, value in answer_dict.items() :
            print (key, " : " ,value)