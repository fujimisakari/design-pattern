import unittest

from .observers.current_conditions_display import CurrentConditionsDisplay
from .observers.forcast_display import ForecastDisplay
from .observers.statistics_display import StatisticsDisplay
from .wather_data import WeatherData


class ObserverTest(unittest.TestCase):

    def setUp(self):
        self.weather_data = WeatherData()

    def test_current_conditions_display(self):
        current_display = CurrentConditionsDisplay(self.weather_data)
        self.weather_data.set_measurements(28, 65, 30.4)
        self.assertEqual('現在の気象状況: 温度28度 湿度65%', current_display.get_display_message())

    def test_statistics_display(self):
        statistics_display = StatisticsDisplay(self.weather_data)
        self.weather_data.set_measurements(28, 65, 30.4)
        self.weather_data.set_measurements(32, 60, 30.4)
        self.assertEqual('現在の温度統計: 最高32度 最低28度 平均30.0度', statistics_display.get_display_message())

    def test_forcast_display(self):
        forecast_display = ForecastDisplay(self.weather_data)
        self.weather_data.set_measurements(28, 65, 30.4)
        self.assertEqual('予想: 天候が回復しそう', forecast_display.get_display_message())
        self.weather_data.set_measurements(28, 65, 10.4)
        self.assertEqual('予想: 天候が崩れるので、ご注意を', forecast_display.get_display_message())


if __name__ == '__main__':
    unittest.main()
