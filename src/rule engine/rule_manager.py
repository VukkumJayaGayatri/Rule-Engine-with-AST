from .ast import Node
import re

def create_rule(rule_string):
    # Parse the rule string to build an AST
    tokens = re.findall(r'\(|\)|\w+|[<>=!]+|AND|OR', rule_string)
    return build_ast(tokens)

def build_ast(tokens):
    stack = []
    operators = []

    for token in tokens:
        if token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                right = stack.pop()
                operator = operators.pop()
                left = stack.pop()
                node = Node('operator', left, right, operator)
                stack.append(node)
            operators.pop()  # Pop the '('
        elif token in ['AND', 'OR']:
            while (operators and operators[-1] in ['AND', 'OR']):
                right = stack.pop()
                operator = operators.pop()
                left = stack.pop()
                node = Node('operator', left, right, operator)
                stack.append(node)
            operators.append(token)
        else:
            # Assuming the token is an operand (e.g., "age", "salary")
            match = re.match(r"(\w+)\s*([<>=!]+)\s*(\d+|'[a-zA-Z]+')", token)
            if match:
                operand, operator, value = match.groups()
                node = Node('operand', value=value)
                stack.append(node)
            else:
                raise ValueError(f"Invalid token: {token}")

    while operators:
        right = stack.pop()
        operator = operators.pop()
        left = stack.pop()
        node = Node('operator', left, right, operator)
        stack.append(node)

    return stack[0]

def combine_rules(rules):
    combined = Node('operator', None, None, 'OR')  # Combine rules with OR for simplicity
    for rule in rules:
        rule_node = create_rule(rule)
        combined.left = combined.right
        combined.right = rule_node
    return combined

def evaluate_rule(rule_node, data):
    if rule_node.type == 'operand':
        return evaluate_operand(rule_node.value, data)
    elif rule_node.type == 'operator':
        left_result = evaluate_rule(rule_node.left, data)
        right_result = evaluate_rule(rule_node.right, data)
        return evaluate_operator(left_result, right_result, rule_node.value)
    
def evaluate_operand(operand_value, data):
    # Parse the operand and evaluate based on the data
    # This will need further implementation
    pass

def evaluate_operator(left_result, right_result, operator):
    if operator == 'AND':
        return left_result and right_result
    elif operator == 'OR':
        return left_result or right_result
    return False
