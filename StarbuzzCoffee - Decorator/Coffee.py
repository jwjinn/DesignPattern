from Beverage import *

class Espresso(Beverage):

    def __init__(self):
        super(Espresso, self).__init__("Espresso")

    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        super(HouseBlend, self).__init__("HouseBlend")


    def cost(self):
        return 0.89

