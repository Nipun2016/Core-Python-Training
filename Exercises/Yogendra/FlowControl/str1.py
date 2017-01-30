#str,num1,num2=input("enter string:"),int(input()),int(input())
#print(str[0:num1] * num2)
def str_mul(str,num1,num2):
    if num1 > 0 or num2 >0:
         return (str[:num1]*num2)
    else:
         return False

if __name__=="__main__":
       str=input("enter string:")
       try:
            num1=int(input("enter char"))
            num2=int(input("repeating numbers"))
            print(str_mul(str,num1,num2)) 
       except Exception as e:
            print("!-------------position and numbers must be in numbers:")
            

