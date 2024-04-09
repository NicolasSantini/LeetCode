class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mins:
            self.mins.append(min(val, self.mins[-1]))
        else:
            self.mins.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.mins:
            return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(5)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
