import unittest
from unittest.mock import patch
from weather_app import WeatherAPI, MockWeather, WeatherHandler, ServiceFactory 

class WeatherTesting(unittest.TestCase):
    def test_weatherapi(self):
        service = WeatherAPI()
        handler = WeatherHandler(service)
        data = handler.get_weather_data()
        self.assertIsNotNone(data)

    @patch('requests.get')
    def test_weatherapi_invalid_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {}

        service = WeatherAPI()
        handler = WeatherHandler(service)
        data = handler.get_weather_data()
        self.assertIsNone(data)

    
    def test_mockweather(self):
        service = MockWeather()
        handler = WeatherHandler(service)
        data = handler.get_weather_data()
        
        expected_data = {"temp": 25, "humidity": 50}
        self.assertEqual(data, expected_data)

    def test_handler_invalid_data(self):
        service = MockWeather()
        handler = WeatherHandler(service)
        service.mock_data = {}
        data = handler.get_weather_data()
        self.assertIsNone(data)

if __name__ == "__main__":
    unittest.main()
