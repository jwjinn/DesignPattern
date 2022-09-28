
from abc import abstractmethod, ABCMeta

from FlyAndQuack.FlyBehavior import *
from FlyAndQuack.QuackBehavior import *




class Duck(metaclass=ABCMeta):

    def setFlyBehavior(self, FlyBehavior):
        self.Flybehavior = FlyBehavior
        #print(self.Flybehavior)

    def PerformBehavior(self):
        print(self.Flybehavior.fly())

    def setQuackBehavior(self, QuackBehavior):
        self.QuackBehavior = QuackBehavior

    def PerformQuack(self):
        print(self.QuackBehavior.quack())

    def swim(self):
        print("오리가 수영합니다.")

    def display(self):
        print(self)

    @abstractmethod
    def display(self):
        pass

class MallardDuck(Duck):

    def display(self):
        print("I'm MallardDuck")

class RedheadDuck(Duck):

    def display(self):
        print("I'm RedheadDuck")

class RubberDuck(Duck):

    def display(self):
        print("I'm RubberDuck")

class DecoyDuck(Duck):

    def display(self):
        print("I'm DecoyDuck")


if __name__ == "__main__":

    mallardDuck = MallardDuck()

    mallardDuck.setQuackBehavior(Quack())
    mallardDuck.setFlyBehavior(FlyWithWings())

    mallardDuck.PerformQuack()
    mallardDuck.PerformBehavior()



