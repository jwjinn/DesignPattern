from Beverage import *

class CondimentDecorator(Beverage):

    def __init__(self, Beverage):
        self.beverage = Beverage

    @abstractmethod
    def getDescription(self):
        pass