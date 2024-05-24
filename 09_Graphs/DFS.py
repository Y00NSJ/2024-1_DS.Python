# DFS : recursion
class Node:
    def __init__(self, value):
        self.data = value

class Graph:
    def __init__(self):
        self.graph = {}
        self.visit = []     # 방문 여부 기록
    
    def create(self, v, data):      # 정점 v의 인접 리스트에 노드 추가
        node = Node(data)
        if v not in self.graph:     # 인접 리스트가 아직 없다면 새로 생성
            self.graph[v] = []
        self.graph[v].append(node)  # 노드 추가
    
    def dfs(self, v):
        self.visit.append(v)        # 방문 사실 기록
        for node in self.graph[v]:  # 인접 리스트 v의 노드들에 대해
            if node.data not in self.visit: # 방문 리스트에 없는 노드라면
                self.dfs(node.data)         # 재귀!
    
    def show(self):
        for no, alist in self.graph.items():    # 딕셔너리에서 item은 key, value 리턴
            print("[", no, "] :", end = ' ')      # [ 정점 V ]
            for node in alist:                    # value인 alist를 돌면서
                print(node.data, end = ' ')
            print()