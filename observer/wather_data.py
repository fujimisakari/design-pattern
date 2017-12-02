from .subject_interface import SubjectInterface


class WeatherData(SubjectInterface):

    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        observers = []
        for o in self.observers:
            if o == observer:
                continue
            observers.append(o)
        self.observers = observers

    def notify_observers(self):
        for o in self.observers:
            o.update(self.temperature, self.humidity, self.pressure)

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self._measurements_changed()

    def _measurements_changed(self):
        self.notify_observers()
