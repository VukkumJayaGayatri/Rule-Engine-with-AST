class Evaluator:
    def __init__(self):
        self.variables = {}

    def evaluate(self, node, data):
        if node.type == 'NUMBER':
            return node.value
        elif node.type == 'IDENTIFIER':
            return data.get(node.value, 0)
        elif node.type == 'AND':
            return self.evaluate(node.left, data) and self.evaluate(node.right, data)
        elif node.type == 'OR':
            return self.evaluate(node.left, data) or self.evaluate(node.right, data)
        elif node.type in ['<', '<=', '>', '>=', '==', '!=']:
            left = self.evaluate(node.left, data)
            right = self.evaluate(node.right, data)
            if node.type == '<':
                return left < right
            elif node.type == '<=':
                return left <= right
            elif node.type == '>':
                return left > right
            elif node.type == '>=':
                return left >= right
            elif node.type == '==':
                return left == right
            elif node.type == '!=':
                return left != right
        else:
            raise Exception(f"Unknown node type: {node.type}")
