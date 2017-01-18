# num = int(input("Enter the limit "))
# ls = [int(a) for a in input("Enter the num for that you want multiple ").split()]
# print (ls)
print (list(filter(lambda x: x%3==0 or x%5==0,[int(a) for a in range(int(input('Enter range: ')))])))
