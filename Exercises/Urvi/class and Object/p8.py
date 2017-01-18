class kindergarten:

    def __init__(self):
        self.nm=[ "Alice","Bob", "Charlie", "David","Eve", "Fred", "Ginny", "Harriet","Ileana", "Joseph", "Kincaid"," Larry"];
        self.p1=["Violets","Radishes","Clover","Grass","Violets","Violets","Radishes","Violets","Clover","Grass","Grass",
            "Clover","Clover","Grass","Violets","Radishes","Grass","Clover","Violets","Clover","Grass","Clover","Grass","Violets"];
        self.p2=["Violets","Radishes","Clover","Clover","Clover","Grass","Clover","Radishes","Radishes","Grass","Violets",
            "Clover","Grass","Clover","Radishes","Violets","Violets","Clover","Violets","Grass","Clover","Grass","Clover","Violets"]
        self.flag = 0
        self.ans = []

    def cal_plant(self,name):
        #print(name)
        for i in range(0,len(self.nm)):
            if(self.nm[i] != name):
                self.flag = 1
            else:
                self.ans.append(self.p1[i*2])
                self.ans.append(self.p1[(i*2)+1])
                self.ans.append(self.p2[i*2])
                self.ans.append(self.p2[(i*2)+1])
                self.flag = 0
                break

        if(self.flag == 0):
            print(name," have these plant: ",self.ans)
        else:
            print("Name not found... ")

k = kindergarten()
k.cal_plant(input("Enter name of kid: "))
