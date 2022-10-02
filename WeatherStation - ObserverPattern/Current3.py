from WeatherData import *
from interface.Interface import *

class Current3(Observer, DisplayElement):

    def __init__(self, WeatherData):
        self.weatherData = WeatherData
        self.weatherData.registerObserve(self)

    def update(self, temp, humidity, pressure):
        self.temperature = temp
        self.humidity = humidity
        self.pressure = pressure

        self.display()


    def display(self):
        print("Current3의  현재 상태: 온도 " + str(self.temperature) + " 습도 " + str(self.humidity) + "기압 " + str(self.pressure))


