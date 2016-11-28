class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.minstack = []
        self.stack = []
        
    def push(self, x):
        if len(self.minstack) == 0:
            self.minstack.append(x)
        elif x <= self.minstack[-1]:
            self.minstack.append(x)
        self.stack.append(x)
        
    # @return nothing
    def pop(self):
        popped = self.stack.pop()
        if popped == self.minstack[-1]:
            self.minstack.pop()
        return popped

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.minstack[-1]
        