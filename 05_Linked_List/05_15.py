import random

class Node:
    def __init__(self, item):
        self.data = item
        self.llink = None
        self.rlink = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head == None
    
    def add(self, item):
        node = Node(item)
        if self.empty():                    # 최초 추가할 땐
            self.head = node
            self.tail = node
            node.rlink = node    # LR링크 모두 자기 자신을 가리키게
            node.llink = node
        elif self.head.rlink == self.head:      #두 번째 항목 추가할 때
            self.tail = node
            node.llink = self.head              #최초 항목과 두 번째 항목 연결
            node.rlink = self.head
            self.head.llink = node
            self.head.rlink = node
        else:                               # 3개 이상: 가장 마지막 항목으로 추가
            self.tail.rlink = node
            node.llink = self.tail
            self.tail = node
            node.rlink = self.head
            self.head.llink = node
        return node

    def delete(self, item):
        if self.empty():
            print("List Empty")
            return
        node = self.find(item)
        if not node:
            print("Not Found")
            return
        if node == self.head:               #기존 헤드 삭제될 시 2번째 항목이 헤드가 됨
            self.head = self.head.rlink
        node.llink.rlink = node.rlink
        node.rlink.llink = node.llink
        del node

    def find(self, item):
        temp = self.head
        while temp != self.tail:
            if temp.data == item: 
                return temp
            temp = temp.rlink
        if temp.data == item:
            return temp
        else:
            return None
        
    def view(self):
        temp = self.head
        print("[", end = ' ')
        while temp != self.tail:
            print(temp.data, end = ' ')
            temp = temp.rlink
        print(temp.data, "]")

class hide_and_seek:
    def __init__(self):
        num = int(input("노드 수 >> "))
        self.board = LinkedList()
        self.player = ['p1', 'p2']
        for i in range(num):
            if i == 0:            # Player 1
                self.player[0] = self.board.add(1)
            elif i == num / 2:    # Player 2 = 1과 대각선 위치
                self.player[1] = self.board.add(2)
            else:
                self.board.add(0)
        self.way = '+'
        print("Game Start!")
        print("Player 초기 위치")
        self.board.view()
    
    def play_game(self):
        isEnd = False
        while True:
            for i in range(len(self.player)):
                dice = (random.randint(1,6), random.randint(1,6))
                if dice == (6, 6):          # (6, 6) 이동 방향 전환
                    if self.way == '+':
                        way = '-'
                        print(i+1, dice, "이동방향 전환: ←")
                    else:
                        way = '+'
                        print(i+1, dice, "이동방향 전환: →")

                elif dice == (5, 5):
                    print(i+1, dice, "말의 위치 교환 ↔")
                    self.player[0].data = 2
                    self.player[1].data = 1
                    self.player[0].data, self.player[1].data = self.player[1].data, self.player[0].data
                    self.board.view()


                elif dice == (1, 1):
                    print(i+1, dice, "1칸 후진")
                    isEnd = self.move(self.player[i], i, 1, True)
                    if isEnd == True:
                        break
                    else:
                        self.board.view()

                else:
                    spots = dice[0] + dice[1]
                    print(i+1, dice, "%d칸 전진" %(spots))
                    isEnd = self.move(self.player[i], i, spots)
                    if isEnd == True:
                        break
                    else:
                        self.board.view()
            if isEnd == True:
                print(i+1, "player won!")
                break

    def move(self, player, j, amount, back = False):
        start = self.board.find(j+1)
        start.data = 0
        temp = start
        if back == True:
            if self.way == '+':
                temp = temp.llink
            else:
                temp = temp.rlink
        else:
            for i in range(amount):
                if self.way == '+':
                    temp = temp.rlink
                else:
                    temp = temp.llink
        dest = temp
        if self.isWin(dest):
            return 1
        else:
            dest.data = j + 1
            return 0

    def isWin(self, player):
        if player.data != 0:
            return True

    
game = hide_and_seek()
game.play_game()