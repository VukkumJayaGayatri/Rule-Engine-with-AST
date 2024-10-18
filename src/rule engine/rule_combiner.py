# src/rule_engine/rule_combiner.py
from .ast import Node

def create_rule(rule_string):
    # This function parses the rule_string into an AST.
    # Simple parser example; you'd want a real parser here.
    # This is just a placeholder for demonstration.
    if "AND" in rule_string:
        left = create_rule(rule_string.split("AND")[0].strip())
        right = create_rule(rule_string.split("AND")[1].strip())
        return Node(type_="operator", left=left, right=right, value="AND")
    elif "OR" in rule_string:
        left = create_rule(rule_string.split("OR")[0].strip())
        right = create_rule(rule_string.split("OR")[1].strip())
        return Node(type_="operator", left=left, right=right, value="OR")
    else:
        # Assuming a simple comparison for operands.
        return Node(type_="operand", value=rule_string)

def combine_rules(rules):
    # Combine rules into a single AST.
    combined_root = None
    for rule in rules:
        if combined_root is None:
            combined_root = create_rule(rule)
        else:
            # Combine using AND for simplicity
            combined_root = Node("operator", left=combined_root, right=create_rule(rule), value="AND")
    return combined_root
