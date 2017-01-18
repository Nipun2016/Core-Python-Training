from itertools import permutations

word = input("Enter String : ")
perms = [''.join(p) for p in permutations(word)]
#print (perms)
list2 = []
options = ([x for x in input("Enter Value to list :").split()])
#print (options)

for i in options:
    if i in perms:
        list2.append(i)

print (list2)
