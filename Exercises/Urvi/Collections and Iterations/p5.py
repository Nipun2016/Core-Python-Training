input_string = input("Enter the string of parenthesis ")
cnt = 0
for i in input_string:
    if(i == '['):
        cnt+=1
    if(i == ']'):
        cnt-=1

if(input_string[0] == ']'):
    print ("not ok")
    exit()
if(cnt == 0):
    print ("ok")
if(cnt > 0):
    print ("not ok")
