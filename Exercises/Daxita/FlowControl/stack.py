class Stack:
    def __init__(self,sz):
        self.items = []
        self.sz=sz
        print("\nList size is: ",len(self.items))

    def isEmpty(self):
        print("\nList is: ",self.items)
        return self.items == []

    def push(self, item):
        
        if (len(self.items)>=self.sz):
            print("\nStack overflow!!")
        else:
            self.items.append(item)
        return len(self.items)
        #print("\nList is: ",self.items)

    def pop(self):
        if(self.items == []):
            return ("Stack Empty!!!!")
        return self.items.pop()
        #print("\nList is: ",self.items)

    def size(self):
        return len(self.items)
        #print(len(self.items))

    def print(self):
        #print("\nList is: ",self.items)
        return self.items
if __name__=="__main__":
    sz=int(input("Enter size of stack: "))
    s=Stack(sz)
    while True:
        try:
            choice=int(input('\nEnter your choice: \n1.Push\n2.Pop\n3.print list\n4.exit\n'))
            if choice==1:
                try:
                    if s.isEmpty():
                        print('\nStack Empty!!!!')
                    i=int(input('\nEnter value in stack: '))
                    s.push(i)
                    #print(len(s))
                except ValueError:
                    print("Please enter valid input")
            if choice==2:
                if s.isEmpty():
                    print('\nStack Empty!!!!')
                    break
                print("\npoped item is:",s.pop())
            if choice==4:
                exit()
            if choice==3:
                print(s.print())
        except ValueError:
            print ("Value Error...Please Enter Above Choice")

# print("stack is empty or not: ",s.isEmpty())
# s.push(4)
# s.push('dog')
# s.push(True)
# print("Size of Stack: ",s.size())
# print("Stack empty or not: ",s.isEmpty())
# s.push(8.4)
# print("Poped item is: ",s.pop())
# print("Poped item is:",s.pop())
# print("Size of Stack is: ",s.size())