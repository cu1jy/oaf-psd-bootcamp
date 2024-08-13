import requests

# api calling service
class WeatherAPI:
    def __init__(self) -> None:
        self.api_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,relative_humidity_2m&forecast_days=1"
    
    def call_endpoint(self):
        try: 
            response = requests.get(self.api_url)
            response.raise_for_status()
            return self.validate_data(response.json())
        except requests.exceptions.RequestException as e:
            print(f"Error calling API: {e}")
            return None
    
    def validate_data(self, data):
        if "hourly" in data:
            time_data = data["hourly"]["time"]
            temperature_data = data["hourly"]["temperature_2m"]
            humidity_data = data["hourly"]["relative_humidity_2m"]

            parsed_data = [
                {
                    "time": time,
                    "temperature": temp,
                    "humidity": humidity
                }
                for time, temp, humidity in zip(time_data, temperature_data, humidity_data)
            ]
            return parsed_data
        else:
            print("Invalid data received")
            return None

# mocked data service
class MockWeather:
    def __init__(self):
        self.mock_data = {
            "temperature": 25,
            "humidity": 50
        }
    
    def generate_data(self):
        return self.mock_data
    
# data source handler - doesn't care about how data was retrieved - getTemp or getHumidity
class WeatherHandler:
    def __init__(self, service) -> None:
        self.service = service

    def get_weather_data(self):
        if isinstance(self.service, WeatherAPI):
            self.data = self.service.call_endpoint()
        else:
            self.data = self.service.generate_data()
        return self.verify_data(self.data)
    
    def verify_data(self, data):
        if(data):
            print("Data verified")
            return data
        else:
            print("Data verification failed")
            return None 
    
    def get_temp(self):
        self.get_weather_data()
        if isinstance(self.data, list):
            temperatures = [entry["temperature"] for entry in self.data]
            return temperatures
        elif isinstance(self.data, dict) and "temperature" in self.data:
            return self.data["temperature"]
        else:
            print("Temperature data not available")
            return None
        
    def get_humidity(self):
        self.get_weather_data()
        if isinstance(self.data, list):
            humidities = [entry["humidity"] for entry in self.data]
            return humidities
        elif isinstance(self.data, dict) and "humidity" in self.data:
            return self.data["humidity"]
        else:
            print("Humidity data not available")
            return None

# creates services
class ServiceFactory:
    @staticmethod
    def create_api_service():
        return WeatherAPI
    
    @staticmethod
    def create_mock_service():
        return MockWeather

