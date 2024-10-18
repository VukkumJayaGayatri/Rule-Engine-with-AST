class ASTNode:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"ASTNode({self.type}, {self.value}, {self.left}, {self.right})"
