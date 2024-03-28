class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return len(self.s2) == 0 and len(self.s1) == 0

    # migliorata ma sempre O(n) tempo e spazio
    class MyQueue:

        def __init__(self):
            self.s1 = []
            self.s2 = []

        def push(self, x: int) -> None:
            self.s1.append(x)

        def _shift_stacks(self) -> None:
            if not self.s2:
                while self.s1:
                    self.s2.append(self.s1.pop())

        def pop(self) -> int:
            self._shift_stacks()
            return self.s2.pop()

        def peek(self) -> int:
            self._shift_stacks()
            return self.s2[-1]

        def empty(self) -> bool:
            return not self.s1 and not self.s2
