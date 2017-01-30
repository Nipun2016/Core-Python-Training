def convert_data(valid_data):
    dictinory = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
    flag = 0
    outputText = []

    for i in valid_data:
        if(i in dictinory):
            outputText.append((dictinory.get(i)))
        else:
            flag = 1
            break

    if (flag == 0):
        return (" ".join(outputText))
    else:
        return ("Please insert valid input")

def valid_input(message):
    valid_data = message.split()

    for i in valid_data:
        if not i.isalpha():
            return False
        elif len(i) == 0:
            return False
        else:
            return valid_data

if __name__ == "__main__":
    message = input("Enter String : ")
    valid_data = valid_input(message)
    if valid_data is False:
        print ("Please Insert String only.")
    else:
        print (convert_data(valid_data))
