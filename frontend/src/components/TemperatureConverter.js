import React, { useState } from 'react';
import axios from 'axios';

const TemperatureConverter = () => {
    const [value, setValue] = useState('');
    const [fromUnit, setFromUnit] = useState('celsius');
    const [toUnit, setToUnit] = useState('fahrenheit');
    const [result, setResult] = useState(null);
    const [error, setError] = useState('');

    const handleConvert = async () => {
        try {
            const response = await axios.post('http://localhost:5000/api/temperature/convert', {
                value: parseFloat(value),
                from: fromUnit,
                to: toUnit
            });
            setResult(response.data.result);
            setError('');
        } catch (err) {
            setError('Invalid conversion');
            setResult(null);
        }
    };

    return (
        <div>
            <h2>Temperature Converter</h2>
            <input
                type="number"
                value={value}
                onChange={(e) => setValue(e.target.value)}
                placeholder="Enter temperature"
            />
            <select value={fromUnit} onChange={(e) => setFromUnit(e.target.value)}>
                <option value="celsius">Celsius</option>
                <option value="fahrenheit">Fahrenheit</option>
                <option value="kelvin">Kelvin</option>
            </select>
            <span> to </span>
            <select value={toUnit} onChange={(e) => setToUnit(e.target.value)}>
                <option value="celsius">Celsius</option>
                <option value="fahrenheit">Fahrenheit</option>
                <option value="kelvin">Kelvin</option>
            </select>
            <button onClick={handleConvert}>Convert</button>
            {result && <div>Result: {result} {toUnit.charAt(0).toUpperCase() + toUnit.slice(1)}</div>}
            {error && <div>{error}</div>}
        </div>
    );
};

export default TemperatureConverter;
