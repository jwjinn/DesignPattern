from WeatherData import *
from CurrentConditionDisplay import *
from Current3 import *

if __name__ == "__main__":

    weatherData = WeatherData()

    currentDisplay = CurrentConditionsDisplay(weatherData)
    current3 = Current3(weatherData)


    weatherData.setMeasurements(80, 65, 30.4)
    weatherData.setMeasurements(82, 70, 29.2)

    currentDisplay.disconnect()

    weatherData.setMeasurements(82, 70, 29.2)



