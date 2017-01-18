s = str(input('Enter string:'))
word=sorted(s)
alternatives = (list(str(ar) for ar in input('Enter string: ').split()))
for a in alternatives:
    if word == sorted(a):
        print (a)
