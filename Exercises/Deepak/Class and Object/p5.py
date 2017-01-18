class Student:
    def __init__(self):
        self.final = []
        self.final = "".join(x for x in input("Enter Data : ")).split()
        self.final1 = []
        #print (self.final)

    def print_data(self):
        for i in range(0,len(self.final)-1,2):
            self.final1.append([self.final[i],self.final[i+1]])
        print(sorted(self.final1))

obj = Student()
obj.print_data()
