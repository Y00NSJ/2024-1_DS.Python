class QuickSort:
    def __init__(self, num):
        self.num = num
        self.size = len(num)
        print("Quick Sort", self.num)
    
    def __str__(self):
        for i in range(self.size):
            print("%2d " % self.num[i])
    
    def swap(self, a, b):
        self.num[a], self.num[b] = self.num[b], self.num[a]
    
    def sort(self, left, right):
        if left < right:
            i = left
            j = right + 1
            pivot = self.num[left]
            while True:
                while True:
                    i += 1
                    if i > right or self.num[i] >= pivot:
                        break
                while True:
                    j -= 1
                    if j < left or self.num[j] <= pivot:
                        break
                if i < j:
                    self.swap(i, j)
                    print(self.num)
                else:
                    break
                
            self.swap(left, j)
            if left != j:
                print(self.num)
            #print("L-sort", left, j - 1)
            self.sort(left, j - 1)
            #print("R-sort", j+1, right)
            self.sort(j + 1, right)


num = [25, 30, 17, 14, 49, 66, 23, 39]
s = QuickSort(num)
s.sort(0, len(num) - 1)