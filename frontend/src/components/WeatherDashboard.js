import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';

function WeatherDashboard() {
  const [weatherData, setWeatherData] = useState([]);
  const [summary, setSummary] = useState(null);

  useEffect(() => {
    fetchWeatherData();
    fetchWeatherSummary();
  }, []);

  const fetchWeatherData = async () => {
    const response = await fetch('http://localhost:5000/api/weather');
    const data = await response.json();
    setWeatherData(data);
  };

  const fetchWeatherSummary = async () => {
    const response = await fetch('http://localhost:5000/api/weather/summary');
    const data = await response.json();
    setSummary(data);
  };

  const chartData = {
    labels: weatherData.map(d => d.date),
    datasets: [
      {
        label: 'Temperature',
        data: weatherData.map(d => d.temperature),
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
      }
    ]
  };
