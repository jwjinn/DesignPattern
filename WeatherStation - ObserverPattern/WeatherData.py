from interface.Interface import *


class WeatherData(Subject):


    def __init__(self):
        self.observer = []

    def notifyObservers(self):
        for k in self.observer:
            k.update(self.temperature, self.humidity, self.pressure)


    def registerObserve(self, Observer):
        self.observer.append(Observer)

    def removeObserver(self, Observer):
        self.observer.remove(Observer)


    def measurementsChanged(self):
        self.notifyObservers()


    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurementsChanged()



