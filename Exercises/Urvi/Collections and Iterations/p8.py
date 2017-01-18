# n = "listen"
# option = [str(a) for a in input("Enter the option for anagram ").split()]
# print (option)
# ans = []
# for i in option:
#     if i == sorted(n):
#         print (i)
#         ans.append(i)
# print (ans)
w=input('Enter string:  ')
ans = []
word=sorted(w)
options = [str(a) for a in input("Enter the option for anagram ").split()]
for i in options:
    if word == sorted(i):
        ans.append(i)
print (ans)
