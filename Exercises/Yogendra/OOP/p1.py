class MyClass:
     def get_String(self,str):
         self.name=str

     def print_String(self):
         return(self.name)

if __name__=="__main__":
    str1=input("enter a string: ")
    myc=MyClass()
    myc.get_String(str1)
    print(myc.print_String())
