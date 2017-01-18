class Stack:
    def __init__(self):
        self.items = []
        print("\nList size is: ",len(self.items))
    def isEmpty(self):
        print("\nList is: ",self.items)
        return self.items == []

    def push(self, item):
        self.items.append(item)
        print("\nList is: ",self.items)

    def pop(self):
        return self.items.pop()
        print("\nList is: ",self.items)

    def size(self):
        return len(self.items)
        print(len(self.items))

    def print(self):
        print("\nList is: ",self.items)
s=Stack()
while True:
    choice=int(input('\nEnter your choice: \n1.Push\n2.Pop\n3.print list\n4.exit\n'))
    if choice==1:
        if s.isEmpty():
            print('\nStack Empty!!!!')
        i=int(input('\nEnter value in stack: '))
        s.push(i)
    if choice==2:
        if s.isEmpty():
            print('\nStack Empty!!!!')
            break
        print("\npoped item is:",s.pop())
    if choice==4:
        exit()
    if choice==3:
        s.print()

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