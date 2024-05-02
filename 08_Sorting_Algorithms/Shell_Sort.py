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
                h = 1
                while i * h < n:
                    j = i * h
                    temp = self.num[i * h]
                    while j >= gap:
                        if temp < self.num[j - gap]:
                            self.num[j] = self.num[j - gap]
                        else:
                            break
                        j -= gap
                    self.num[j] = temp
                    h += 1
            print(gap, self.num)
            gap //= 2

num = [38, 32, 17, 5, 18, 25, 12, 7, 2]
s = ShellSort(num)
s.sort()