def num_cal(n):
    return([num for num in range(1,n) if (num%3 ==0 or num%5 ==0) and (num != 3 and num !=5)])

if __name__=="__main__":
   try:
      n=int(input("enter range"))
      print(num_cal(n))
   except Exception as e:
      print("strings not allowed")
