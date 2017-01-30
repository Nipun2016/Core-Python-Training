class Stack(object):
    def __init__(self,size):
         self.items = []
         self.size = size

    def push(self, item):
         self.items.append(item)
         return len(self.items)

    def pop(self):
         return self.items.pop()

    def stack_size(self):
        return len(self.items)

    def print_stack(self):
        print ("Stack is : " ,self.items)

if __name__ == "__main__":
    cont = "y"
    size_of_stack = int(input("Enter Total size of Stack : "))
    obj = Stack(size_of_stack)
    while cont == "y" :
        user_input = input("What You Want (push/pop/print): ")

        if (user_input == "push") :
            #print (len(obj.items))
            if(len(obj.items) < obj.size) :
                try:
                    element = int(input("Enter Element To Stack : "))
                    obj.push(element)
                except Exception:
                    print ("Please Enter Digit only...")
            else:
                print ("Stack Is Full")
        elif (user_input == "pop") :
            if(len(obj.items) > 0) :
                print ("Removed Element from Stack Is : " , obj.pop())
            else:
                print ("Stack Is Empty")
        elif (user_input == "print") :
            obj.print_stack()
        else:
            print ("Please Insert Valid Input...!!")

        cont = input("Do You want to Continue (y/n) : ")
