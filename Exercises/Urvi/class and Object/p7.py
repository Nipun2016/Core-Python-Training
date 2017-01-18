class liststack():

    #initialize stack
    def __init__(self):
        self.lstack = []
        self.maxsize = 3
    #for pushing data
    def push(self, item):
        if(len(self.lstack) <= self.maxsize ):
            self.lstack.append(item)
            print("stack after pushing ",self.lstack)
        else:
            print("stack is full")
    #for pop the item
    def pop(self):
        if(len(self.lstack) > 0):
            print("popped element is",self.lstack.pop()," and stack is ",self.lstack)
        else:
            print("Stack is empty")

l = liststack()
inp = 'Y'
while inp == 'Y':
    u_in = input("Select option PUSH or POP: ")
    if(u_in == "PUSH"):
        element = input("Enter the element for pushing....")
        l.push(element)
    elif(u_in == "POP"):
        l.pop()
    else:
        print("Enter valid input")
    inp = input("do u wish to continue: enter Y for continue")
