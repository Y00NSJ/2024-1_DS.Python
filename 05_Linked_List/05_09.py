class Node:
    def __init__(self, item):
        self.data = item
        self.rlink = None
        self.llink = None

class DoubleLinkedlist:
    def __init__(self):
        self.head = Node(0)
        self.head.rlink = self.head
        self.head.llink = self.head

    def empty(self):
        return self.head.rlink == self.head
    
    def find(self, item):
        temp = self.head.rlink
        while temp != self.head:
            if temp.data == item:
                return temp
            temp = temp.rlink
        return None
    
    def view(self):
        temp = self.head.rlink
        print("[", end=' ')
        while temp != self.head:
            print(temp.data, end=' ')
            temp = temp.rlink
        print("]", end=' ')
        if not self.empty():
            print("H=%d R=%d I=%d" %(self.head.rlink.data, self.head.llink.data, self.head.data))
        else:
            print("List is Empty")



    def add(self, item):
        node = Node(item)
        self.head.data += 1
        if self.empty():
            node.llink = self.head
            node.rlink = self.head
            self.head.rlink = node
            self.head.llink = node
        else:
            node.llink = self.head.llink
            node.rlink = self.head
            self.head.llink.rlink = node
            self.head.llink = node

    def reverse(self):
        prev = None
        temp = self.head.rlink
        start = self.head.rlink
        
        while temp:
            next = temp.rlink
            temp.rllink = prev
            temp.llink = next
            prev = temp
            temp = next
            if temp == self.head:
                break
        temp.rlink = prev
        temp.llink = self.head
        self.head.rlink, self.head.llink = self.head.llink, self.head.rlink


lst = DoubleLinkedlist()
for item in [100, 200, 300]:
    lst.add(item)
lst.view()
lst.reverse()
lst.view()
