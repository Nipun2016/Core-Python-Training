def key_check(key,value):
    dict={'sape': 4139, 'guido': 4127, 'jack': 4098}
    if key in dict:
        print("already exist")
        return False 
    else:
        dict[key]=value 
        return dict

if __name__=="__main__":
      key,value=input("enter new key:"),input("enter value:")
      print(key_check(key,value))
