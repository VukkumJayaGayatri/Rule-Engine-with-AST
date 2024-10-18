from flask import Flask, request, jsonify
from flask_cors import CORS
from rule_engine.rule_parser import RuleParser
from rule_engine.evaluator import Evaluator
from weather.weather_data import WeatherData
from weather.weather_processor import WeatherProcessor

app = Flask(__name__)
CORS(app)

weather_data = WeatherData()
weather_data.generate_mock_data()

rule_parser = RuleParser()
evaluator = Evaluator()

@app.route('/api/weather', methods=['GET'])
def get_weather_data():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    data = weather_data.get_data(start_date, end_date)
    return jsonify(data)

@app.route('/api/weather/summary', methods=['GET'])
def get_weather_summary():
    data = weather_data.get_data()
    summary = WeatherProcessor.calculate_daily_summary(data)
    return jsonify(summary)

@app.route('/api/temperature/convert', methods=['POST'])
def convert_temperature():
    data = request.json
    value = data['value']
    from_unit = data['from']
    to_unit = data['to']

    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        result = WeatherProcessor.celsius_to_fahrenheit(value)
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        result = WeatherProcessor.fahrenheit_to_celsius(value)
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        result = WeatherProcessor.celsius_to_kelvin(value)
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        result = WeatherProcessor.kelvin_to_celsius(value)
    else:
        return jsonify({'error': 'Invalid conversion'}), 400

    return jsonify({'result': result})

@app.route('/api/rules/evaluate', methods=['POST'])
def evaluate_rule():
    data = request.json
    rule_string = data['rule']
    weather_data = data['weather_data']

    try:
        ast = rule_parser.parse(rule_string)
        result = evaluator.evaluate(ast, weather_data)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
