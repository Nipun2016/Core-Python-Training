class Student:

    #var initialization
    def __init__(self):
        self.data = []
        self.data = "".join(a for a in input("Enter student Entry")).split()
        self.lst_data = []
        print("Student called")
    #sorting function
    def sorting_data(self):
        for i in range(0,len(self.data)-1,2):
            self.lst_data.append([self.data[i],self.data[i+1]])
        print(sorted(self.lst_data))

s = Student()
s.sorting_data()
