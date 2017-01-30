class KinderGarten:
    #initialize the Veriable
    def __init__(self, name):
        self.flag = 0
        self.error = "Name not found...."
        self.name = name
        self.namelist=[ "Alice","Bob", "Charlie", "David","Eve", "Fred", "Ginny", "Harriet","Ileana", "Joseph", "Kincaid"," Larry"]
        self.plant1=["Violets","Radishes","Clover","Grass","Violets","Violets","Radishes","Violets","Clover","Grass","Grass",
            "Clover","Clover","Grass","Violets","Radishes","Grass","Clover","Violets","Clover","Grass","Clover","Grass","Violets"]
        self.plant2=["Violets","Radishes","Clover","Clover","Clover","Grass","Clover","Radishes","Radishes","Grass","Violets",
            "Clover","Grass","Clover","Radishes","Violets","Violets","Clover","Violets","Grass","Clover","Grass","Clover","Violets"]
        self.result = []

    #Calculate the data and Get Plant Accouding to Name
    def calculate_data(self):
        for i in range(0,len(self.namelist)) :
            if(self.namelist[i] != self.name) :
                self.flag = 1
            else :
                self.result.append(self.plant1[i*2])
                self.result.append(self.plant1[(i*2)+1])
                self.result.append(self.plant2[i*2])
                self.result.append(self.plant2[(i*2)+1])
                self.flag = 0
                break

        if(self.flag == 0) :
            return (self.result)
        else :
            return (self.error)

if __name__ == "__main__":
    enter_Name = input("Enter Name : ")
    obj = KinderGarten(enter_Name)
    print (obj.calculate_data())
