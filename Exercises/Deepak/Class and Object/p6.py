class Calculate_obj:
    #iniitialize class variable
    i = 0

    #iniitialize an Constructor
    def __init__(self):
        Calculate_obj.i += 1 #class var accessed by classname rather than object
        print ("Object Number :" , Calculate_obj.i)

if __name__ == "__main__":
    first = Calculate_obj()
    second = Calculate_obj()
    third = Calculate_obj()
    Forth = Calculate_obj()
