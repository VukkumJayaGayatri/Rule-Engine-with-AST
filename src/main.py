from flask import Flask, request, jsonify
from rule_engine.rule_manager import create_rule, combine_rules, evaluate_rule

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    rule_string = request.json.get('rule_string')
    rule_node = create_rule(rule_string)
    return jsonify(rule_node.to_dict()), 201

@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    rules = request.json.get('rules')
    combined_rule_node = combine_rules(rules)
    return jsonify(combined_rule_node.to_dict()), 201

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    rule_json = request.json.get('rule_json')
    data = request.json.get('data')
    result = evaluate_rule(rule_json, data)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
