class ShellSort:
    def __init__(self, num):
        self.num = num
        self.size = len(num)
        print("Shell Sort", self.num)

    def __str__(self):
        for i in range(self.size):
            print("%2d " % self.num[i])
    
    def sort(self):
        n = self.size
        gap = n // 2
        while gap > 0:
            if gap % 2 == 0:
                gap += 1
            for i in range(gap, n):
                h = 1       # 그 다음 gap의 위치
                while i * h < n:
                    j = i * h   # gap의 위치(=pivot)
                    temp = self.num[i * h]
                    while j >= gap:
                        if temp < self.num[j - gap]:    # j - gap = 비교 대상 수
                            self.num[j] = self.num[j - gap]
                        else:
                            break
                        j -= gap    # gap 만큼 앞으로 jump해 재비교 (a - 6, a - 3, a)
                    self.num[j] = temp
                    h += 1
                    print(gap, i)
                print(gap, i, self.num)
            print(gap, self.num, "\n")
            gap //= 2

num = [77, 62, 80, 40, 30, 21, 14, 25, 9]
s = ShellSort(num)
s.sort()