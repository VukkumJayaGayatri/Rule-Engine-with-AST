import React from 'react';
import WeatherDashboard from './components/WeatherDashboard';
import TemperatureConverter from './components/TemperatureConverter';
import AlertConfig from './components/AlertConfig';

function App() {
  return (
    <div className="App">
      <h1>Weather Rule Engine</h1>
      <WeatherDashboard />
      <TemperatureConverter />
      <AlertConfig />
    </div>
  );
}

export default App;
