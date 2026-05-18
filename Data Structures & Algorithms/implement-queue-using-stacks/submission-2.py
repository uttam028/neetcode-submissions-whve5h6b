class MyQueue:

    def __init__(self):
        self.main = []
        self.buffer = []

    def push(self, x: int) -> None:
        self.main.append(x)

    def pop(self) -> int:
        data = self.main[0]
        while(len(self.main) > 1):
            self.buffer.append(self.main.pop())
        self.main.pop()
        for i in range(len(self.buffer)):
            self.main.append(self.buffer.pop())
        self.buffer = []
        return data

    def peek(self) -> int:
        return self.main[0]

    def empty(self) -> bool:
        return len(self.main) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()