class SelectionSort:
    def __init__(self, num):
        self.num = num
        self.size = len(num)
        print("Selection Sort", self.num)   # 정렬 전 리스트

    def __str__(self):
        for i in range(self.size):
            print("$2d " % self.num[i])

    def swap(self, a, b):
        self.num[a], self.num[b] = self.num[b], self.num[a]

    def sort(self):
        n = self.size
        for i in range(n - 1):
            min = i     # 최솟값 우선 선택
            for j in range(i + 1, n):
                if self.num[j] < self.num[min]:
                    min = j
            self.swap(i, min)
            print(self.num)

num = [31, 10, 9, 23, 49, 15, 11, 7]
s = SelectionSort(num)
s.sort()