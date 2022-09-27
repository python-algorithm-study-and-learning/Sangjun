class MyStack:
    def __init__(self):
        self.queue = collections.deque();

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft());
        return self.queue.popleft();
    
    def top(self) -> int:
        return self.queue[-1]
        
    def empty(self) -> bool:
        if len(list(self.queue)) != 0: 
            return False
        else: 
            return True
        