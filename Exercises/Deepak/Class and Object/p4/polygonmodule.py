from abc import ABCMeta, abstractmethod

class Polygon(object):

    __metaclass__ = ABCMeta
    def __init__(self):
        #self.sides = int(input("Enter The Number Of Sides : "))
        self.list_size = [int(a) for a in input("Enter Value : ").split()]

    @abstractmethod
    def get_area(self):
        #print ("Deepak")
        pass
