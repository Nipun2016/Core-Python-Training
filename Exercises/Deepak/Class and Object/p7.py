class Stack(object):
     def __init__(self):
         self.items = []
         self.size = 2

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

cont = "y"
obj = Stack()
while cont == "y" :
    user_input = input("What You Want (push/pop/print): ")

    if (user_input == "push") :
        #print (len(obj.items))
        if(len(obj.items) <= obj.size) :
            element = int(input("Enter Element To Stack : "))
            obj.push(element)
        else:
            print ("Stack Is Full")
    elif (user_input == "pop") :
        if(len(obj.items) > 0) :
            print ("Removed Element from Stack Is : " , obj.pop())
        else:
            print ("Stack Is Empty")
    elif (user_input == "print") :
        print ("Stack Is : ", obj.items)
    else:
        print ("Please Insert Valid Input...!!")


    cont = input("Do You want to Continue (y/n) : ")
