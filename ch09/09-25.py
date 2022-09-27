class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k 
        self.length = k
        self.rear_idx = k - 1
        self.front_idx = 0
    
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.rear_idx = (self.rear_idx + 1) % (self.length)
            self.queue[self.rear_idx] = value
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False 
        else:
            self.queue[self.front_idx] = None
            self.front_idx = (self.front_idx + 1) % (self.length)
            return True

    def Front(self) -> int:
        if self.queue[self.front_idx] == None:
            return -1
        return self.queue[self.front_idx]
            
    def Rear(self) -> int:
        if self.queue[self.rear_idx] == None:
            return -1
        return self.queue[self.rear_idx]
    
    def isEmpty(self) -> bool:
        rear_next = (self.rear_idx + 1) % self.length
        return self.front_idx == rear_next and self.queue[rear_next] == None

    def isFull(self) -> bool:
        rear_next = (self.rear_idx + 1) % self.length
        return rear_next == self.front_idx and self.queue[rear_next]


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()