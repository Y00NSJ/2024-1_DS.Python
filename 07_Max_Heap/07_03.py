class HeapSort:
    def __init__(self, num):
        self.num = num
        self.size = len(num)
        print("Heap Sort", self.num)

    def __str__(self):
        for i in range(self.size):
            print("%2d " % self.num[i])

    def swap(self, a, b):
        temp = self.num[a]
        self.num[a] = self.num[b]
        self.num[b] = temp
    
    def makeheap(self, root, n):
        temp = self.num[root]
        child = 2 * root
        while child <= n:
            if child < n and self.num[child] > self.num[child + 1]:
                child += 1
            if temp < self.num[child]:
                break
            else:
                self.num[child//2] = self.num[child]
                child *= 2
        self.num[child//2] = temp

    def sort(self):
        n = self.size - 1
        for i in range(n//2, 0, -1):
            self.makeheap(i, n)
        print(self.num)
        for i in range(n-1, 0, 1):
            self.swap(1, i + 1)
            self.makeheap(1, i)
            print(self.num)

s = HeapSort([0, 24, 7, 80, 3, 64, 15, 50, 10, 42, 18])
s.sort()
