from .ast_node import ASTNode

class RuleParser:
    def __init__(self):
        self.tokens = []
        self.current = 0

    def parse(self, rule_string):
        self.tokens = rule_string.split()
        self.current = 0
        return self.expression()

    def expression(self):
        return self.logical_or()

    def logical_or(self):
        expr = self.logical_and()
        while self.match('OR'):
            right = self.logical_and()
            expr = ASTNode('OR', left=expr, right=right)
        return expr

    def logical_and(self):
        expr = self.equality()
        while self.match('AND'):
            right = self.equality()
            expr = ASTNode('AND', left=expr, right=right)
        return expr

    def equality(self):
        expr = self.comparison()
        while self.match('==', '!='):
            operator = self.previous()
            right = self.comparison()
            expr = ASTNode(operator, left=expr, right=right)
        return expr

    def comparison(self):
        expr = self.term()
        while self.match('<', '<=', '>', '>='):
            operator = self.previous()
            right = self.term()
            expr = ASTNode(operator, left=expr, right=right)
        return expr

    def term(self):
        if self.match('('):
            expr = self.expression()
            self.consume(')', "Expect ')' after expression.")
            return expr
        elif self.is_number(self.peek()):
            return ASTNode('NUMBER', value=float(self.advance()))
        elif self.is_identifier(self.peek()):
            return ASTNode('IDENTIFIER', value=self.advance())
        else:
            raise Exception(f"Unexpected token: {self.peek()}")

    def match(self, *types):
        for t in types:
            if self.check(t):
                self.advance()
                return True
        return False

    def check(self, t):
        if self.is_at_end():
            return False
        return self.peek() == t

    def advance(self):
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def is_at_end(self):
        return self.current >= len(self.tokens)

    def peek(self):
        if self.is_at_end():
            return None
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]

    def consume(self, t, message):
        if self.check(t):
            return self.advance()
        raise Exception(message)

    @staticmethod
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_identifier(s):
        return s.isalpha()
