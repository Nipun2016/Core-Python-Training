def convert(plainText):
    listofPlainText = plainText.split()
    anslist = []
    for i in listofPlainText:
        charofWord = " ".join(i).split()
        for j in charofWord:
            c = ord(j)
            if (c>78 and c<91) :
                anslist.append(chr(c - 13))
            elif (c>109 and c<123) :
                anslist.append(chr(c - 13))
            else:
                anslist.append(chr(c + 13))

        anslist.append(" ")
    return anslist

def valid_input(input_data):
    try:
        if not input_data.isalpha():
            return False
    except Exception as e:
        return False
    return input_data

if __name__ == "__main__":
    option = input("Do you want to Encrypt or Decrypt : ")
    if (option == "Encrypt" or option == "encrypt"):
        plainText = input("Enter Plain text : ")
        valid_data = valid_input(plainText)

        if not valid_data:
            print("Please Enter String only...!!!")
        else:
            print ("Decrypted Text is : " , "".join(convert(plainText)))

    elif (option == "Decrypt" or option == "decrypt"):
        cypherText = input("Enter Cypher text : ")
        valid_data = valid_input(cypherText)

        if not valid_data:
            print("Please Enter String only...!!!")
        else:
            print ("Encrypted Text is : " , "".join(convert(cypherText)))
    else:
        print("Please Enter Valid Input...!!!")
