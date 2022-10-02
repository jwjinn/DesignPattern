
from WeatherData import *
from interface.Interface import *

class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, WeatherData):
        self.weatherData = WeatherData
        self.weatherData.registerObserve(self)

    def update(self, temp, humidity, pressure):
        self.temperature = temp
        self.humidity = humidity

        self.display()


    def disconnect(self):
        print("CurrentConditionsDisplay - observer와의 관계를 청산하겠습니다.")
        self.weatherData.removeObserver(self)


    def display(self):
        print("CurrentConditoin의 현재 상태: 온도 " + str(self.temperature) + " 습도 " + str(self.humidity))
