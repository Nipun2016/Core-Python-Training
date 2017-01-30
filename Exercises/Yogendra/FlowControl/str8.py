def is_prime(num):
    if num > 1:
        for i in range(2,num):
           if (num % i) == 0:
               print(num,"is not a prime number")
               print(i,"times",num//i,"is",num)
               break
        else:
           print(num,"is a prime number")
           return True 
    else:
         print(num,"is not a prime number")
         return False

if __name__=="__main__":
    try:
        num=int(input("enter number"))
        is_prime(num)
    except Exception as e:
        print("only integers")
