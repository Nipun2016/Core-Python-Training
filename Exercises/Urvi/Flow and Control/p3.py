def check(key):
    d= {"urvi":99,9:"dac","deepak":100,"daxita":98,"krupa":78}
    keylist= d.keys()
    if(key in keylist):
        return True
    else:
        return False

if __name__ == "__main__":
    key = input("Enter the key:")
    print (check(key))
