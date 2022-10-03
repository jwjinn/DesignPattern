
from Beverage import *
from Coffee import *
from Mocha import *

if __name__ == "__main__":

    beverage = HouseBlend()
    beverage = Mocha(beverage)
    print(beverage.getDescription())
    print(beverage.cost())

    beverage1 = Espresso()
    beverage1 = Mocha(beverage1)
    beverage1 = Mocha(beverage1)
    print(beverage1.getDescription())
    print(beverage1.cost())

    '''
    beverage = Espresso()
    print(Beverage.getDescription(beverage) + " $" + str(beverage.cost()))

    print("------------------")

    beverage1 = Espresso()
    beverage1 = Mocha(beverage1)
    beverage1 = Mocha(beverage1)

    print(beverage1.getDescription() + " S" + str(beverage1.cost()))

    beverage2 = HouseBlend()
    beverage2 = Mocha(beverage2)

    print(beverage2.getDescription() + " S" + str(beverage2.cost()))
    '''






