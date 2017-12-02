from .desplay_interface import DisplayInterface
from .observer_interface import ObserverInterface


class StatisticsDisplay(ObserverInterface, DisplayInterface):

    def __init__(self, weatherData):
        weatherData.register_observer(self)
        self.weatherData = weatherData
        self.max_temp = 0.0
        self.min_temp = 15
        self.temp_sum = 0.0
        self.num_readings = 0

    def update(self, temperature, humidity, pressure):
        self.temp_sum += temperature
        self.num_readings += 1

        if self.max_temp:
            if temperature > self.max_temp:
                self.max_temp = temperature

            if temperature < self.min_temp:
                self.min_temp = temperature
        else:
            self.max_temp = temperature
            self.min_temp = temperature

        # self.display()

    def get_display_message(self):
        return '現在の温度統計: 最高{}度 最低{}度 平均{}度'.format(self.max_temp, self.min_temp, (self.temp_sum / self.num_readings))

    def display(self):
        print(self.get_display_message())
