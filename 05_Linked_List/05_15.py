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
        temp = self.head.rlink
        while temp != self.head:
            if temp.data == item: 
                return temp
            temp = temp.rlink
        if temp.data == item:
            return temp
        else:
            return None
        
    def view(self):
        temp = self.head.rlink
        print("[", end = ' ')
        while temp != self.head:
            print(temp.data, end = ' ')
            temp = temp.rlink
        print(temp.data, "]")

class hide_and_seek:
    def __init__(self):
        num = int(input("노드 수 >> "))
        board = LinkedList()
        for i in range(num):
            board.add(0)
        print("Game Start!")
        print("Player 초기 위치")
        board.view()
    
    def play_game(self):
        return
    
game = hide_and_seek()