from abc import abstractmethod, ABCMeta

class FlyBehavior(metaclass=ABCMeta):

    @abstractmethod
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):

    def fly(self):
        print("날고 있어요.!!!!")

class FlyNoWing(FlyBehavior):

    def fly(self):
        print("저는 못날아요")


