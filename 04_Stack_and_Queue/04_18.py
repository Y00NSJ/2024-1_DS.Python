class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1
    
    def push(self, item):
        if self.top < self.size - 1:
            self.top += 1
            return self.stack.append(item)
        else:
            print("stack full")
    
    def pop(self):
        if self.top > -1:
            self.top -= 1
            return self.stack.pop()
        else: 
            print("stack empty")

    def show_stack(self):
        print(self.stack)

class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.front = -1
        self.rear = -1
    
    def push(self, item):
        if self.rear < self.size - 1:
            self.rear += 1
            return self.queue.append(item)
        else:
            print("queue full")
    
    def pop(self):
        if self.front < self.size - 1:
            self.front += 1
            return self.queue.pop(0)
        else:
            print("queue empty")
    
    def show_queue(self):
        print(self.queue)

q = Queue(5)
for item in range(3, 9):
    q.push(item)
    q.show_queue()
for i in range(6):
    q.pop()
    q.show_queue()
