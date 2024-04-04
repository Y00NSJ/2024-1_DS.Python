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
    
    def show_stack(self): print(self.stack)

    def eval_postfix(self):
        temp = ""                   #operand를 문자 형태로 저장할 임시 변수
        for i in range(len(self.expr)):
            sym_type = self.getSymtype(self.expr[i])
            if sym_type == 'space':
                continue
            elif sym_type == Sym.OPERAND:     # 읽은 게 operand이면
                while self.getSymtype(self.expr[i + 1]) == Sym.OPERAND:     # operator 만날 때까지
                    temp += self.expr[i]        #temp 문자열에 추가
                self.push(int(temp))            #operator 만나면 int로 캐스팅해 push
                print(temp, end = ' ')
            else:
                print(self.expr[i], end = ' ')
                op2 = self.pop()
                op1 = self.pop()
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
        return self.pop()                   #최종 계산 값 전달

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
    

while True:
    expr = input("수식을 입력하세요(-1 입력 시 종료) >> ")
    if expr == -1:
        break
    else:
        e = Expression(expr)
        #print("수식 : ", expr)
        print("결과값 =", e.eval_postfix())
        print()