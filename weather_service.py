import requests
import os
import logging
from typing import Dict, Optional

class WeatherService:
    """Service to fetch weather data from OpenWeather API"""
    
    def __init__(self):
        self.api_key = os.environ.get("OPENWEATHER_API_KEY", "demo_key")
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def get_weather_data(self, location: str) -> Optional[Dict]:
        """Fetch current weather data for a location"""
        try:
            params = {
                'q': location,
                'appid': self.api_key,
                'units': 'metric'
            }
            
            response = requests.get(self.base_url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                # Extract relevant weather information
                weather_data = {
                    'location': data['name'],
                    'country': data['sys']['country'],
                    'temp': data['main']['temp'],
                    'feels_like': data['main']['feels_like'],
                    'temp_min': data['main']['temp_min'],
                    'temp_max': data['main']['temp_max'],
                    'humidity': data['main']['humidity'],
                    'pressure': data['main']['pressure'],
                    'weather': data['weather'][0]['description'],
                    'weather_main': data['weather'][0]['main'],
                    'wind_speed': data['wind'].get('speed', 0),
                    'clouds': data['clouds']['all'],
                    'visibility': data.get('visibility', 10000),
                    'sunrise': data['sys']['sunrise'],
                    'sunset': data['sys']['sunset'],
                    'timezone': data['timezone']
                }
                
                logging.info(f"Weather data fetched successfully for {location}")
                return weather_data
                
            elif response.status_code == 401:
                logging.error("Invalid OpenWeather API key")
                return self._get_default_weather_data(location)
                
            elif response.status_code == 404:
                logging.error(f"Location '{location}' not found")
                return None
                
            else:
                logging.error(f"Weather API error: {response.status_code}")
                return self._get_default_weather_data(location)
                
        except requests.exceptions.RequestException as e:
            logging.error(f"Network error fetching weather data: {str(e)}")
            return self._get_default_weather_data(location)
            
        except Exception as e:
            logging.error(f"Error fetching weather data: {str(e)}")
            return self._get_default_weather_data(location)
    
    def _get_default_weather_data(self, location: str) -> Dict:
        """Return default weather data when API is unavailable"""
        return {
            'location': location,
            'country': 'Unknown',
            'temp': 22.0,
            'feels_like': 22.0,
            'temp_min': 18.0,
            'temp_max': 26.0,
            'humidity': 65,
            'pressure': 1013,
            'weather': 'clear sky',
            'weather_main': 'Clear',
            'wind_speed': 3.5,
            'clouds': 20,
            'visibility': 10000,
            'sunrise': 1692681600,  # Example timestamp
            'sunset': 1692728400,   # Example timestamp
            'timezone': 0,
            'is_default': True  # Flag to indicate this is default data
        }
    
    def get_climate_recommendations(self, weather_data: Dict) -> Dict:
        """Get climate-based farming recommendations"""
        temp = weather_data['temp']
        humidity = weather_data['humidity']
        
        recommendations = {
            'climate_suitability': self._assess_climate_suitability(temp, humidity),
            'growing_conditions': self._get_growing_conditions(temp, humidity),
            'seasonal_advice': self._get_seasonal_advice(weather_data),
            'risk_factors': self._identify_risk_factors(weather_data)
        }
        
        return recommendations
    
    def _assess_climate_suitability(self, temp: float, humidity: int) -> str:
        """Assess overall climate suitability for vertical farming"""
        if 18 <= temp <= 26 and 50 <= humidity <= 70:
            return 'Excellent'
        elif 15 <= temp <= 30 and 40 <= humidity <= 80:
            return 'Good'
        elif 10 <= temp <= 35 and 30 <= humidity <= 90:
            return 'Fair'
        else:
            return 'Challenging'
    
    def _get_growing_conditions(self, temp: float, humidity: int) -> Dict:
        """Get specific growing condition recommendations"""
        conditions = {
            'heating_needed': temp < 18,
            'cooling_needed': temp > 26,
            'dehumidification_needed': humidity > 70,
            'humidification_needed': humidity < 50,
            'ventilation_priority': 'high' if humidity > 75 or temp > 28 else 'medium'
        }
        
        return conditions
    
    def _get_seasonal_advice(self, weather_data: Dict) -> str:
        """Provide seasonal farming advice"""
        temp = weather_data['temp']
        weather_main = weather_data['weather_main'].lower()
        
        if temp < 15:
            return "Consider cold-hardy crops like lettuce, spinach, and kale. Increase heating systems."
        elif temp > 30:
            return "Focus on heat-tolerant crops. Ensure adequate cooling and ventilation."
        elif 'rain' in weather_main:
            return "Excellent conditions for leafy greens. Monitor humidity levels carefully."
        else:
            return "Ideal conditions for most vertical farming crops. Maintain current parameters."
    
    def _identify_risk_factors(self, weather_data: Dict) -> list:
        """Identify potential risk factors based on weather"""
        risks = []
        
        temp = weather_data['temp']
        humidity = weather_data['humidity']
        wind_speed = weather_data['wind_speed']
        
        if temp > 35:
            risks.append("Extreme heat - risk of crop stress and increased cooling costs")
        elif temp < 5:
            risks.append("Freezing temperatures - risk of crop damage and high heating costs")
        
        if humidity > 85:
            risks.append("Very high humidity - increased risk of fungal diseases")
        elif humidity < 30:
            risks.append("Low humidity - risk of plant dehydration")
        
        if wind_speed > 15:
            risks.append("High winds - potential structural stress on facilities")
        
        return risks

# Global weather service instance
weather_service = WeatherService()
