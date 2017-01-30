class Basic(object):
    #get Data From User
    def get_String(self, arg):
        self.arg = arg

    #Print the variable of Class
    def print_String(self):
        return self.arg.upper()

    def valid_input(self,word):
        self.arg_list = " ".join(self.arg).split()
        for i in self.arg_list:
            if i.isalpha():
                continue
            else:
                return False
        return self.arg

if __name__ == "__main__":
    #takes input from User
    word = input("Enter String : ")
    obj = Basic()
    obj.get_String(word)
    valid_input = obj.valid_input(word)

    if not valid_input:
        print ("Please insert valid input")
    else:
        print (obj.print_String())
