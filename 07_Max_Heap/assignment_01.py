class Node:
    def __init__(self, item):
        self.data = item
        self.parent = None
        self.rlink = None
        self.llink = None

class LinkedMaxHeap:
    def __init__(self):
        self.head = Node(0)

    def empty(self):
        return self.head.rlink == self.head
    
    def find(self, item):
        temp = self.head.llink
        if temp == None:
            return None
        self.recursive_search(temp, item)
    
    def recursive_search(self, node, item):
        if item == node.data:
            return node
        if node.llink == None:
            return None
        elif node.rlink == None:
            return None
        self.recursive_search(node.llink, item)
        self.recursive_search(node.rlink, item)

    def view(self):
        temp = self.head.llink
        print("현재 노드 수 : ", self.head.data)
        # 루트 노드만 있으면
        if temp.llink == None:
            print(temp.data)
        
        # 노드 최소 2개 이상
        else:
            # 마지막 노드 직전까지 출력
            while temp != self.head.rlink:
                #print("loop 1")
                print(temp.data, "\t")
                # temp가 루트라면
                if temp == self.head.llink:
                    temp = temp.llink
                # temp가 왼쪽 자식이라면 형제 노드로 이동
                elif temp == temp.parent.llink:
                    temp = temp.parent.rlink
                # temp가 오른쪽 자식이라면 
                elif temp == temp.parent.rlink:
                    # 잎 노드라면 부모의 형제의 왼쪽 자식으로 이동 = 마지막 노드의 왼쪽 형제 노드
                    if temp.llink == None:
                        temp = self.head.rlink.parent.llink
                        
                    # 왼쪽 형제의 자식으로 이동
                    else:
                        temp = temp.parent.llink.llink
                        print()
            print(temp.data)
    
    def traversal(self, node):
        print(node.llink, "\t", node.rlink)

    def swap(self, a, b):
        a.data, b.data = b.data, a.data

    def add_heap(self, item):
        self.head.data += 1
        count = self.head.data

        if self.find(item):     # 1. 기존 최대힙에 동일 값이 있는지 확인
            print("동일한 값이 이미 존재합니다.")
            return
        
        node = Node(item)       # 삽입될 값에 대한 DLL 노드 생성

        # 2. 마지막 노드 다음 위치에 node 추가
        if count == 1:          # 루트 노드 추가
            self.head.rlink = node
            self.head.llink = node
        else:
            if self.head.llink.llink == None or self.head.llink.rlink == None:
                if self.head.rlink.llink == None:
                    self.head.rlink.llink = node
                    node.parent = self.head.rlink.llink
                    self.head.rlink = node
                else:
                    self.head.rlink.rlink = node
                    node.parent = self.head.rlink.rlink
                    self.head.rlink = node

            # 2-a) 마지막 노드 부모가 오른쪽 자식이 없으면
            if self.head.rlink.parent.rlink == None:
                # 마지막 노드 부모의 오른쪽 자식으로 추가
                self.head.rlink.parent.rlink = node
                node.parent = self.head.rlink.parent.rlink
                self.head.rlink = node
            # 2-b) 마지막 노드 부모가 양쪽 자식이 모두 있으면
            else:
                # 마지막 노드 부모의 왼쪽 자식의 자식으로 추가
                self.head.rlink.parent.llink.llink = node
                node.parent = self.head.rlink.parent.llink.llink
                self.head.rlink = node

         # 3. 제 자리 찾을 때까지 data끼리 swap
        if self.head.data > 1:
            pointer = self.head.rlink
            while pointer.parent == None:
                #print("loop 2")
                if pointer.data > pointer.parent.data:
                    self.swap(pointer.data, pointer.parent.data)
                    pointer = pointer.parent
                else:
                    break


        
ex1 = LinkedMaxHeap()
for item in [10, 20, 30, 40, 56, 35, 60, 70, 85]:
    ex1.add_heap(item)
    ex1.view()
    print()