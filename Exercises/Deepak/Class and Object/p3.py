from itertools import combinations

class CalculateSum(object):
    #initialize the variables
    def __init__(self, listVariable):
        self.listVariable = listVariable
        #print (self.listVariable)

    #find variable by calculate the sum
    def getAnswer(self):
        finalAnswer = []
        for var in combinations(self.listVariable, 3):
            if (var[0] + var[1] + var[2] == 0):
                finalAnswer.append([var[0], var[1], var[2]])
        return (finalAnswer)

if __name__ == "__main__":
    try:
        #takes input from User
        obj = CalculateSum(([float(x) for x in input("Enter Value to list :").split()]))
        if len(obj.listVariable) != 0 :
            print (obj.getAnswer())
        else:
            raise ValueError()
    except ValueError:
        print ("Please Insert Digit only.")
