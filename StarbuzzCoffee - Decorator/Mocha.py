
from CondimentDecorator import *
from Beverage import *

class Mocha(CondimentDecorator):

    #def __init__(self, Beverage):
    #   self.beverage =Beverage
    
    def __init__(self, Beverage):
        super(Mocha, self).__init__(Beverage)


    def getDescription(self):
        return self.beverage.getDescription() + ", 모카"

    def cost(self):
        return self.beverage.cost() + 0.2

