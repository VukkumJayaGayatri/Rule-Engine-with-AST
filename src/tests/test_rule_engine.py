# tests/test_rule_engine.py
import unittest
from src.rule_engine.rule_combiner import create_rule, combine_rules
from src.rule_engine.evaluator import evaluate_rule
from src.rule_engine.ast import Node

class TestRuleEngine(unittest.TestCase):
    
    def test_create_rule(self):
        rule = "age > 30"
        ast = create_rule(rule)
        self.assertEqual(ast.type, "operand")
        self.assertEqual(ast.value, "age > 30")
        
    def test_combine_rules(self):
        rules = ["age > 30", "salary > 50000"]
        combined = combine_rules(rules)
        self.assertEqual(combined.type, "operator")
        self.assertEqual(combined.value, "AND")

    def test_evaluate_rule(self):
        node = Node(type="operator", left=Node(type="operand", value="age > 30"), 
                     right=Node(type="operand", value="salary > 50000"), value="AND")
        data = {"age": 31, "salary": 60000}
        result = evaluate_rule(node, data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
