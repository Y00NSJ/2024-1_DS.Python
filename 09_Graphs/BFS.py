# DFS : recursion
class Node:
    def __init__(self, value):
        self.data = value

class Graph:
    def __init__(self):
        self.graph = {}
        self.visit = []     # 방문 여부 기록
        self.queue = []
    
    def create(self, v, data):      # 정점 v의 인접 리스트에 노드 추가
        node = Node(data)
        if v not in self.graph:     # 인접 리스트가 아직 없다면 새로 생성
            self.graph[v] = []
        self.graph[v].append(node)  # 노드 추가
    
    def addq(self, v):
        self.queue.append(v)
    
    def delq(self):
        if self.queue: return self.queue.pop(0)
        else: print("Queue Empty")

    def bfs(self, v):
        self.visit.append(v)        # 방문 사실 기록
        self.visit.append(v)        # 시작 예정 노드 추가

        while True:
            v = self.delq()         # First Out
            for node in self.graph[v]:  # 정점 v의 인접리스트 내 모든 노드에 대해
                if node.data not in self.visit: # 미방문 노드라면
                    self.visit.append(node.data)    # 방문 기록 추가
                    self.addq(node.data)            # 큐에 그 노드 추가(방문 대기열 줄서기)
    
    def show(self):
        for no, alist in self.graph.items():    # 딕셔너리에서 item은 key, value 리턴
            print("[", no, "] :", end = ' ')      # [ 정점 V ]
            for node in alist:                    # value인 alist를 돌면서
                print(node.data, end = ' ')
            print()