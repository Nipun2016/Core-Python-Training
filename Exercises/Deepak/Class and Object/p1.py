class Basic(object):
    #initialize the variables
    def __init__():
        print("Constructor Called...")
        
    #get Data From User
    def get_String(self, arg):
        self.arg = arg

    #Print the variable of Class
    def print_String(self):
        return self.arg.upper()

obj = Basic(word)
#takes input from User
word = input("Enter String : ")
obj.get_String(word)
print (obj.print_String())
