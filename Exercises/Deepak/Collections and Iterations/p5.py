def check_brackets(valid_data_list):
    counter = 0
    for i in valid_data_list:
        if (i == '['):
            counter += 1

        if (i == ']'):
            counter -= 1

        if (counter<0):
            break

    if(counter == 0):
        return ("Ok")
    else:
        return ("Not Ok")

def valid_input(user_input):
    user_input_list = " ".join(user_input).split()
    for i in user_input_list:
        if (i == "[" or i == "]" or i == "{" or i == "}" or i == "(" or i == ")") :
            continue
        else:
            return False

    return user_input_list

if __name__ == "__main__":
    user_input = input("Enter a string of brackets : ")

    valid_data_list = valid_input(user_input)
    if not valid_data_list:
        print ("Please Insert Valid Input.")
    else:
        print (check_brackets(valid_data_list))
