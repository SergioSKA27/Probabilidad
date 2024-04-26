import re

class Evaluator:
    
    NAMES = ['Omega','O','omega','o','w','W']
    
    def __init__(self,omega,names):
        self.names = names
        self.omega = omega
        self.operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
            "^": lambda x, y: x ** y,
            "<": lambda x, y: x < y,
            ">": lambda x, y: x > y,
            "<=": lambda x, y: x <= y,
            ">=": lambda x, y: x >= y,
            "==": lambda x, y: x == y,
            "!=": lambda x, y: x != y,
            "and": lambda x, y: x and y,
            "or": lambda x, y: x or y,
            "not": lambda x: not x,
            "#": lambda x, y: x in y,
            "$": lambda x, y, z: x == y[z],
        }

        self.presedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "^": 3,
            "<": 0,
            ">": 0,
            "<=": 0,
            ">=": 0,
            "==": 0,
            "!=": 0,
            "and": 0,
            "or": 0,
            "not": 0,
            "#": 0,
            "$": 0,
        }
        
        self.association_order = {
            '+': 'left',
            '-': 'left',
            '*': 'left',
            '/': 'left',
            '^': 'right',
            '<': 'left',
            '>': 'left',
            '<=': 'left',
            '>=': 'left',
            '==': 'left',
            '!=': 'left',
            'and': 'left',
            'or': 'left',
            'not': 'right',
            '#': 'left',
            '$': 'left',
        }
        
    def set_rule(self,rule: str):
        self.rule = rule
        self.tokens = self.tokenize(rule)
    
    
    def to_sufix(self):
        stack = []
        output = []
        for token in self.tokens:
            if token not in self.operators :
                
                if token in self.names or token in self.NAMES:
                    output.append(token)
                
            elif token == "(":
                stack.append(token)

            elif token == ")":
                while stack[-1] != "(":
                    output.append(stack.pop())
                stack.pop()
                
            else:
                if len(stack) == 0:
                    stack.append(token)
                elif self.presedence[token] > self.presedence[stack[-1]]:
                    stack.append(token)
                else:
                    if self.presedence[token] < self.presedence[stack[-1]]:
                        while len(stack) > 0 and self.presedence[token] <= self.presedence[stack[-1]]:
                            output.append(stack.pop())
                        stack.append(token)
                    else:
                        if self.association_order[token] == 'left':
                            while len(stack) > 0 and self.association_order[stack[-1]] == 'left':
                                output.append(stack.pop())
                            stack.append(token)
                        else:
                            stack.append(token)
                
                        
        while len(stack) > 0:
            element = stack.pop()

            if element != "(" and element != ")" and element != " " and element != ";":
                output.append(element)
                
        
        return output
    def tokenize(self,rule):
        tokens = re.findall(r"[\d.]+|\W|\w+", rule)
        return tokens



