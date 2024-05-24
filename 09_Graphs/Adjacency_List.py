class Node:
    def __init__(self, value):
        self.data = value

class Graph:
    def __init__(self):         # Initialize : 전체 인접 리스트 생성
        self.graph = {}         # 딕셔너리로 구현

    def create(self, v, data):  # 정점 v의 인접 리스트에 인접 정점 data를 노드로 추가
        node = Node(data)
        if v not in self.graph: # 정점 v의 인접 리스트 생성
            self.graph[v] = []  # key : value = v : []
        self.graph[v].append(node)  # data 정점을 노드로 추가
    
    def show(self):
        for no, alist in self.graph.items():    # 딕셔너리에서 item은 key, value 리턴
            print("[", no, "] :", end = ' ')      # [ 정점 V ]
            for node in alist:                    # value인 alist를 돌면서
                print(node.data, end = ' ')
            print()

g = Graph()
for v, node in [(1, 2), (1, 4), (2, 3), (2, 5), (3, 4)]:    #튜플 (a, b) 의 a = v, b = node
    g.create(v, node)
g.show()