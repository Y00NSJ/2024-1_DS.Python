class Sym:
    OPEN_B = 1
    CLOSE_B = 2
    PLUS = 3
    MINUS = 4
    TIMES = 5
    DIVIDE = 6
    MOD = 7
    OPERAND = 8

class Expression:
    def __init__(self, expr):
        self.stack = []
        self.size = 100
        self.expr = expr
        self.top = -1
        self.output = []

    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.stack.append(item)
            #self.show_stack()
        else:
            print("Stack Full")
    
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.stack.pop()
        else:
            print("Stack Empty")

    def show_stack(self): print(self.stack)

    def isEmpty(self): return len(self.stack) == 0
    
    def isFull(self): return len(self.stack) == self.size

    def getSymtype(self, sym):
        if sym == '(' : sym_type = Sym.OPEN_B
        elif sym == ')' : sym_type = Sym.CLOSE_B
        elif sym == '+' : sym_type = Sym.PLUS
        elif sym == '-' : sym_type = Sym.MINUS
        elif sym == '*' : sym_type = Sym.TIMES
        elif sym == '/' : sym_type = Sym.DIVIDE
        elif sym == '%' : sym_type = Sym.MOD
        elif sym == ' ' : sym_type = 'space'
        else: sym_type = Sym.OPERAND
        return sym_type
    
    def eval_postfix(self): 
        for sym in self.expr:
            sym_type = self.getSymtype(sym)
            if sym_type == Sym.OPERAND:     
                self.push(int(sym))            
                print("스택:", self.stack)
            else:
                op2 = self.pop()
                op1 = self.pop()
                print("연산:", op1, op2, sym, "\n")
                if sym_type == Sym.PLUS:
                    self.push(op1 + op2)
                elif sym_type == Sym.MINUS:
                    self.push(op1 - op2)
                elif sym_type == Sym.TIMES:
                    self.push(op1 * op2)
                elif sym_type == Sym.DIVIDE:
                    self.push(op1 // op2)
                elif sym_type == Sym.MOD:
                    self.push(op1 % op2)
                print("스택:", self.stack)
        print("evaluation:", self.pop())                   #최종 계산 값 전달
    
    def infix_postfix(self):   
        temp = ""
        for i in range(len(self.expr)):
            token = self.expr[i]
            if token == ' ':
                continue

            elif token.isalnum(): #알파벳/숫자인지 판별하는 내장함수
                if (i+1) >= len(self.expr) or not self.expr[i + 1].isalnum():
                    temp += self.expr[i]
                    self.output.append(int(temp))
                    temp = "" 
                    print("postfix:", self.output)
                else:
                    temp += self.expr[i]        #temp 문자열에 추가
                    continue
                
                
            elif token == '(':
                self.push(token)
                print("스택:", self.stack)
                
            elif token == ')':
                sym = self.pop()
                while sym != '(':
                    self.output.append(sym)
                    sym = self.pop()
                
            else:
                while not self.isEmpty() and self.precedence(self.stack[-1]) >= self.precedence(token):
                    sym = self.pop()
                    self.output.append(sym)
                self.push(token)
                print("스택:", self.stack)

        while not self.isEmpty():
            self.output.append(self.pop())
            print("postfix:", self.output)
        print('-------')

    def precedence(self, op):
        if op == '(' : return 0
        elif op in ['+', '-']: return 1
        elif op in ['*', '/', '%']: return 2
    
while True:
    expr = input("수식을 입력하세요(-1 입력 시 종료) >> ")
    if expr == '-1':
        break
    else: # ******변환과정 노션 참고******
        e = Expression(expr)
        e.infix_postfix()
        print("infix to postfix : ", e.output)
        e.stack = []
        e.expr = e.output
        print('-------')
        print("expr to evaluate : ", e.output)
        e.eval_postfix()
        print()

