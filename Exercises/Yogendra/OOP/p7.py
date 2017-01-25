class Stack:
      def __init__(self,op,max_stack_age,stack,ele=""):
          self.op=op
          self.size=max_stack_age
          self.stk=stack
          self.ele=ele
      def stack_update(self):
          if self.op==0:
             if(len(self.stk)!=0):
                   self.stk.pop()
                   return self.stk
             else:
                   print("stack is empty")
                   return False
          elif self.op==1:
             if(len(self.stk)<self.size):
                   self.stk.append(self.ele)
                   return self.stk

             else:
                   return "stack is full"


if __name__=="__main__":
   stack=[]
   ch='y'

   while ch=='y':
       op=int(input("enter 0 for pop and 1 for push: "))
       b=1
       max_stack_age=5
    
       print(type(stack))
    
       if op==0:
            stk1=Stack(op,max_stack_age,stack,b)
            print(stk1.stack_update())
            ch=input("do u want to continue")
       elif op==1:
            ele=input("enter element u want to push")
            stk1=Stack(op,max_stack_age,stack,ele)
            print(stk1.stack_update())
            ch=input("do u want to continue")
       else:
            print("wrong input")
            ch=input("do u want to continue")

