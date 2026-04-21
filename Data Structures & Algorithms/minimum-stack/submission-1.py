class MinStack:

    def __init__(self):
        self.stack = []
        self.minElement = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1 or self.minElement > val:
            self.minElement = val

    def pop(self) -> None:
        prev_top = self.stack.pop()
        if self.minElement == prev_top and len(self.stack) != 0:
            self.minElement = self.top()
            for i in range(len(self.stack) - 1, -1, -1):
                self.minElement = min(self.stack[i], self.minElement)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minElement
        
