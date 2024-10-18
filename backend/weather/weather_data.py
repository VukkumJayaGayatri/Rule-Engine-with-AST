import random
from datetime import datetime, timedelta

class WeatherData:
    def __init__(self):
        self.data = []

    def generate_mock_data(self, days=30):
        start_date = datetime.now() - timedelta(days=days)
        for i in range(days):
            date = start_date + timedelta(days=i)
            self.data.append({
                'date': date.strftime('%Y-%m-%d'),
                'temperature': round(random.uniform(-10, 40), 2),
                'humidity': round(random.uniform(0, 100), 2),
                'pressure': round(random.uniform(950, 1050), 2),
                'condition': random.choice(['Sunny', 'Cloudy', 'Rainy', 'Snowy'])
            })

    def get_data(self, start_date=None, end_date=None):
        if start_date and end_date:
            return [d for d in self.data if start_date <= d['date'] <= end_date]
        return self.data
