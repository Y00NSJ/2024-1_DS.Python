#program 3.7_loop & stack ver.
class Stack:
    def __init__(self):
        self.stack = []
    def empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    def push(self, item):
        self.stack.append(item)
        #self.view()
    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            print("Stack Empty")
    def view(self):
        print(self.stack)
    def search(self, item):
        return item in self.stack


class Maze:
    def __init__(self):
        self.maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ], \
                     [1, 0, 0, 1, 0, 0, 0, 0, 1, 1 ], \
                     [1, 1, 0, 1, 0, 1, 1, 0, 0, 1 ], \
                     [1, 0, 0, 0, 0, 1, 1, 1, 1, 1 ], \
                     [1, 0, 1, 1, 0, 1, 0, 0, 0, 1 ], \
                     [1, 0, 0, 1, 0, 1, 1, 0, 1, 1 ], \
                     [1, 1, 0, 0, 1, 0, 0, 0, 1, 1 ], \
                     [1, 1, 1, 0, 0, 0, 1, 0, 0, 1 ], \
                     [1, 0, 0, 0, 1, 0, 1, 1, 'X', 1 ], \
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]]
        self.mark = [[0] * 10 for i in range(10)]
        self.path = Stack()
        self.found = False

    def empty(self):
        return len(self.path) == 0
    def add(self, row, col):
        self.path.push((row, col))
    def delete(self):
        return self.path.pop()
    def view(self):
        print("path")
        self.path.view()

    def rexplore(self, row, col):
        self.idx = 0
        while True:
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_row = row + x
                next_col = col + y
                if self.maze[next_row][next_col] == 'X':
                    self.add(row, col)
                    self.add(next_row, next_col)
                    self.found = True
                    return True
                elif self.maze[next_row][next_col] == 0 and self.mark[next_row][next_col] == 0:
                    self.mark[next_row][next_col] == 1
                    if not self.path.search((row, col)):        #미방문 위치이면
                        self.add(row, col)
                        self.view()
                        row, col = next_row, next_col
                        break                                       #for문 break, 다음 위치에서 탐색 재개
                    else:                                       #막다른 골목
                        self.delete()                               #next 위치 삭제 후
                        self.idx += 1                               #다음 offset 더해 탐색 실행
            
            if self.idx == 4:                                   #for문 다 돌도록 못 찾음
                return False

m = Maze()
if m.rexplore(1, 1) == True:
    print("탈출 성공")
    m.view()
else:
    print("탈출 경로 없음")