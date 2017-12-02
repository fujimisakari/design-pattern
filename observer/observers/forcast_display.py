from .desplay_interface import DisplayInterface
from .observer_interface import ObserverInterface


class ForecastDisplay(ObserverInterface, DisplayInterface):

    def __init__(self, weather_data):
        weather_data.register_observer(self)
        self.weather_data = weather_data
        self.current_pressure = 29.92
        self.last_pressure = 0

    def update(self, temperature, humidity, pressure):
        self.last_pressure = self.current_pressure
        self.current_pressure = pressure
        # self.display()

    def get_display_message(self):
        msg = None
        if self.current_pressure > self.last_pressure:
            msg = '天候が回復しそう'
        elif self.current_pressure == self.last_pressure:
            msg = '天候に変化はなさそう'
        elif self.current_pressure < self.last_pressure:
            msg = '天候が崩れるので、ご注意を'
        return '予想: {}'.format(msg)

    def display(self):
        print(self.get_display_message())
