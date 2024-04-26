import re


class Evaluator:

    NAMES = ["Omega", "O", "omega", "o", "w", "W"]

    def __init__(self, omega, names):
        self.names = names
        self.omega = omega
        self.operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
            "^": lambda x, y: x**y,
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
            "or": -1,
            "not": 0,
            "#": 0,
            "$": 0,
        }

        self.association_order = {
            "+": "left",
            "-": "left",
            "*": "left",
            "/": "left",
            "^": "right",
            "<": "left",
            ">": "left",
            "<=": "left",
            ">=": "left",
            "==": "left",
            "!=": "left",
            "and": "left",
            "or": "left",
            "not": "right",
            "#": "left",
            "$": "left",
        }

    def set_rule(self, rule: str):
        self.rule = rule
        self.tokens = self.tokenize(rule)
        self.sufix = self.to_sufix()

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def to_sufix(self):
        stack = []
        output = []
        for token in self.tokens:
            if token not in self.operators:

                if token in self.names or token in self.NAMES or self.is_number(token):
                    output.append(token)

            # trunk-ignore(bandit/B105)
            elif token == "(":
                stack.append(token)

            # trunk-ignore(bandit/B105)
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
                        while (
                            len(stack) > 0
                            and self.presedence[token] <= self.presedence[stack[-1]]
                        ):
                            output.append(stack.pop())
                        stack.append(token)
                    else:
                        if self.association_order[token] == "left":
                            while (
                                len(stack) > 0
                                and self.association_order[stack[-1]] == "left"
                            ):
                                output.append(stack.pop())
                            stack.append(token)
                        else:
                            stack.append(token)

        while len(stack) > 0:
            element = stack.pop()

            if element != "(" and element != ")" and element != " " and element != ";":
                output.append(element)

        return output

    def tokenize(self, rule):
        tokens = re.findall(r"[\d.]+|\W|\w+", rule)
        return tokens

    def eval_tuple(self, _tuple):
        stack = []
        sufix = self.sufix
        # st.write(_tuple)

        for token in sufix:
            if token not in self.operators:
                stack.append(token)
            else:
                A = stack.pop()
                B = stack.pop()
                if token == "#":
                    stack.append(A in _tuple or B in _tuple)
                elif token == "$":
                    try:
                        indx = int(B)
                        stack.append(A == _tuple[indx])
                    except Exception:
                        indx = int(A)
                        stack.append(B == _tuple[indx])
                else:
                    stack.append(self.operators[token](B, A))
        return stack

    def find_all(self):
        s = []
        for i in self.omega:
            evalt = self.eval_tuple(i)
            if evalt[0]:
                s.append(i)
        return s
