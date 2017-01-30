from abc import ABCMeta, abstractmethod

class Polygon(object):

    __metaclass__ = ABCMeta
    def __init__(self,sides,list_size):
        self.sides = sides
        self.list_size = list_size

    @abstractmethod
    def get_area(self):
        pass
