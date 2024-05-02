class InsertionSort:
    def __init__(self, num):
        self.num = num
        self.size = len(num)
        print("Insertion Sort", self.num)

    def __str__(self):
        for i in range(self.size):
            print("%2d " % self.num[i])

    def sort(self):
        for i in range(1, self.size):
            pivot = self.num[i]     # 정렬 예정인 기준수
            j = i - 1               # 기준수 바로 앞의 수
            while j >= 0 and pivot < self.num[j]:   # j가 [0] 위치로 갈 때까지(lower bound 방지) && 기준수가 그 바로 앞 수보다 작다면
                self.num[j + 1] = self.num[j]       # 바로 앞 수를 뒤로 밀어내고
                j -= 1                              # 그 앞 원소와 비교할 준비
            self.num[j + 1] = pivot  # 제 자리 찾았다면, 준비하기 직전의 값이 기준수가 들어갈 위치값
            print(self.num)

num = [13, 25, 9, 12, 34, 52, 49, 17, 5, 8]
s = InsertionSort(num)
s.sort()