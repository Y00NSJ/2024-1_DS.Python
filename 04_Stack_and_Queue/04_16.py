class Expression:
    def __init__(self, expr):
        self.stack = []
        self.size = 100
        self.expr = expr
        self.top = -1

    def push(self, item):
        self.top += 1
        self.stack.append(item)
        #self.show_stack()

    def pop(self):
        if len(self.stack) > 0:
            self.top -= 1
            return self.stack.pop()
        else:
            print("Stack Empty")

    def isMatch(self):
        bracket = [0, 0]
        double = False
        for token in self.expr:
            if token == '{':
                bracket[0] = 1
            if token == '(':
                if bracket[1] == 1:
                    double = True
                else:
                    bracket[1] = 1
            if token == ')':
                if bracket[1] == 1:
                    break
                bracket[1] = 0
            if token == '}':
                bracket[0] = 0
        if bracket[0] == 1 or bracket[1] == 1:
            print("수식 괄호 맞지 않음")
        else:
            print("수식 괄호 맞음")




while True:
    expr = input("수식 입력 (-1 입력 시 종료) >> ")
    if expr == '-1':
        break
    else:
        e = Expression(expr)
        e.isMatch()
    