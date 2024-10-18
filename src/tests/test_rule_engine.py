import unittest
from src.rule_engine.rule_manager import create_rule, combine_rules, evaluate_rule

class TestRuleEngine(unittest.TestCase):

    def test_create_rule(self):
        rule_string = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing'))"
        rule_node = create_rule(rule_string)
        self.assertEqual(rule_node.type, 'operator')

    def test_combine_rules(self):
        rules = [
            "((age > 30 AND department = 'Sales'))",
            "((age < 25 AND department = 'Marketing'))"
        ]
        combined_node = combine_rules(rules)
        self.assertEqual(combined_node.type, 'operator')

    def test_evaluate_rule(self):
        # Add sample data and evaluate
        rule_string = "((age > 30 AND department = 'Sales'))"
        rule_node = create_rule(rule_string)
        data = {'age': 35, 'department': 'Sales'}
        result = evaluate_rule(rule_node, data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
