from abc import ABCMeta, abstractmethod
class Polygone:

    __metaclass__ = ABCMeta
    def __init__(self):
        self.n = int(input("Enter the number of sides"))
        self.list_size = [int(a) for a in input('Enter size of sides: ').split()]

    @abstractmethod
    def compute_Area(self):
        """Abstract method"""
        return
