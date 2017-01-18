dictinory = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
#print (dictinory.keys())
message = input().split()
flag = 0
#print (message)
outputText = []
for i in message:
    if(i in dictinory):
        outputText.append((dictinory.get(i)))
    else:
        flag = 1
        break

if (flag == 0):
    print (" ".join(outputText))
else:
    print ("Please insert valid input")
