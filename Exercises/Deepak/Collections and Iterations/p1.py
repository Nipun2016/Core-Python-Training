option = input("Do you want to Encrypt or Decrypt : ")
def convert(charofWord):
    for j in charofWord:
        c = ord(j)
        #print (c)
        if (c>78 and c<91) :
            anslist.append(chr(c - 13))
        elif (c>109 and c<123) :
            anslist.append(chr(c - 13))
        else:
            anslist.append(chr(c + 13))

    anslist.append(" ")

if (option == "Encrypt") :
    plainText = input("Enter Plain text : ")
    listofPlainText = plainText.split()
    #print (listofPlainText)
    anslist = []
    for i in listofPlainText:
        charofWord = " ".join(i).split()
        convert(charofWord)
    print ("Cypher Text : " + "".join(anslist))
elif (option == "Decrypt"):
    cypherText = input("Enter Cypher text : ")
    listofcypherText = cypherText.split()
    #print (listofcypherText)
    anslist = []
    for i in listofcypherText:
        charofWord = " ".join(i).split()
        convert(charofWord)
    print ("Plain Text : " + "".join(anslist))
else:
    print ("Please insert valid input..!!")
