from collections import Counter

class WeatherProcessor:
    @staticmethod
    def calculate_daily_summary(data):
        temperatures = [d['temperature'] for d in data]
        conditions = [d['condition'] for d in data]
        
        return {
            'average_temp': sum(temperatures) / len(temperatures),
            'max_temp': max(temperatures),
            'min_temp': min(temperatures),
            'dominant_condition': Counter(conditions).most_common(1)[0][0]
        }

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15
