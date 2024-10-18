# src/rule_engine/evaluator.py
from .ast import Node

def evaluate_rule(node: Node, data: dict) -> bool:
    if node.type == "operand":
        # Handle simple comparisons (e.g., "age > 30")
        field, condition = node.value.split(" ")
        field_value = data.get(field, None)
        # Example comparison handling (e.g., ">", "<")
        if condition == ">":
            return field_value > int(condition[1:])
        elif condition == "<":
            return field_value < int(condition[1:])
        elif condition == "=":
            return field_value == condition[2:].strip("'")
    elif node.type == "operator":
        left_eval = evaluate_rule(node.left, data)
        right_eval = evaluate_rule(node.right, data)
        if node.value == "AND":
            return left_eval and right_eval
        elif node.value == "OR":
            return left_eval or right_eval
    return False
