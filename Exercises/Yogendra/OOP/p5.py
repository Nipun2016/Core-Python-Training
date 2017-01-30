class Student:
      def __init__(self,nm,rno):
          self.nm=nm
          self.rno=rno
      def get_details(self):
            return self.nm,self.rno	     
           
def sort(lst):
        lst.sort()
        return(lst) 




if __name__=="__main__":
    lst=[]
    
    ch='y'
    while ch=='y':
        name=input("enter student name: ")
        roll_no=input("enter student roll_no: ")
        #lst.append((name,roll_no))
        stud=Student(name,roll_no)
        lst.append((stud.get_details()))
        #lst.append((stud))
        #lst.append((stud.name,stud.roll_no))
        #stud.get_details(lst) 
        ch=input("do u wish to continue: enter y for continue")
    print(lst)
    print(sort(lst))

        


