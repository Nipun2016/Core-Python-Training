
def balance(valid_list):
    counter = 0
    for i in valid_list:
        if (i == '['):
            counter += 1

        if (i == ']'):
            counter -= 1

        if (counter<0):
            break

    if(counter == 0):
        return ("OK")
    else:
        return ("NOT OK")

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

    valid_list = valid_input(user_input)
    if not valid_list:
        print ("Please Insert Valid Input.")
    else:
        print (balance(valid_list))