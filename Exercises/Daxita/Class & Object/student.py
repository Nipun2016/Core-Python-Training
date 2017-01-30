# class student:
# 	def __init__(self,no,name):
# 		self.no=no
# 		self.name=name
# if __name__=="__main__":
# 	d={}
# 	try:
# 		n=int(input('Enter no how many students you want to add in list: '))
# 		for i in range(0,n):
# 			n=int(input('Enter your roll no: '))
# 			your_name=input('Enter ypur name: ')
# 			s=student(n,your_name)
# 			d[n]=your_name
# 		for key in sorted(d):
# 		    return (key, d[key])
# 	except ValueError:
# 		print("Value error")

class student:
    def __init__(self,data):
        self.final = data
        self.final1 = []

    def print(self):
        for i in range(0,len(self.final)-1,2):
            self.final1.append([self.final[i],self.final[i+1]])
        return (sorted(self.final1))

if __name__ == "__main__":
    try:
        total_student = int(input("Enter Number of Student : "))
        list_student = []
        while total_student>0 :
            student_number = int(input("Enter Enrollment Number : "))
            student_name = input("Enter Name : ")
            if len(student_name) == 0:
                print("please Enter name")
            total_student -= 1
            list_student.append(student_number)
            list_student.append(student_name)

            obj = Student(list_student)
            print (obj.print())
    except Exception:
        print("Enter Valid Input.")