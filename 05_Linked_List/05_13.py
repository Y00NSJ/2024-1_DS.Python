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

class atm:
    def __init__(self):
        self.account_list = SinglyLinkedList()
        for customer in [["가", 1000, 0, 1], ["나", 10000, 2000, 2], ["다", 100000, 2000, 1], ["라", 500000, 10000, 1]]:
            self.account_list.attatch(customer)
    
    def view_info(self):
        temp = self.account_list.head
        print("전체 고객 정보")
        while temp:
            print("이름 :", temp.data[0]); print("예금 잔액 :", temp.data[1]); print("대출 잔액 :", temp.data[2]); print("대출 금리 :", temp.data[3])
            temp = temp.link
        print("--------------")
    
    def avr_deposit(self):
        dsum = 0
        count = 0
        temp = self.account_list.head
        while temp:
            dsum += temp.data[1]
            count += 1
        print("평균 예금 잔액 :", dsum / count)
    
    def avr_loan(self):
        lsum = 0
        count = 0
        temp = self.account_list.head
        while temp:
            lsum += temp.data[1]
            count += 1
        print("평균 예금 잔액 :", lsum / count)
    
    def highst_cust(self):
        max_asset = 0
        max_nasset = 0
        ma = None
        mna = None
        temp = self.account_list.head
        while temp:
            asset = temp.data[1] + temp.data[2]
            nasset = temp.data[1] - temp.data[2]
            if asset > max_asset:
                max_asset = asset
                ma = temp
            if nasset > max_nasset:
                max_nasset = nasset
                mna = temp
        print("자산 최고 고객 계좌 정보")
        print("이름 :", ma.data[0]); print("예금 잔액 :", ma.data[1]); print("대출 잔액 :", ma.data[2]); print("대출 금리 :", ma.data[3])
        print("\n순자산 최고 고객 계좌 정보")
        print("이름 :", mna.data[0]); print("예금 잔액 :", mna.data[1]); print("대출 잔액 :", mna.data[2]); print("대출 금리 :", mna.data[3])