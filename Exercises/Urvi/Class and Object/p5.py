class Student:
    def __init__(self,input_data):
        self.final = input_data
        self.final1 = []

    def print_data(self):
        for i in range(0,len(self.final)-1,2):
            self.final1.append([self.final[i],self.final[i+1]])
        return (sorted(self.final1))

if __name__ == "__main__":
    try:
        total_student = int(input("Enter Total Number of Student : "))
        list_of_student = []
        while total_student>0 :
            student_number = int(input("Enter Enrollment Number : "))
            student_name = input("Enter Name : ")
            if len(student_name) == 0:
                raise ValueError()
            total_student -= 1
            list_of_student.append(student_number)
            list_of_student.append(student_name)

            #print (list_of_student)
            obj = Student(list_of_student)
            print (obj.print_data())
    except Exception:
        print("Please Insert Valid Input.")
