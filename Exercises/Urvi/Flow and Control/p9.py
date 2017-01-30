import string

def ispanagram(input_string, alphabet=string.ascii_lowercase):
    alphabet = set(alphabet)
    return alphabet <= set(input_string.lower())

if __name__ == "__main__":
    input_data = input("Please Insert String : ")
    if ispanagram(input_data):
        print (input_data," is Panagram")
    else:
        print (input_data," is not Panagram")

#qwertyuioplkjhgfdsazxcvbnm
