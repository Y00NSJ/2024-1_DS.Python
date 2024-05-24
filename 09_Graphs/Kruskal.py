class Node:
    def __init__(self, value):
        self.data = value

class Graph:
    def __init__(self):
        self.graph = {}     # 인접 리스트
        self.v_list = {}    # 정점 집합 딕셔너리 : 초기엔 모든 정점 집합의 카디날리티 1
        self.edge = []      # 신장 트리 edge 리스트
        self.total = 0      # 가중치 총합

    def create(self, v, data, weight):
        node = Node(data)
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append((node, weight))    # (노드, 가중치) 저장
    
    def sort_edge(self, network):    # 간선 비용을 오름차순으로 정렬해 리스트로 리턴
        temp = []
        for v1, v2, cost in network:
            temp.append((cost, v1, v2))
        temp.sort()
        return temp
    
    def find(self, v2):     # v2가 속한 집합 찾기
        for v1, lst in self.v_list.items():
            if v2 == v1:    # v2가 key라면
                return v1
            if v2 in self.v_list[v1]:   #v2가 key의 value에 있다면
                return v1
        return -1
    
    def union(self, s1, s2):    # 두 집합 합치기
        if s1 < s2:
            self.v_list[s1].append(s2)      # 집합 내 가장 앞 원소(min) 비교
            self.v_list[s1].extend(self.v_list[s2])     # min 원소가 더 작은 집합으로 편입
            del self.v_list[s2]
        else:
            self.v_list[s2].append(s1)
            self.v_list[s2].extend(self.v_list[s1])
            del self.v_list[s1]

    def kruskal(self):
        # 초기 셋팅
        for v1, v2, cost in network:    # network는 (v1, v2, 가중치)의 형태로 시작 시 주어짐
            if v1 not in self.v_list:
                self.v_list[v1] = []    # 새로운 정점 집합
            if v2 not in self.v_list:
                self.v_list[v2] = []
        print("set list = ", self.v_list)
        # 정렬
        sort_network = self.sort_edge(network)   # [ (가중치, v1, v2) ] 로 리턴
        print("cost sorted (cost, v1, v2) : ", sort_network, "\n")
        print("\n ***** Edge Selection Strategies - Kruskal *****")
        for cost, v1, v2 in sort_network:
            print("(", v1, ",", v2, ")", "cost =", cost, end = ' ')
            print()
            s1 = self.find(v1)
            s2 = self.find(v2)
            print("v1 set : ", s1, " | v2 set : ", s2)
            if s1 == s2:
                print("Same set. Rejected for cycle")
                continue
            # 두 정점이 속한 집합이 다르면 cycle이 형성되지 않을 것!
            self.edge.append((v1, v2, cost))
            self.total += cost
            self.union(s1, s2)
            print(self.v_list, end = "\n")

g = Graph()
network = [(1,5,6),(1,6,8),(2,3,17),(2,6,9),(5,6,7), # (v1, v2, weight)
(3,7,15), (3,4,5), (3,8,3),(4,8,4),(6,7,10)]

for v, node, weight in network:
    g.create(v, node, weight) # add node to graph[v] adj. list
print('network=', network)
g.kruskal()
print()
print('Spanning tree vertices = ', g.v_list)
print('spanning tree edges = ', g.edge)
print('cost total = ', g.total)