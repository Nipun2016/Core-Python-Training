def calculate(name,endchar,multiple):
    return (name[:endchar]*multiple)

def check_valid_data(name,endchar,multiple):
    if (endchar < 0 or multiple < 0) :
        return False
    else:
        return True,name, endchar, multiple

if __name__ == "__main__":
    try:
        name = input("Enter string : ")
        endchar = int(input("Enter End Character Length : "))
        multiple = int(input("Enter Multiple : "))

        is_valid_input, name, endchar, multiple = check_valid_data(name,endchar,multiple)

        if not is_valid_input:
            print ("Please Enter Positive Number..")
        else:
            print (calculate(name,endchar,multiple))
    except ValueError:
        print("End Character and Multiple must be Number")
