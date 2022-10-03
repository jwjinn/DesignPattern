from abc import abstractmethod, ABCMeta

class Beverage(metaclass=ABCMeta):

    def __init__(self, name):
        self.description = name

    def getDescription(self):
        return self.description


    @abstractmethod
    def cost(self):
        pass

