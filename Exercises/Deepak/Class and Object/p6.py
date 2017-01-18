
class Calculate_obj:
    #iniitialize class variable
    i = 0

    #iniitialize an Constructor
    def __init__(self):
        Calculate_obj.i += 1 #class var accessed by classname rather than object
        print("New Object created and total object is:",Cal_obj.i)

first = Calculate_obj()
second = Calculate_obj()
third = Calculate_obj()
Forth = Calculate_obj()
