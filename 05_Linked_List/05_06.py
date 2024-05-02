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
    
    def add_rear(self, item):
        node = Node(item)
        if not self.head:
            self.head = node
            self.tail = node
        elif self.tail:
            self.tail.link = node
            self.tail = node
        node.link = self.head       #순환!

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

    def length_list(self):
        if not self.head:
            return 0
        count = 0
        temp = self.head
        while True:
            count += 1
            temp = temp.link
            if temp == self.head:
                break
        return count

    def reverseAll(self):
        first = self.head
        end = self.head
        second = third = None
        self.tail = self.head
        while first:
            third = second
            second = first
            first = first.link
            second.link = third
            if first == end:
                break
        self.head = second
        self.view()


    def reverse(self):
        for i in range(self.length_list()):
            temp = self.head
            self.head = self.tail
            while True:
                temp = temp.link
                if temp == self.head:
                    break
        self.view()

lst = SinglyLinkedList()
for item in [20, 10, 30, 50, 40]:
    lst.add_rear(item)
lst.reverseAll()
