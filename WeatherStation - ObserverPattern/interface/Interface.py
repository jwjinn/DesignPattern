from abc import abstractmethod, ABCMeta

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, temp, humidity, pressure):

        print("update 작동중")
        pass

class Subject(metaclass=ABCMeta):

    @abstractmethod
    def registerObserve(self, Observer):
        pass

    @abstractmethod
    def removeObserver(self, Observer):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass


class DisplayElement(metaclass=ABCMeta):

    @abstractmethod
    def display(self):
        pass
