def changeChar(name_to_list, firstChar):
    for i in range(1,len(name_to_list)):
        if(name_to_list[i] == firstChar or name_to_list[i] == firstChar.upper() or name_to_list[i] == firstChar.lower()):
            name_to_list[i] = '$'
    return ("".join(name_to_list))

def formate_data(name):
    try:
        if name.isalpha():
            name_to_list = list(name)
            firstChar=name_to_list[0]
            return name_to_list, firstChar
    except Exception as e:
            return False

if __name__ == "__main__":
    name = input("Enter Name : ")
    try:
        formated_input,firstChar = formate_data(name)
        print (changeChar(formated_input, firstChar))
    except Exception as e:
        print ("Please insert String only.")
