class stringdemo:

    def __init__(self):
        print("stringdemo called")

    def get_String(self,name):
        self.name = name

    def print_String(self):
        print(self.name.upper())

s = stringdemo()
s.get_String(input("Enter the string "))
s.print_String()
