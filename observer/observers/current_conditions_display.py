from .desplay_interface import DisplayInterface
from .observer_interface import ObserverInterface


class CurrentConditionsDisplay(ObserverInterface, DisplayInterface):

    def __init__(self, weatherData):
        weatherData.register_observer(self)
        self.weatherData = weatherData
        self.temperature = 0
        self.humidity = 0

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        # self.display()

    def get_display_message(self):
        return '現在の気象状況: 温度{}度 湿度{}%'.format(self.temperature, self.humidity)

    def display(self):
        print(self.get_display_message())
