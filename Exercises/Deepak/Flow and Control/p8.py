def prime_number(lastValue):
    if lastValue > 1:
       for i in range(2,lastValue):
           if (lastValue % i) == 0:
               return "{} is not a prime number".format(lastValue)
               break
       else:
           return "{} is a prime number".format(lastValue)
    else:
       return "{} is not a prime number".format(lastValue)


if __name__ == "__main__":
    try:
        lastValue = int(input("Enter a number: "))
        print (prime_number(lastValue))
    except ValueError:
        print ("Please Enter Interger Value")
