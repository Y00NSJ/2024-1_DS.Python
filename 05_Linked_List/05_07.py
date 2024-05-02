class Node:
    def __init__(self, item):
        self.data = item
        self.link = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return not self.head
    
    def attatch(self, item):
        node = Node(item)
        if not self.head:
            self.head = node
            self.tail = node
        elif self.tail:
            self.tail.link = node
            self.tail = node

    def find(self, item):
        if not self.head:
            return None, None       #prev, temp(현재)
        temp = self.head
        prev = None
        while temp:
            if temp.data == item:
                return prev, temp
            prev = temp
            temp = temp.link
        return None, None           #if temp == None
    
    def insert(self, prev, item):
        if not self.head:
            return
        node = Node(item)
        if not prev:
            node.link = self.head
            self.head = node
            return
        before, temp = self.find(prev)
        if not temp:
            print("앞 노드 없음")
            return
        else:
            node.link = temp.link
            temp.link = node
            if not node.link:
                self.tail = node

    def delete(self, item):
        if not self.head:
            print("빈 리스트")
            return
        prev, node = self.find(item)
        if not node:
            print("해당 노드 없음")
            return
        if prev:
            prev.link = node.link
            print("노드 삭제됨")
        else:
            if self.head == node:
                print("첫 노드 삭제됨")
                self.head = node.link
        if node == self.tail:
            self.tail = prev
        del node

    def view(self):                 #리스트 출력
        temp = self.head
        print("[", end = ' ')
        while temp:
            print(temp.data, end = ' ')
            temp = temp.link
        print("]", end = ' ')
        if self.head:
            print("H =", self.head.data, "T =", self.tail.data)
        else:
            print("빈 리스트")

    def deleteAll(self):
        temp = self.head
        while temp:
            del_node = temp
            temp = temp.link
            del del_node
        print("--Delete All--")
        self.head = None
    
    def add_sort(self, item):
        node = Node(item)
        if not self.head:
            self.head = node
            self.tail = node
            return
        temp = self.head
        prev = None
        while temp:
            if item > temp.data:
                prev = temp
                temp = temp.link
            elif item == temp.data:
                print("중복")
                return
            else:
                node.link = temp
                if prev:
                    prev.link = node
                else:
                    self.head = node
                return
        prev.link = node
        self.tail = node

lst = SinglyLinkedList()
for item in [20, 10, 30, 50, 40]:
    lst.add_sort(item)
lst.view()