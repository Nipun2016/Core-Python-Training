class Basic(object):
    #initialize the variables
    def __init__(self, arg):
        self.arg = arg

    #Print the variable of Class
    def print_data(self):
        return self.arg.upper()

#takes input from User
word = input("Enter String : ")
obj = Basic(word)
print (obj.print_data())
