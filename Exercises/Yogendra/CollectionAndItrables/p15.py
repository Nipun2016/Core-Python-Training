import re
def square(str):
    if re.match("^[\[\] ]*$", str):
        ct=0
        for i in str:
            if ct<0:
               break    
            elif i=='[':
               ct=ct+1
            elif i==']':
               ct=ct-1
        if ct!=0:
             return ("not closed properly:")   
        else:
             return ("right closing:")    
    else:
        return ("only square brackets:")

if __name__=="__main__":
    str=input("enter [] brackets: ")
    print(square(str))
