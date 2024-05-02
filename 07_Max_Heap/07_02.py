class Heap:
    def __init__(self, size):
        self.size = size
        self.heap = [None]*size
        self.count = 0

    def __str__(self):
        return "Heap, 0 is Dummy"
    
    def add_heap(self, item):
        #if self.isFull():
         #   return
        self.count += 1
        i = self.count
        while i != 1 and item < self.heap[i // 2]:
            self.heap[i] = self.heap[i // 2]
            i //= 2
        self.heap[i] = item
        print(self.heap)

s = Heap(8)
for i in [7, 16, 49, 82, 5, 31, 6]:
    s.add_heap(i)
