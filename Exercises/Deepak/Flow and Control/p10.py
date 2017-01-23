def count_words(input_data_list):
    dictionary = {}

    for i in input_data_list:
        count_word = input_data_list.count(i)
        if i not in dictionary:
            dictionary.update({i: count_word})
    return (dictionary)

def valid_data(input_data_list):
    try:
        if len(input_data_list) == 0:
            return False

        for i in input_data_list:
            if not i.isalpha():
                return False
    except Exception as e:
        return False

    return input_data_list

if __name__ == "__main__":
    #Takes the input from User and convert to list
    input_data_list = [x for x in input("Enter String : ").split()]

    valid_input_data = valid_data(input_data_list)

    if valid_input_data is False:
        print ("Please insert string only.")
    else:
        answer_dict = count_words(valid_input_data)
        for key, value in answer_dict.items() :
            print (key, " : " ,value)
