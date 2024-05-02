class BubbleSort:
    def __init__(self, num):
        self.num = num
        self.size = len(num)
        print("Bubble Sort", self.num)

    def __str__(self):
        for i in range(self.size):
            print("%2d " % self.num[i])
    
    def swap(self, a, b):
        self.num[a], self.num[b] = self.num[b], self.num[a]

    def sort(self):
        n = self.size
        for i in range(n - 1):
            flag = 0
            for j in range(0, n - i - 1):   # 오른쪽 끝에 최댓값 주고 점차 범위 좁힘
                if self.num[j] > self.num[j + 1]:
                    self.swap(j, j + 1)
                    flag = 1                # 교환완료
            if flag == 0:
                break                       # swap이 더 이상 안 일어나면 break
            print(self.num)

num = [13, 25, 9, 12, 34, 52, 49, 17, 5, 8]
s = BubbleSort(num)
s.sort()