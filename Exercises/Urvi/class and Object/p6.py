
class Cal_obj:
    #class var i
    i = 0

    #iniitialize an instance
    def __init__(self):
        Cal_obj.i += 1 #class var accessed by classname rather than object
        print("New Object created and total object is:",Cal_obj.i)
c = Cal_obj()

s = Cal_obj()

t = Cal_obj()
